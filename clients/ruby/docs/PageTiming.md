# BrowserupMitmProxy::PageTiming

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **on_content_load** | **Integer** | onContentLoad per the browser | [optional] |
| **on_load** | **Integer** | onLoad per the browser | [optional] |
| **_first_input_delay** | **Integer** | firstInputDelay from the browser | [optional] |
| **_first_paint** | **Integer** | firstPaint from the browser | [optional] |
| **_cumulative_layout_shift** | **Integer** | cumulativeLayoutShift metric from the browser | [optional] |
| **_largest_contentful_paint** | **Integer** | largestContentfulPaint from the browser | [optional] |
| **_dom_interactive** | **Integer** | domInteractive from the browser | [optional] |
| **_first_contentful_paint** | **Integer** | firstContentfulPaint from the browser | [optional] |
| **_dns** | **Integer** | dns lookup time from the browser | [optional] |
| **_ssl** | **Integer** | Ssl connect time from the browser | [optional] |
| **_time_to_first_byte** | **Integer** | Time to first byte of the page&#39;s first request per the browser | [optional] |
| **_href** | **String** | Top level href, including hashtag, etc per the browser | [optional] |
| **_span_id** | **String** | W3C Trace Context span ID for this page | [optional] |
| **_parent_id** | **String** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] |

## Example

```ruby
require 'browserup_mitmproxy_client'

instance = BrowserupMitmProxy::PageTiming.new(
  on_content_load: null,
  on_load: null,
  _first_input_delay: null,
  _first_paint: null,
  _cumulative_layout_shift: null,
  _largest_contentful_paint: null,
  _dom_interactive: null,
  _first_contentful_paint: null,
  _dns: null,
  _ssl: null,
  _time_to_first_byte: null,
  _href: null,
  _span_id: null,
  _parent_id: null
)
```

