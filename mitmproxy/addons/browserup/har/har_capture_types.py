from enum import auto
from enum import Enum


class HarCaptureTypes(Enum):
    REQUEST_HEADERS = auto()
    REQUEST_COOKIES = auto()
    REQUEST_CONTENT = auto()
    REQUEST_BINARY_CONTENT = auto()
    RESPONSE_HEADERS = auto()
    RESPONSE_COOKIES = auto()
    RESPONSE_CONTENT = auto()
    RESPONSE_BINARY_CONTENT = auto()
    RESPONSE_DYNAMIC_CONTENT = auto()
    WEBSOCKET_MESSAGES = auto()

    REQUEST_CAPTURE_TYPES = {
        REQUEST_HEADERS,
        REQUEST_CONTENT,
        REQUEST_BINARY_CONTENT,
        REQUEST_COOKIES,
    }
    RESPONSE_CAPTURE_TYPES = {
        RESPONSE_HEADERS,
        RESPONSE_CONTENT,
        RESPONSE_DYNAMIC_CONTENT,
        RESPONSE_BINARY_CONTENT,
        RESPONSE_COOKIES,
        WEBSOCKET_MESSAGES,
    }
    HEADER_CAPTURE_TYPES = {REQUEST_HEADERS, RESPONSE_HEADERS}
    NON_BINARY_CONTENT_CAPTURE_TYPES = {
        REQUEST_CONTENT,
        RESPONSE_CONTENT,
        WEBSOCKET_MESSAGES,
    }
    BINARY_CONTENT_CAPTURE_TYPES = {REQUEST_BINARY_CONTENT, RESPONSE_BINARY_CONTENT}
    ALL_CONTENT_CAPTURE_TYPES = {
        REQUEST_CONTENT,
        RESPONSE_CONTENT,
        REQUEST_BINARY_CONTENT,
        RESPONSE_BINARY_CONTENT,
        WEBSOCKET_MESSAGES,
    }
    COOKIE_CAPTURE_TYPES = {REQUEST_COOKIES, RESPONSE_COOKIES}
