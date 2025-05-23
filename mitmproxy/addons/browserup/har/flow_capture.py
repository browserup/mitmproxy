import base64
import logging
import typing
from datetime import datetime
from datetime import timezone

from mitmproxy import connection
from mitmproxy.addons.browserup.har.har_builder import HarBuilder
from mitmproxy.addons.browserup.har.har_capture_types import HarCaptureTypes
from mitmproxy.utils import strutils

# all the specifics to do with converting a flow into a HAR
# A list of server seen till now is maintained so we can avoid
# using 'connect' time for entries that use an existing connection.
SERVERS_SEEN: typing.Set[connection.Server] = set()

REQUEST_SUBMITTED_FLAG = "_submitted"

STATIC_MIME_TYPES = {
    "application/javascript",
    "application/pdf",
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/svg+xml",
    "image/webp",
    "image/bmp",
    "image/tiff",
    "audio/mpeg",
    "audio/wav",
    "audio/ogg",
    "video/mp4",
    "video/webm",
    "video/ogg",
    "video/quicktime",
    "font/woff",
    "font/woff2",
    "font/ttf",
    "image/x-icon",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-tar",
    "application/x-7z-compressed",
    "application/octet-stream",
    "application/x-shockwave-flash",
    "text/css",
}


class FlowCaptureMixin(object):
    def is_browser_user_agent(self, user_agent):
        """Check if User-Agent looks like a browser based on the specified regex pattern"""
        if not user_agent:
            return False

        import re

        pattern = re.compile(
            r"Mozilla|Chrome|Firefox|Safari|Edge|Gecko|WebKit|Ladybird|Lightpanda",
            re.IGNORECASE,
        )
        return bool(pattern.search(user_agent))

    def is_first_request_in_page(self, flow):
        """Check if this is the first request for the current page"""
        page = self.get_or_create_current_page()
        page_entries = self.entries_for_page(page["id"])

        # This could be the first request for this page
        is_first = len(page_entries) == 0 or (
            len(page_entries) == 1
            and page_entries[0]["request"]["url"] == self.get_full_url(flow.request)
        )

        return is_first

    def is_html_content_type(self, flow):
        """Check if response content type is HTML"""
        content_type = (
            flow.response.headers.get("Content-Type", "") if flow.response else ""
        )
        return "text/html" in content_type.lower()

    def decorate_request_with_trace_headers(self, flow):
        """Add or update W3C trace context headers for distributed tracing"""
        har_entry = flow.get_har_entry()

        # Get the IDs from HAR entry
        trace_id = har_entry.get("_trace_id")
        span_id = har_entry.get("_span_id")

        # Skip if we don't have proper IDs
        if not trace_id or not span_id:
            logging.debug("No trace info available for request")
            return

        # Check if this is the first request in a page and has a browser user-agent
        if self.is_first_request_in_page(flow):
            user_agent = flow.request.headers.get("User-Agent", "")
            is_browser = self.is_browser_user_agent(user_agent)

            if is_browser:
                # Mark as potential browser root - will be confirmed when response comes in
                har_entry["_potential_browser_root"] = True
                logging.debug(
                    f"Potential browser root request detected: {flow.request.url}"
                )

        # Check if traceparent header already exists
        existing_traceparent = flow.request.headers.get("traceparent")
        if existing_traceparent:
            # Parse the existing traceparent header
            parts = existing_traceparent.split("-")
            if len(parts) == 4:
                # Extract trace ID and flags from the existing header
                existing_trace_id = parts[1]
                trace_flags = parts[3]

                # Update the HAR entry with the existing trace ID
                har_entry["_trace_id"] = existing_trace_id

                # Use the existing trace ID, but with the HAR entry's span ID
                traceparent = f"{parts[0]}-{existing_trace_id}-{span_id}-{trace_flags}"
                flow.request.headers["traceparent"] = traceparent
                logging.debug(f"Updated existing traceparent header: {traceparent}")
            else:
                # Invalid format, create a new traceparent
                traceparent = f"00-{trace_id}-{span_id}-01"
                flow.request.headers["traceparent"] = traceparent
                logging.debug(f"Replaced invalid traceparent header: {traceparent}")
        else:
            # No existing header, create a new one
            # Format: version-traceid-spanid-traceflags
            # Using version 00 and traceflags 01 (sampled)
            traceparent = f"00-{trace_id}-{span_id}-01"
            flow.request.headers["traceparent"] = traceparent
            logging.debug(f"Added traceparent header: {traceparent}")

        # Handle tracestate according to W3C spec
        # The spec says new vendors should add their entry to the left of any existing entries
        vendor_name = "browserup"

        # Get existing tracestate
        existing_tracestate = flow.request.headers.get("tracestate", "")

        # Add our entry to tracestate
        # Use span_id as our vendor-specific value
        new_entry = f"{vendor_name}={span_id}"

        if existing_tracestate:
            # Parse existing entries, remove our vendor if it exists already
            entries = [entry.strip() for entry in existing_tracestate.split(",")]
            entries = [
                entry for entry in entries if not entry.startswith(f"{vendor_name}=")
            ]

            # Add our entry to the left (at the beginning)
            entries.insert(0, new_entry)

            # Join with commas and update the header
            # Limit to 32 entries per spec (the newest 32)
            updated_tracestate = ",".join(entries[:32])
            flow.request.headers["tracestate"] = updated_tracestate
            logging.debug(f"Updated tracestate header: {updated_tracestate}")
        else:
            # No existing tracestate, just add ours
            flow.request.headers["tracestate"] = new_entry
            logging.debug(f"Added tracestate header: {new_entry}")

    def capture_request(self, flow):
        full_url = self.get_full_url(flow.request)
        if "BrowserUpData" in full_url or "detectportal.firefox.com" in full_url:
            logging.info("Ignored, capturing nothing.")
            return

        logging.info("Populating har entry for request: {}".format(full_url))

        # First get the HAR entry - this creates it with the trace info
        har_entry = flow.get_har_entry()

        har_entry["startedDateTime"] = datetime.fromtimestamp(
            flow.request.timestamp_start, timezone.utc
        ).isoformat()

        logging.info(
            "Har startedDateTime for request: {} is {}".format(
                full_url, har_entry["startedDateTime"]
            )
        )

        har_request = HarBuilder.entry_request()
        har_request["method"] = flow.request.method
        har_request["url"] = full_url
        har_request["httpVersion"] = flow.request.http_version
        har_request["queryString"] = self.name_value(flow.request.query or {})
        har_request["headersSize"] = len(str(flow.request.headers))

        har_request["_updated"] = datetime.fromtimestamp(
            flow.request.timestamp_start, timezone.utc
        ).isoformat()

        har_entry["request"] = har_request
        req_url = "none"
        if flow.request is not None:
            req_url = flow.request.url

        logging.info("Incoming request, url: {}".format(req_url))

        if HarCaptureTypes.REQUEST_COOKIES in self.har_capture_types:
            har_entry["request"]["cookies"] = self.format_request_cookies(
                flow.request.cookies.fields
            )

        if HarCaptureTypes.REQUEST_HEADERS in self.har_capture_types:
            har_entry["request"]["headers"] = self.name_value(flow.request.headers)

        if HarCaptureTypes.REQUEST_CONTENT in self.har_capture_types:
            params = [
                {"name": a, "value": b}
                for a, b in flow.request.urlencoded_form.items(multi=True)
            ]
            har_entry["request"]["postData"] = {
                "mimeType": flow.request.headers.get("Content-Type", ""),
                "text": flow.request.get_text(strict=False),
                "params": params,
            }

        har_entry["request"]["bodySize"] = (
            len(flow.request.raw_content) if flow.request.raw_content else 0
        )
        flow.set_har_entry(har_entry)

    def capture_response(self, flow):
        full_url = self.get_full_url(flow.request)

        if "BrowserUpData" in full_url or "detectportal.firefox.com" in full_url:
            logging.info(
                "BrowserUpData response or ignored response, capturing nothing."
            )
            return

        logging.debug("Incoming response for request to url: {}".format(full_url))

        t = HarBuilder.entry_timings()
        t["send"] = self.diff_millis(
            flow.request.timestamp_end, flow.request.timestamp_start
        )
        t["wait"] = self.diff_millis(
            flow.response.timestamp_start, flow.request.timestamp_end
        )
        t["receive"] = self.diff_millis(
            flow.response.timestamp_end, flow.response.timestamp_start
        )

        if flow.server_conn and flow.server_conn not in SERVERS_SEEN:
            t["connect"] = self.diff_millis(
                flow.server_conn.timestamp_tcp_setup, flow.server_conn.timestamp_start
            )

            if flow.server_conn.timestamp_tls_setup is not None:
                t["ssl"] = self.diff_millis(
                    flow.server_conn.timestamp_tls_setup,
                    flow.server_conn.timestamp_tcp_setup,
                )

            SERVERS_SEEN.add(flow.server_conn)

        full_time = sum(v for v in t.values() if v > -1)

        har_entry = flow.get_har_entry()
        har_entry["timings"] = t

        # Response body size and encoding
        response_body_size = (
            len(flow.response.raw_content) if flow.response.raw_content else 0
        )
        response_body_decoded_size = (
            len(flow.response.content) if flow.response.content else 0
        )
        response_body_compression = response_body_decoded_size - response_body_size

        if flow.metadata.get("injected_script_len") and response_body_size > 0:
            logging.debug(
                f"Subtracting injected script length of {flow.metadata.get('injected_script_len')}"
            )
            response_body_size = response_body_size - flow.metadata.get(
                "injected_script_len"
            )

        har_response = HarBuilder.entry_response()
        har_response["status"] = flow.response.status_code
        har_response["statusText"] = flow.response.reason
        har_response["httpVersion"] = flow.response.http_version

        if HarCaptureTypes.RESPONSE_COOKIES in self.har_capture_types:
            har_response["cookies"] = self.format_response_cookies(
                flow.response.cookies.fields
            )

        if HarCaptureTypes.RESPONSE_HEADERS in self.har_capture_types:
            har_response["headers"] = self.name_value(flow.response.headers)

        if flow.response.status_code in [300, 301, 302, 303, 307]:
            har_response["redirectURL"] = flow.response.headers["Location"]

        content = har_response["content"]
        content["size"] = response_body_size
        content["compression"] = response_body_compression
        content["mimeType"] = flow.response.headers.get("Content-Type", "")

        # Check if this is a confirmed browser-based HTML response
        content_type = flow.response.headers.get("Content-Type", "").lower()
        is_html = "text/html" in content_type

        # If this was marked as a potential browser root request and it's HTML,
        # confirm it as a browser root for parent/child relationships
        if har_entry.get("_potential_browser_root") and is_html:
            har_entry["_browser_root"] = True
            har_entry.pop("_potential_browser_root", None)
            logging.info(f"Confirmed browser root request: {flow.request.url}")

            # Set parent to page span id since this is main HTML request
            page = self.get_or_create_current_page()
            har_entry["_parent_id"] = page["_span_id"]
        elif not har_entry.get("_browser_root"):
            # For non-root requests, check if there's a browser root in this page to set as parent
            page = self.get_or_create_current_page()
            page_entries = self.entries_for_page(page["id"])

            for entry in page_entries:
                if (
                    entry.get("_browser_root")
                    and entry["_span_id"] != har_entry["_span_id"]
                ):
                    # Set parent to browser root span instead of page span
                    har_entry["_parent_id"] = entry["_span_id"]
                    logging.debug(f"Set parent of {flow.request.url} to browser root")
                    break

        if HarCaptureTypes.RESPONSE_DYNAMIC_CONTENT in self.har_capture_types:
            mime_type = (
                flow.response.headers.get("Content-Type", "").split(";")[0].strip()
            )
            # Skip capturing if mime_type is in the types to ignore
            if mime_type not in STATIC_MIME_TYPES:
                if strutils.is_mostly_bin(flow.response.content):
                    har_response["content"]["text"] = base64.b64encode(
                        flow.response.content
                    ).decode()
                    har_response["content"]["encoding"] = "base64"
                else:
                    har_response["content"]["text"] = flow.response.get_text(
                        strict=False
                    )

        if HarCaptureTypes.RESPONSE_CONTENT in self.har_capture_types:
            if strutils.is_mostly_bin(flow.response.content):
                if HarCaptureTypes.RESPONSE_BINARY_CONTENT in self.har_capture_types:
                    har_response["content"]["text"] = base64.b64encode(
                        flow.response.content
                    ).decode()
                    har_response["content"]["encoding"] = "base64"
            else:
                har_response["content"]["text"] = flow.response.get_text(strict=False)

        har_response["redirectURL"] = flow.response.headers.get("Location", "")
        har_response["headersSize"] = len(str(flow.response.headers))
        har_response["bodySize"] = response_body_size

        har_entry["response"] = har_response
        har_entry["time"] = full_time
        har_entry["pageref"] = self.get_current_page_ref()

        har_entry["timings"] = t

        if flow.server_conn.connected:
            har_entry["serverIPAddress"] = str(flow.server_conn.ip_address[0])

        flow.set_har_entry(har_entry)

    def capture_websocket_message(self, flow):
        full_url = self.get_full_url(flow.request)
        if "BrowserUpData" in full_url or "devtools" in full_url:
            logging.info("BrowserUpData websocket, capturing nothing.")
        else:
            logging.info("Capturing WS data.")
            if HarCaptureTypes.WEBSOCKET_MESSAGES in self.har_capture_types:
                har_entry = flow.get_har_entry()
                msg = flow.websocket.messages[-1]
                data = msg.content
                try:
                    data = data.decode("utf-8")
                except (UnicodeDecodeError, AttributeError):
                    pass

                msg = {
                    "type": "send" if msg.from_client else "receive",
                    "opcode": msg.type.value,
                    "data": data,
                    "time": msg.timestamp,
                }

                msgs = har_entry.get("_webSocketMessages", [])
                msgs.append(msg)
                har_entry["_webSocketMessages"] = msgs
                flow.set_har_entry(har_entry)

    # for all of these:  Use -1 if the timing does not apply to the current request.
    # Time required to create TCP connection.

    # question: how to make the server connect time stop reporting once it has happened.
    #
    # connection id seems like it is unique. We can choose to only report it once.
    # we could also put it on the page object.

    def get_full_url(self, request):
        host_port = request.pretty_host
        if request.method == "CONNECT":
            if request.port != 443:
                host_port = host_port + ":" + str(request.port)
            host_port = "https://" + host_port
        else:
            if request.scheme is not None:
                host_port = request.pretty_url
            else:
                host_port = host_port + ":" + str(request.port)

        return host_port

    def diff_millis(self, ts_end, ts_start):
        if ts_end is None or ts_start is None:
            return -1
        else:
            return round((ts_end - ts_start) * 1000)
