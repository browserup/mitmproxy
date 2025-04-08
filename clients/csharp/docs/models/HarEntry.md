# BrowserUpMitmProxyClient.Model.HarEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartedDateTime** | **DateTime** |  | 
**Time** | **long** |  | 
**Request** | [**HarEntryRequest**](HarEntryRequest.md) |  | 
**Response** | [**HarEntryResponse**](HarEntryResponse.md) |  | 
**Cache** | [**HarEntryCache**](HarEntryCache.md) |  | 
**Timings** | [**HarEntryTimings**](HarEntryTimings.md) |  | 
**Pageref** | **string** |  | [optional] 
**ServerIPAddress** | **string** |  | [optional] 
**WebSocketMessages** | [**List&lt;WebSocketMessage&gt;**](WebSocketMessage.md) |  | [optional] 
**SpanId** | **string** | W3C Trace Context span ID for this entry | [optional] 
**ParentId** | **string** | W3C Trace Context parent span ID (typically the page span ID) | [optional] 
**TraceId** | **string** | W3C Trace Context trace ID for distributed tracing | [optional] 
**Connection** | **string** |  | [optional] 
**Comment** | **string** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

