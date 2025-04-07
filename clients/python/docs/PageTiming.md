# PageTiming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_content_load** | **int** | onContentLoad per the browser | [optional] 
**on_load** | **int** | onLoad per the browser | [optional] 
**first_input_delay** | **int** | firstInputDelay from the browser | [optional] 
**first_paint** | **int** | firstPaint from the browser | [optional] 
**cumulative_layout_shift** | **int** | cumulativeLayoutShift metric from the browser | [optional] 
**largest_contentful_paint** | **int** | largestContentfulPaint from the browser | [optional] 
**dom_interactive** | **int** | domInteractive from the browser | [optional] 
**first_contentful_paint** | **int** | firstContentfulPaint from the browser | [optional] 
**dns** | **int** | dns lookup time from the browser | [optional] 
**ssl** | **int** | Ssl connect time from the browser | [optional] 
**time_to_first_byte** | **int** | Time to first byte of the page&#39;s first request per the browser | [optional] 
**href** | **str** | Top level href, including hashtag, etc per the browser | [optional] 
**span_id** | **str** | W3C Trace Context span ID for this page | [optional] 
**parent_id** | **str** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] 

## Example

```python
from BrowserUpMitmProxyClient.models.page_timing import PageTiming

# TODO update the JSON string below
json = "{}"
# create an instance of PageTiming from a JSON string
page_timing_instance = PageTiming.from_json(json)
# print the JSON string representation of the object
print(PageTiming.to_json())

# convert the object into a dict
page_timing_dict = page_timing_instance.to_dict()
# create an instance of PageTiming from a dict
page_timing_from_dict = PageTiming.from_dict(page_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


