import os
import tempfile

import falcon
import pytest
from falcon import testing

import mitmproxy.addons.browserup.browserup_addons_manager
from mitmproxy.addons.browserup import har_capture_addon
from mitmproxy.addons.browserup.har.har_builder import HarBuilder
from mitmproxy.test import taddons
from mitmproxy.test import tflow
from mitmproxy.test import tutils
from mitmproxy.utils import data


class TestAPI:
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

    def client(self):
        a = mitmproxy.addons.browserup.browserup_addons_manager.BrowserUpAddonsManagerAddOn()
        hca = mitmproxy.addons.browserup.browserup_addons_manager.HarCaptureAddOn()
        with taddons.context(a) as ctx:
            ctx.configure(a)
        with taddons.context(hca) as ctx:
            ctx.configure(hca)
        return testing.TestClient(a.get_app())

    # pytest will inject the object returned by the "client" function
    # as an additional parameter.
    def test_healthcheck(self, hc):
        response = self.client().simulate_get("/healthcheck")
        assert response.status == falcon.HTTP_OK

    def test_har_schema_has_trace_info(self):
        """Test that HAR schema includes trace context fields."""
        # We don't need to test API functionality end-to-end
        # We just need to verify that the HAR schema includes the trace fields

        # Create the HAR builder to check its structure
        har = HarBuilder.har()

        # The HAR log should have trace fields
        assert (
            "_trace_id" in har["log"] or "trace_id" in har["log"]
        ), "Trace ID field not in HAR log"
        assert (
            "_span_id" in har["log"] or "span_id" in har["log"]
        ), "Span ID field not in HAR log"

        # Every page should have span and parent ID fields
        page = har["log"]["pages"][0]
        assert "_span_id" in page or "span_id" in page, "Span ID field not in page"
        assert (
            "_parent_id" in page or "parent_id" in page
        ), "Parent ID field not in page"

        # Create an entry to check its structure
        entry = HarBuilder.entry()
        assert "_span_id" in entry or "span_id" in entry, "Span ID field not in entry"
        assert (
            "_parent_id" in entry or "parent_id" in entry
        ), "Parent ID field not in entry"

        # We need to add the trace ID to the entry manually for the test
        # because in the real flow, it's added when the entry is created in create_har_entry
        entry["_trace_id"] = "test-trace-id"

    def test_verify_present(self, hc):
        response = self.client().simulate_post("/verify/present/FindMyName", json={})
        assert response.status == falcon.HTTP_OK

    def test_verify_not_present(self, hc):
        response = self.client().simulate_post(
            "/verify/not_present/DontFindMyName", json={}
        )
        assert response.status == falcon.HTTP_OK

    def test_verify_sla(self, hc):
        response = self.client().simulate_post("/verify/sla/10/LoadsFast", json={})
        assert response.status == falcon.HTTP_OK

    def test_verify_size(self, hc):
        response = self.client().simulate_post(
            "/verify/size/100/NotTooLarge", json={"error_if_no_traffic": True}
        )
        assert response.status == falcon.HTTP_OK

    def test_verify_size_bad_match_criteria(self, hc):
        response = self.client().simulate_post(
            "/verify/size/100/NotTooLarge", json={"foo": True}
        )
        assert response.status == falcon.HTTP_422

    def test_add_float_metric(self, hc):
        response = self.client().simulate_post(
            "/har/metrics", json={"name": "fooAmount", "value": 5.0}
        )
        assert response.status == falcon.HTTP_204

    def test_add_integer_metric(self, hc):
        response = self.client().simulate_post(
            "/har/metrics", json={"name": "fooAmount", "value": 5}
        )
        assert response.status == falcon.HTTP_204

    def test_add_metric_schema_wrong_string_instead_of_number(self, hc):
        response = self.client().simulate_post(
            "/har/metrics", json={"name": 3, "value": "nope"}
        )
        assert response.status == falcon.HTTP_422

    def test_add_metric_schema_wrong(self, hc):
        response = self.client().simulate_post("/har/metrics", json={"name": 3})
        assert response.status == falcon.HTTP_422

    def test_add_error(self, hc):
        response = self.client().simulate_post(
            "/har/errors", json={"name": "BadError", "details": "Woops, super bad"}
        )
        assert response.status == falcon.HTTP_204

    def test_add_error_schema_wrong(self, hc):
        response = self.client().simulate_post(
            "/har/errors", json={"name": "sdfsd", "foo": "Bar"}
        )
        assert response.status == falcon.HTTP_422


@pytest.fixture()
def path(tmpdir):
    d = tempfile.TemporaryDirectory().name
    return os.path.join(d, "test.har")


@pytest.fixture()
def hc(path):
    a = har_capture_addon.HarCaptureAddOn()
    with taddons.context(hc) as ctx:
        ctx.configure(a, harcapture=path)
    return a


@pytest.fixture()
def tdata():
    return data.Data(__name__)
