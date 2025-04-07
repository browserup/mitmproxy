# HarLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**creator** | [**HarLogCreator**](HarLogCreator.md) |  | 
**browser** | [**HarLogCreator**](HarLogCreator.md) |  | [optional] 
**pages** | [**List[Page]**](Page.md) |  | 
**entries** | [**List[HarEntry]**](HarEntry.md) |  | 
**trace_id** | **str** | W3C Trace Context trace ID for distributed tracing | [optional] 
**span_id** | **str** | W3C Trace Context span ID for this HAR trace root | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from BrowserUpMitmProxyClient.models.har_log import HarLog

# TODO update the JSON string below
json = "{}"
# create an instance of HarLog from a JSON string
har_log_instance = HarLog.from_json(json)
# print the JSON string representation of the object
print(HarLog.to_json())

# convert the object into a dict
har_log_dict = har_log_instance.to_dict()
# create an instance of HarLog from a dict
har_log_from_dict = HarLog.from_dict(har_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


