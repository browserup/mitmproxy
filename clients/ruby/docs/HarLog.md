# BrowserupMitmProxy::HarLog

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  |  |
| **creator** | [**HarLogCreator**](HarLogCreator.md) |  |  |
| **browser** | [**HarLogCreator**](HarLogCreator.md) |  | [optional] |
| **pages** | [**Array&lt;Page&gt;**](Page.md) |  |  |
| **entries** | [**Array&lt;HarEntry&gt;**](HarEntry.md) |  |  |
| **_trace_id** | **String** | W3C Trace Context trace ID for distributed tracing | [optional] |
| **_span_id** | **String** | W3C Trace Context span ID for this HAR trace root | [optional] |
| **comment** | **String** |  | [optional] |

## Example

```ruby
require 'browserup_mitmproxy_client'

instance = BrowserupMitmProxy::HarLog.new(
  version: null,
  creator: null,
  browser: null,
  pages: null,
  entries: null,
  _trace_id: null,
  _span_id: null,
  comment: null
)
```

