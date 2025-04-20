import pytest

from mitmproxy.addons.browserup import har_capture_addon
from mitmproxy.test import taddons
from mitmproxy.test import tflow
from mitmproxy.test import tutils


class TestHARTracing:
    def flow(self, resp_content=b"message"):
        times = dict(
            timestamp_start=746203200,
            timestamp_end=746203290,
        )

        # Create a dummy flow for testing
        return tflow.tflow(
            req=tutils.treq(method=b"GET", **times),
            resp=tutils.tresp(content=resp_content, **times),
        )

    def test_har_root_tracing_properties(self, hc):
        """Test that the root HAR object has correct trace context properties."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset to ensure clean state
            hc.reset_har_and_return_old_har()
            
            # Verify root trace properties
            har = hc.har
            
            # The HAR log should have a trace_id
            assert "_trace_id" in har["log"]
            
            # The HAR log should have a span_id
            assert "_span_id" in har["log"]
            
            # The HAR log root span should have parent_id set to all zeros (W3C spec)
            assert "_parent_id" in har["log"]
            assert har["log"]["_parent_id"] == "0000000000000000"
            
            # The trace ID should be 32 characters (hex)
            assert len(har["log"]["_trace_id"]) == 32
            
            # The span ID should be 16 characters (half of trace ID)
            assert len(har["log"]["_span_id"]) == 16
            
            # The first part of trace ID should match span ID
            assert har["log"]["_trace_id"][:16] == har["log"]["_span_id"]
            
            # The first page should have parent_id set to root span
            page = har["log"]["pages"][0]
            assert "_parent_id" in page
            assert page["_parent_id"] == har["log"]["_span_id"]

    def test_har_page_tracing_properties(self, hc):
        """Test that HAR pages have correct trace context properties."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset to ensure clean state
            hc.reset_har_and_return_old_har()
            
            # Get the initial page and record IDs
            har = hc.har
            root_span_id = har["log"]["_span_id"]
            
            # Initial page properties
            page = har["log"]["pages"][0]
            assert "_span_id" in page
            assert len(page["_span_id"]) == 16
            assert page["_parent_id"] == root_span_id
            
            # Create a new page
            hc.new_page()
            
            # New page should also link to root span
            new_page = har["log"]["pages"][1]
            assert "_span_id" in new_page
            assert len(new_page["_span_id"]) == 16
            assert new_page["_parent_id"] == root_span_id
            assert new_page["_span_id"] != page["_span_id"]  # Different span IDs

    def test_har_entry_tracing_properties(self, hc):
        """Test that HAR entries have correct trace context properties and parent relationships."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset to ensure clean state
            hc.reset_har_and_return_old_har()
            
            # Get the HAR and record root trace details
            har = hc.har
            root_trace_id = har["log"]["_trace_id"]
            
            # Create a flow/entry and verify its trace context
            f = self.flow()
            hc.request(f)
            
            # Entry should have trace context
            entry = har["log"]["entries"][0]
            assert "_trace_id" in entry
            assert "_span_id" in entry
            assert "_parent_id" in entry
            
            # Entry should have same trace ID as root
            assert entry["_trace_id"] == root_trace_id
            
            # Entry's parent should be the page's span ID
            page = har["log"]["pages"][0]
            assert entry["_parent_id"] == page["_span_id"]
            
            # Create a new page and entry
            hc.new_page()
            f2 = self.flow()
            hc.request(f2)
            
            # New entry should link to new page
            new_page = har["log"]["pages"][1]
            new_entry = har["log"]["entries"][1]
            
            assert new_entry["_parent_id"] == new_page["_span_id"]
            
            # Entry should still share the same trace ID
            assert new_entry["_trace_id"] == root_trace_id
            
    def test_browser_root_entry_parent_child_relationship(self, hc):
        """Test that browser root entries correctly establish parent-child relationships."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset to ensure clean state
            hc.reset_har_and_return_old_har()
            
            # Create a browser-like main HTML request
            f_html = self.flow()
            f_html.request.headers["User-Agent"] = "Mozilla/5.0 Chrome/91.0"
            f_html.response.headers["Content-Type"] = "text/html"
            
            # Process request and response
            hc.request(f_html)
            hc.response(f_html)
            
            # This should be identified as a browser root
            entry_html = hc.har["log"]["entries"][0]
            assert entry_html.get("_browser_root") is True
            
            # Parent should be the page span
            page = hc.har["log"]["pages"][0]
            assert entry_html["_parent_id"] == page["_span_id"]
            
            # Create a subsequent resource request on the same page
            f_js = self.flow()
            f_js.request.headers["User-Agent"] = "Mozilla/5.0 Chrome/91.0"
            f_js.response.headers["Content-Type"] = "application/javascript"
            
            # Process request and response
            hc.request(f_js)
            hc.response(f_js)
            
            # This resource entry should have the HTML entry as parent
            entry_js = hc.har["log"]["entries"][1]
            assert not entry_js.get("_browser_root")
            assert entry_js["_parent_id"] == entry_html["_span_id"]
            
            # Create a new page
            hc.new_page()
            
            # Create a new HTML request for the new page
            f_html2 = self.flow()
            f_html2.request.headers["User-Agent"] = "Mozilla/5.0 Chrome/91.0"
            f_html2.response.headers["Content-Type"] = "text/html"
            
            # Process request and response
            hc.request(f_html2)
            hc.response(f_html2)
            
            # This should be a new browser root
            entry_html2 = hc.har["log"]["entries"][2]
            assert entry_html2.get("_browser_root") is True
            
            # Its parent should be the new page
            new_page = hc.har["log"]["pages"][1]
            assert entry_html2["_parent_id"] == new_page["_span_id"]
            
            # Add a resource to the new page
            f_img = self.flow()
            f_img.request.headers["User-Agent"] = "Mozilla/5.0 Chrome/91.0"
            f_img.response.headers["Content-Type"] = "image/jpeg"
            
            # Process request and response
            hc.request(f_img)
            hc.response(f_img)
            
            # This resource should have the second HTML entry as parent
            entry_img = hc.har["log"]["entries"][3]
            assert entry_img["_parent_id"] == entry_html2["_span_id"]
            
    def test_har_reset_changes_trace_ids(self, hc):
        """Test that reset_har generates new trace and span IDs while maintaining zero parent_id."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Get initial IDs
            initial_trace_id = hc.har["log"]["_trace_id"]
            initial_span_id = hc.har["log"]["_span_id"]
            
            # Parent ID should be zeros
            assert hc.har["log"]["_parent_id"] == "0000000000000000"
            
            # Reset the HAR
            old_har = hc.reset_har_and_return_old_har()
            
            # Verify the old_har has the initial IDs
            assert old_har["log"]["_trace_id"] == initial_trace_id
            assert old_har["log"]["_span_id"] == initial_span_id
            assert old_har["log"]["_parent_id"] == "0000000000000000"
            
            # Get new IDs
            new_trace_id = hc.har["log"]["_trace_id"] 
            new_span_id = hc.har["log"]["_span_id"]
            
            # New IDs should be different from initial IDs
            assert new_trace_id != initial_trace_id
            assert new_span_id != initial_span_id
            
            # New parent ID should still be zeros
            assert hc.har["log"]["_parent_id"] == "0000000000000000"
            
            # The first page should have the new root span as parent
            page = hc.har["log"]["pages"][0]
            assert page["_parent_id"] == new_span_id
            
    def test_page_reset_preserves_trace_structure(self, hc):
        """Test that adding a new page maintains trace relationships but creates new span IDs."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset to ensure clean state
            hc.reset_har_and_return_old_har()
            
            # Get root trace info
            root_trace_id = hc.har["log"]["_trace_id"]
            root_span_id = hc.har["log"]["_span_id"]
            
            # Initial page should link to root
            initial_page = hc.har["log"]["pages"][0]
            initial_page_span_id = initial_page["_span_id"]
            assert initial_page["_parent_id"] == root_span_id
            
            # Create a flow for the first page
            f1 = self.flow()
            hc.request(f1)
            
            # Entry should link to page
            entry1 = hc.har["log"]["entries"][0]
            assert entry1["_parent_id"] == initial_page_span_id
            assert entry1["_trace_id"] == root_trace_id
            
            # Create a new page
            hc.new_page()
            
            # Get new page
            new_page = hc.har["log"]["pages"][1]
            new_page_span_id = new_page["_span_id"]
            
            # New page should have a different span ID
            assert new_page_span_id != initial_page_span_id
            
            # New page should still link to the root
            assert new_page["_parent_id"] == root_span_id
            
            # Create a flow for the new page
            f2 = self.flow()
            hc.request(f2)
            
            # New entry should link to the new page
            entry2 = hc.har["log"]["entries"][1]
            assert entry2["_parent_id"] == new_page_span_id
            
            # Entry should share the same trace ID
            assert entry2["_trace_id"] == root_trace_id
            
    def test_trace_preservation_after_multiple_resets(self, hc):
        """Test that trace relationships are correctly preserved after multiple HAR and page resets."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Cycle 1: Initial state
            root_trace_id_1 = hc.har["log"]["_trace_id"]
            root_span_id_1 = hc.har["log"]["_span_id"]
            assert hc.har["log"]["_parent_id"] == "0000000000000000"
            
            # Add a page and an entry
            f1 = self.flow()
            hc.request(f1)
            
            # First entry links to first page
            page1 = hc.har["log"]["pages"][0]
            entry1 = hc.har["log"]["entries"][0]
            assert page1["_parent_id"] == root_span_id_1
            assert entry1["_parent_id"] == page1["_span_id"]
            
            # Reset the HAR
            hc.reset_har_and_return_old_har()
            
            # Cycle 2: After HAR reset
            root_trace_id_2 = hc.har["log"]["_trace_id"]
            root_span_id_2 = hc.har["log"]["_span_id"]
            assert root_trace_id_2 != root_trace_id_1
            assert root_span_id_2 != root_span_id_1
            assert hc.har["log"]["_parent_id"] == "0000000000000000"
            
            # Add a page and entry after reset
            f2 = self.flow()
            hc.request(f2)
            
            # New entry links to new page
            page2 = hc.har["log"]["pages"][0]
            entry2 = hc.har["log"]["entries"][0]
            assert page2["_parent_id"] == root_span_id_2
            assert entry2["_parent_id"] == page2["_span_id"]
            
            # Add a new page
            hc.new_page()
            
            # Add entry to second page
            f3 = self.flow()
            hc.request(f3)
            
            # Entry links to the new page
            page3 = hc.har["log"]["pages"][1]
            entry3 = hc.har["log"]["entries"][1]
            assert page3["_parent_id"] == root_span_id_2
            assert entry3["_parent_id"] == page3["_span_id"]
            
            # Reset the HAR again
            hc.reset_har_and_return_old_har()
            
            # Cycle 3: After second HAR reset
            root_trace_id_3 = hc.har["log"]["_trace_id"]
            root_span_id_3 = hc.har["log"]["_span_id"]
            assert root_trace_id_3 != root_trace_id_2
            assert root_span_id_3 != root_span_id_2
            assert hc.har["log"]["_parent_id"] == "0000000000000000"
            
            # First page links to the root
            page4 = hc.har["log"]["pages"][0]
            assert page4["_parent_id"] == root_span_id_3


@pytest.fixture()
def hc():
    a = har_capture_addon.HarCaptureAddOn()
    with taddons.context(a) as ctx:
        ctx.configure(a, trace_enabled=True)
    return a