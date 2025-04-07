# BrowserupMitmProxy::Page

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **started_date_time** | **Time** |  |  |
| **id** | **String** |  |  |
| **title** | **String** |  |  |
| **_verifications** | [**Array&lt;VerifyResult&gt;**](VerifyResult.md) |  | [optional] |
| **_metrics** | [**Array&lt;Metric&gt;**](Metric.md) |  | [optional] |
| **_errors** | [**Array&lt;Error&gt;**](Error.md) |  | [optional] |
| **_span_id** | **String** | W3C Trace Context span ID for this page | [optional] |
| **_parent_id** | **String** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] |
| **page_timings** | [**PageTimings**](PageTimings.md) |  |  |
| **comment** | **String** |  | [optional] |

## Example

```ruby
require 'browserup_mitmproxy_client'

instance = BrowserupMitmProxy::Page.new(
  started_date_time: null,
  id: null,
  title: null,
  _verifications: null,
  _metrics: null,
  _errors: null,
  _span_id: null,
  _parent_id: null,
  page_timings: null,
  comment: null
)
```

