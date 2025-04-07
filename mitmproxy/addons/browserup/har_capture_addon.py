import logging

import mitmproxy.http
from mitmproxy import ctx
from mitmproxy.addons.browserup.har import flow_har_entry_patch
from mitmproxy.addons.browserup.har.flow_capture import FlowCaptureMixin
from mitmproxy.addons.browserup.har.har_manager import HarManagerMixin
from mitmproxy.addons.browserup.har.har_resources import ErrorResource
from mitmproxy.addons.browserup.har.har_resources import HarCaptureTypesResource
from mitmproxy.addons.browserup.har.har_resources import HarPageResource
from mitmproxy.addons.browserup.har.har_resources import HarResource
from mitmproxy.addons.browserup.har.har_resources import HealthCheckResource
from mitmproxy.addons.browserup.har.har_resources import MetricResource
from mitmproxy.addons.browserup.har.har_resources import NotPresentResource
from mitmproxy.addons.browserup.har.har_resources import PresentResource
from mitmproxy.addons.browserup.har.har_resources import SizeResource
from mitmproxy.addons.browserup.har.har_resources import SLAResource

flow_har_entry_patch.patch_flow()  # patch flow object with a har entry method


class HarCaptureAddOn(FlowCaptureMixin, HarManagerMixin):
    def load(self, loader):
        logging.info("Loading HarCaptureAddon")
        loader.add_option("harcapture", str, "", "HAR capture path.")
        loader.add_option(
            "trace_enabled", bool, True, "Enable W3C distributed tracing headers"
        )

    # Resources are used to define items available over the API.
    def get_resources(self):
        return [
            HarResource(self),
            HarPageResource(self),
            HarCaptureTypesResource(self),
            PresentResource(self),
            NotPresentResource(self),
            SizeResource(self),
            SLAResource(self),
            ErrorResource(self),
            MetricResource(self),
            HealthCheckResource(),
        ]

    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        if "blocklisted" in flow.metadata:
            return
        self.capture_websocket_message(flow)

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "blocklisted" in flow.metadata:
            return

        # First create the HAR entry with trace information
        self.capture_request(flow)

        # Then decorate the request with trace headers if enabled
        if hasattr(ctx.options, "trace_enabled") and ctx.options.trace_enabled:
            self.decorate_request_with_trace_headers(flow)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "blocklisted" in flow.metadata:
            logging.debug("Blocklist filtered, return nothing.")
            return
        self.capture_response(flow)


addons = [HarCaptureAddOn()]
