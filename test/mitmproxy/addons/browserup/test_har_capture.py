import json
import os
import tempfile

import pytest
from wsproto.frame_protocol import Opcode

from mitmproxy import http
from mitmproxy import websocket
from mitmproxy.addons.browserup import har_capture_addon
from mitmproxy.addons.browserup.har.har_capture_types import HarCaptureTypes
from mitmproxy.net.http import cookies
from mitmproxy.test import taddons
from mitmproxy.test import tflow
from mitmproxy.test import tutils
from mitmproxy.test.tflow import twebsocketflow
from mitmproxy.utils import data


class TestHARCapture:
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

    def tvideoflow(self):
        # Create a request object
        req = http.Request.make(
            "GET",
            "http://example.com/video.mp4",
            headers={"Host": "example.com", "User-Agent": "TestAgent"},
        )

        # Create a response object
        resp = http.Response.make(
            200,  # status code
            b"video binary data here",  # video content (truncated for example)
            {
                "Content-Type": "video/mp4",
                "Content-Length": "1234567",  # replace with actual content length
            },
        )
        flow = tflow.tflow(req=req, resp=resp)
        return flow

    def test_capture_dynamic_response_content(self, hc):
        # Test dynamic content (HTML)
        f_dynamic = self.flow()
        f_dynamic.response.headers["Content-Type"] = "text/html"
        f_dynamic.response.content = b"<html><body>Hello World</body></html>"
        hc.har_capture_types = [HarCaptureTypes.RESPONSE_DYNAMIC_CONTENT]
        hc.response(f_dynamic)
        assert (
            hc.har["log"]["entries"][0]["response"]["content"]["text"]
            == "<html><body>Hello World</body></html>"
        )

        # Clear entries for the next test
        hc.har["log"]["entries"].clear()

        # Test non-dynamic content (Video)
        f_video = self.tvideoflow()
        hc.response(f_video)
        assert hc.har["log"]["entries"][0]["response"]["content"]["text"] == ""

    def test_simple(self, hc, path):
        # is invoked if there are exceptions
        # check script is read without errors
        with taddons.context(hc):
            hc.response(self.flow())

        with tempfile.TemporaryDirectory() as tmpdirname:
            print("Created temporary directory:", tmpdirname)
            file_path = os.path.join(tmpdirname, "testbase64.har")
            hc.save_current_har_to_path(file_path)
            with open(file_path) as inp:
                har = json.load(inp)
            assert len(har["log"]["entries"]) == 1

    def test_base64(self, hc):
        hc.har_capture_types = [
            HarCaptureTypes.RESPONSE_BINARY_CONTENT,
            HarCaptureTypes.RESPONSE_CONTENT,
        ]

        hc.response(self.flow(resp_content=b"foo" + b"\xff" * 10))
        with tempfile.TemporaryDirectory() as tmpdirname:
            print("Created temporary directory:", tmpdirname)
            file_path = os.path.join(tmpdirname, "testbase64.har")
            hc.save_current_har_to_path(file_path)
            with open(file_path) as inp:
                har = json.load(inp)
                assert (
                    har["log"]["entries"][0]["response"]["content"]["encoding"]
                    == "base64"
                )

    def test_format_cookies(self, hc):
        CA = cookies.CookieAttrs

        f = hc.format_cookies([("n", "v", CA([("k", "v")]))])[0]
        assert f["name"] == "n"
        assert f["value"] == "v"
        assert not f["httpOnly"]
        assert not f["secure"]

        f = hc.format_cookies([("n", "v", CA([("httponly", None), ("secure", None)]))])[
            0
        ]
        assert f["httpOnly"]
        assert f["secure"]

        f = hc.format_cookies(
            [("n", "v", CA([("expires", "Mon, 24-Aug-2037 00:00:00 GMT")]))]
        )[0]
        assert f["expires"]

    def test_binary(self, hc, path):
        f = self.flow()
        f.request.method = "POST"
        f.request.headers["content-type"] = "application/x-www-form-urlencoded"
        f.request.content = b"foo=bar&baz=s%c3%bc%c3%9f"
        f.response.headers["random-junk"] = bytes(range(256))
        f.response.content = bytes(range(256))

        hc.response(f)
        with tempfile.TemporaryDirectory() as tmpdirname:
            file_path = os.path.join(tmpdirname, "testbase64.har")
            hc.save_current_har_to_path(file_path)
            with open(file_path) as inp:
                har = json.load(inp)
                assert len(har["log"]["entries"]) == 1

    def test_capture_cookies_on(self, hc):
        f = self.flow()
        f.request.headers["cookie"] = "foo=bar"
        hc.har_capture_types = [
            HarCaptureTypes.REQUEST_COOKIES,
            HarCaptureTypes.REQUEST_CAPTURE_TYPES.REQUEST_CONTENT,
        ]
        hc.request(f)
        assert hc.har["log"]["entries"][0]["request"]["cookies"][0]["name"] == "foo"
        assert hc.har["log"]["entries"][0]["request"]["cookies"][0]["value"] == "bar"

    def test_capture_cookies_off(self, hc):
        f = self.flow()
        f.request.headers["cookie"] = "foo=bar"
        hc.har_capture_types = [HarCaptureTypes.REQUEST_CAPTURE_TYPES.REQUEST_CONTENT]
        hc.request(f)
        assert hc.har["log"]["entries"][0]["request"]["cookies"] == []

    def test_capture_request_headers_on(self, hc):
        f = self.flow()
        f.request.headers["boo"] = "baz"
        hc.har_capture_types = [HarCaptureTypes.REQUEST_CAPTURE_TYPES.REQUEST_HEADERS]
        hc.request(f)
        assert hc.har["log"]["entries"][0]["request"]["headers"][2]["name"] == "boo"

    def test_capture_request_headers_off(self, hc):
        f = self.flow()
        f.request.headers["cookie"] = "foo=bar"
        hc.har_capture_types = []
        hc.request(f)
        assert hc.har["log"]["entries"][0]["request"]["headers"] == []

    def test_capture_response_headers_on(self, hc):
        f = self.flow()
        f.response.headers["bee"] = "bazl"
        hc.har_capture_types = [HarCaptureTypes.RESPONSE_HEADERS]
        hc.response(f)
        assert hc.har["log"]["entries"][0]["response"]["headers"][2]["name"] == "bee"

    def test_capture_response_headers_off(self, hc):
        f = self.flow()
        f.response.headers["bee"] = "bazl"
        hc.har_capture_types = []
        hc.response(f)
        assert hc.har["log"]["entries"][0]["response"]["headers"] == []

    def test_websocket_messages_capture_off(self, hc):
        f = twebsocketflow()
        hc.har_capture_types = []
        hc.response(f)
        hc.websocket_message(f)

        assert len(hc.har["log"]["entries"][0]["_webSocketMessages"]) == 0

    def test_websocket_messages_capture_on(self, hc):
        f = twebsocketflow()
        hc.har_capture_types = [HarCaptureTypes.WEBSOCKET_MESSAGES]

        f.websocket.messages = [
            websocket.WebSocketMessage(Opcode.BINARY, True, b"hello binary", 946681203)
        ]
        hc.websocket_message(f)
        f.websocket.messages = [
            websocket.WebSocketMessage(Opcode.BINARY, True, b"hello binary", 946681203),
            websocket.WebSocketMessage(Opcode.TEXT, True, b"hello text", 946681204),
        ]
        hc.websocket_message(f)
        assert hc.har["log"]["entries"][0]["_webSocketMessages"]

    def test_capture_response_on(self, hc):
        f = self.flow()
        hc.har_capture_types = [HarCaptureTypes.RESPONSE_CONTENT]
        hc.response(f)
        assert hc.har["log"]["entries"][0]["response"]["content"]["text"] != ""

    def test_capture_response_off(self, hc):
        f = self.flow()
        hc.har_capture_types = []
        hc.response(f)
        assert hc.har["log"]["entries"][0]["response"]["content"]["text"] == ""

    # if har is cleared, where do existing flow har_entries point?
    def test_new_har_clears_har(self, hc):
        f = self.flow()
        hc.har_capture_types = []
        hc.response(f)
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["entries"]) == 0
        f = tflow.tflow(req=tutils.treq(method=b"GET"), resp=tutils.tresp())
        hc.request(f)
        assert len(hc.har["log"]["pages"]) == 1

    def test_blank_default_page(self, hc):
        f = self.flow()
        hc.request(f)
        assert hc.har["log"]["pages"][0]["id"] == "page_1"
        assert hc.har["log"]["pages"][0]["title"] == "Default"
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1

    def test_har_entries_timings(self, hc):
        f = self.flow()
        hc.request(f)
        assert hc.har["log"]["pages"][0]["id"] == "page_1"

    def test_reset_har_removes_pages_and_entries(self, hc):
        f = self.flow()
        hc.request(f)
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    # test reset returns old har
    def test_reset_returns_old_har(self, hc):
        f = self.flow()
        hc.request(f)
        old_har = hc.reset_har_and_return_old_har()
        assert len(old_har["log"]["pages"]) == 1
        assert len(old_har["log"]["entries"]) == 1

    def test_reset_inits_empty_first_page(self, hc):
        f = self.flow()
        hc.request(f)
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    def test_filter_submitted_entries(self, hc):
        f = self.flow()
        hc.request(f)
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    def test_clean_har(self, hc):
        f = self.flow()
        hc.request(f)
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    def test_uncleaned_video_har_entries_still_there(self, hc):
        f = self.tvideoflow()
        hc.request(f)
        hc.response(f)

        h = hc.create_filtered_har_and_track_submitted()
        assert len(h["log"]["entries"]) == 1

        assert hc.har["log"]["entries"][0]["request"]["_submitted"] is True
        assert not hc.har["log"]["entries"][0]["response"].get("_submitted")

        # test filtering
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    def test_uncleaned_websocket_har_entries_still_there(self, hc):
        f = self.flow()
        hc.request(f)

        f = twebsocketflow()
        hc.request(f)
        hc.response(f)

        f.websocket.messages = [
            websocket.WebSocketMessage(Opcode.BINARY, True, b"hello binary", 946681203)
        ]
        hc.websocket_message(f)
        f.websocket.messages = [
            websocket.WebSocketMessage(Opcode.BINARY, True, b"hello binary", 946681203),
            websocket.WebSocketMessage(Opcode.TEXT, True, b"hello text", 946681204),
        ]
        hc.websocket_message(f)

        hc.create_filtered_har_and_track_submitted()

        assert len(hc.har["log"]["entries"]) == 2
        assert hc.har["log"]["entries"][0]["request"].get("_submitted")

        assert hc.har["log"]["entries"][1]["request"].get("_submitted")
        assert not hc.har["log"]["entries"][1]["response"].get("_submitted")

        # test filtering
        hc.reset_har_and_return_old_har()
        assert len(hc.har["log"]["pages"]) == 1
        assert len(hc.har["log"]["entries"]) == 0

    def test_full_submit(self, hc):
        # combine video and websocket flows and regular flow.
        # Then call create_filtered_har_and_track_submitted(self, report_last_page = True, include_websockets = True, include_videos = True)
        # assert that there are no entries, and no pages
        f = self.flow()
        hc.request(f)
        hc.response(f)
        f = self.tvideoflow()
        hc.request(f)
        hc.response(f)

        f = twebsocketflow()
        hc.request(f)
        f = self.flow()

        filtered_result = hc.create_filtered_har_and_track_submitted(
            report_last_page=True, include_websockets=True, include_videos=True
        )

        assert len(filtered_result["log"]["entries"]) == 3

        # loop through har entries and assert that they are all submitted
        for entry in hc.har["log"]["entries"]:
            assert entry["request"].get("_submitted")
            assert entry["response"].get("_submitted")

        # loop through har pages and assert that they are all submitted
        for page in hc.har["log"]["pages"]:
            assert page.get("_submitted")

        old_har = hc.reset_har_and_return_old_har()
        assert len(old_har["log"]["entries"]) == 3

        assert len(hc.har["log"]["entries"]) == 0

        assert len(hc.har["log"]["pages"]) == 1
        assert hc.har["log"]["pages"][0]["id"] == "page_1"
        
    def test_trace_headers(self, hc):
        """Test that trace information is properly added to HAR entries and requests."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Create a flow
            f = self.flow()
            hc.request(f)
            
            # Check if trace IDs are present in the HAR entry
            entry = hc.har["log"]["entries"][0]
            assert "_trace_id" in entry
            assert "_span_id" in entry
            assert "_parent_id" in entry
            
            # Check if entry parent is the page span
            page = hc.har["log"]["pages"][0]
            assert entry["_parent_id"] == page["_span_id"]
            
            # Check if the request has the traceparent header
            assert "traceparent" in f.request.headers
            traceparent = f.request.headers["traceparent"]
            
            # Verify the format is correct: 00-traceid-spanid-01
            parts = traceparent.split("-")
            assert len(parts) == 4
            assert parts[0] == "00"  # version
            assert parts[1] == entry["_trace_id"]  # trace ID
            assert parts[2] == entry["_span_id"]   # span ID
            assert parts[3] == "01"  # flags (sampled)
            
    def test_trace_header_preservation(self, hc):
        """Test that existing traceparent headers are preserved and properly processed."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Create a flow with an existing traceparent header
            f = self.flow()
            existing_trace_id = "12345678901234567890123456789012"
            existing_parent_id = "1234567890123456"
            f.request.headers["traceparent"] = f"00-{existing_trace_id}-{existing_parent_id}-01"
            
            # Process the request
            hc.request(f)
            
            # Get the entry
            entry = hc.har["log"]["entries"][0]
            
            # The HAR entry should use the existing trace ID from the header
            assert entry["_trace_id"] == existing_trace_id
            
            # The HAR entry should have a new span ID (not the parent ID from header)
            assert entry["_span_id"] != existing_parent_id
            
            # The traceparent header should be updated with the new span ID
            traceparent = f.request.headers["traceparent"]
            parts = traceparent.split("-")
            assert parts[1] == existing_trace_id  # trace ID preserved
            assert parts[2] == entry["_span_id"]  # new span ID used
            
            # The tracestate header should be added with our vendor
            assert "tracestate" in f.request.headers
            tracestate = f.request.headers["tracestate"]
            assert tracestate.startswith("browserup=")
            assert entry["_span_id"] in tracestate
            
    def test_trace_linking(self, hc):
        """Test that trace IDs properly link through the HAR structure."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Make sure we have a fresh HAR
            hc.reset_har_and_return_old_har()
            
            # Set parent ID explicitly for first page
            hc.har["log"]["pages"][0]["_parent_id"] = hc.har["log"]["_span_id"]
            
            # Initial request creates entry
            f1 = self.flow()
            hc.request(f1)
            
            # Get trace IDs
            root_trace_id = hc.har["log"]["_trace_id"]
            root_span_id = hc.har["log"]["_span_id"]
            page_span_id = hc.har["log"]["pages"][0]["_span_id"]
            
            # Verify page links to root span
            assert hc.har["log"]["pages"][0]["_parent_id"] == root_span_id
            
            # Verify entry links to page span
            assert hc.har["log"]["entries"][0]["_parent_id"] == page_span_id
            
            # Create a new page
            hc.new_page()
            
            # The new page should link to the root span
            assert hc.har["log"]["pages"][1]["_parent_id"] == root_span_id
            
            # Add a new request to the new page
            f2 = self.flow()
            hc.request(f2)
            
            # The new entry should link to the new page span
            assert hc.har["log"]["entries"][1]["_parent_id"] == hc.har["log"]["pages"][1]["_span_id"]
            
            # All entries and pages should share the same trace ID
            assert hc.har["log"]["entries"][0]["_trace_id"] == root_trace_id
            assert hc.har["log"]["entries"][1]["_trace_id"] == root_trace_id
            
            # Reset the HAR and check that a new trace ID is created
            hc.reset_har_and_return_old_har()
            new_trace_id = hc.har["log"]["_trace_id"]
            
            # Trace ID should be different after reset
            assert new_trace_id != root_trace_id
            
    def test_tracestate_handling(self, hc):
        """Test that tracestate headers are properly handled according to W3C spec."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Create a flow with an existing tracestate header
            f = self.flow()
            f.request.headers["tracestate"] = "congo=lZWRzIHRoNjM,rojo=00f067aa0ba902b7"
            
            # Process the request
            hc.request(f)
            
            # Get the entry and its span ID
            entry = hc.har["log"]["entries"][0]
            span_id = entry["_span_id"]
            
            # The tracestate header should be updated with our vendor
            assert "tracestate" in f.request.headers
            tracestate = f.request.headers["tracestate"]
            
            # Our entry should be the leftmost
            assert tracestate.startswith(f"browserup={span_id}")
            
            # The original entries should be preserved
            assert "congo=lZWRzIHRoNjM" in tracestate
            assert "rojo=00f067aa0ba902b7" in tracestate
            
            # Create a flow with our vendor already in tracestate
            f2 = self.flow()
            f2.request.headers["tracestate"] = f"browserup=oldspanid,congo=lZWRzIHRoNjM"
            
            # Process the request
            hc.request(f2)
            
            # Get the entry and its span ID
            entry2 = hc.har["log"]["entries"][1]
            span_id2 = entry2["_span_id"]
            
            # The tracestate should be updated with our new span ID
            tracestate2 = f2.request.headers["tracestate"]
            assert tracestate2.startswith(f"browserup={span_id2}")
            
            # Old browserup entry should be removed
            assert "browserup=oldspanid" not in tracestate2
            
            # Original other vendor should be preserved
            assert "congo=lZWRzIHRoNjM" in tracestate2
            
            # Test with a very long tracestate header (more than 32 entries)
            f3 = self.flow()
            # Create a tracestate with 35 entries
            long_tracestate = ",".join([f"vendor{i}=value{i}" for i in range(35)])
            f3.request.headers["tracestate"] = long_tracestate
            
            # Process the request
            hc.request(f3)
            
            # The tracestate should be trimmed to 32 entries including our entry
            tracestate3 = f3.request.headers["tracestate"]
            entries = tracestate3.split(",")
            assert len(entries) == 32  # 32 is the max per W3C spec
            assert entries[0].startswith("browserup=")  # Our entry is first
            
    def test_w3c_trace_context_full_scenario(self, hc):
        """Test a complete W3C trace context scenario with multiple participants."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Simulate a request chain:
            # 1. Original request comes in with Congo and Rojo in tracestate
            # 2. We add browserup to tracestate
            # 3. We verify the trace is propagated correctly
                        
            # First request has existing trace context headers
            f1 = self.flow()
            original_trace_id = "0af7651916cd43dd8448eb211c80319c"
            original_parent_id = "b7ad6b7169203331"
            f1.request.headers["traceparent"] = f"00-{original_trace_id}-{original_parent_id}-01"
            f1.request.headers["tracestate"] = "congo=t61rcWkgMzE,rojo=00f067aa0ba902b7"
            
            # Process the request
            hc.request(f1)
            
            # Get the entry
            entry1 = hc.har["log"]["entries"][0]
            
            # Verify traceparent is updated correctly:
            # - Same trace ID
            # - Our span ID
            # - Same flags
            traceparent1 = f1.request.headers["traceparent"]
            parts = traceparent1.split("-")
            assert parts[0] == "00"  # version
            assert parts[1] == original_trace_id  # preserved trace ID
            assert parts[2] == entry1["_span_id"]  # our span ID
            assert parts[3] == "01"  # preserved flags
            
            # Verify tracestate is updated correctly:
            # - We added our entry at the left
            # - Original entries are preserved
            tracestate1 = f1.request.headers["tracestate"]
            entries = tracestate1.split(",")
            assert entries[0].startswith("browserup=")  # Our entry is first
            assert entries[0].endswith(entry1["_span_id"])  # Using our span ID
            assert "congo=t61rcWkgMzE" in tracestate1  # Congo preserved
            assert "rojo=00f067aa0ba902b7" in tracestate1  # Rojo preserved
            
            # Simulate a second request from the same trace
            f2 = self.flow()
            # Use the updated traceparent from the first request
            f2.request.headers["traceparent"] = traceparent1
            # Use the updated tracestate from the first request
            f2.request.headers["tracestate"] = tracestate1
            
            # Process the request
            hc.request(f2)
            
            # Get the entry
            entry2 = hc.har["log"]["entries"][1]
            
            # Verify traceparent is updated:
            # - Same trace ID as first request
            # - New span ID for this request
            # - Same flags
            traceparent2 = f2.request.headers["traceparent"]
            parts = traceparent2.split("-")
            assert parts[1] == original_trace_id  # same trace ID throughout trace
            assert parts[2] == entry2["_span_id"]  # new span ID for this request
            assert parts[2] != entry1["_span_id"]  # different from first request
            
            # Verify tracestate is updated:
            # - Our entry is updated with new span ID
            # - Other entries are preserved
            tracestate2 = f2.request.headers["tracestate"]
            assert tracestate2.startswith(f"browserup={entry2['_span_id']}")
            assert "congo=t61rcWkgMzE" in tracestate2  # Congo still there
            assert "rojo=00f067aa0ba902b7" in tracestate2  # Rojo still there
    
    def test_page_timing_spans(self, hc):
        """Test that page timing attributes are properly associated with the page span."""
        with taddons.context(hc) as ctx:
            ctx.configure(hc, trace_enabled=True)
            
            # Reset HAR to get a clean state
            hc.reset_har_and_return_old_har()
            
            # Add page timing information
            timing_info = {
                "onContentLoad": 150,
                "onLoad": 350,
                "_firstPaint": 100,
                "_firstContentfulPaint": 120,
                "_domInteractive": 200
            }
            
            # Add the page timing data to the current page
            hc.add_page_timings_to_har(timing_info)
            
            # Get the current page
            page = hc.har["log"]["pages"][0]
            
            # Verify that the page has timing data
            assert page["pageTimings"]["onContentLoad"] == 150
            assert page["pageTimings"]["onLoad"] == 350
            assert page["pageTimings"]["_firstPaint"] == 100
            assert page["pageTimings"]["_firstContentfulPaint"] == 120
            assert page["pageTimings"]["_domInteractive"] == 200
            
            # Verify that the page has a span ID
            assert "_span_id" in page
            
            # Now add a request to this page
            f = self.flow()
            hc.request(f)
            
            # Get the entry
            entry = hc.har["log"]["entries"][0]
            
            # Verify that the entry references the page
            assert entry["pageref"] == page["id"]
            
            # Verify that the entry's parent ID is the page's span ID
            assert entry["_parent_id"] == page["_span_id"]


@pytest.fixture()
def hc(path):
    a = har_capture_addon.HarCaptureAddOn()
    with taddons.context(hc) as ctx:
        ctx.configure(a, harcapture=path)
    return a


@pytest.fixture()
def tdata():
    return data.Data(__name__)


@pytest.fixture()
def path(tmpdir):
    d = tempfile.TemporaryDirectory().name
    return os.path.join(d, "test.har")
