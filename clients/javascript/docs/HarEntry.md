# BrowserUpMitmProxyClient.HarEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageref** | **String** |  | [optional] 
**startedDateTime** | **Date** |  | 
**time** | **Number** |  | 
**request** | [**HarEntryRequest**](HarEntryRequest.md) |  | 
**response** | [**HarEntryResponse**](HarEntryResponse.md) |  | 
**cache** | [**HarEntryCache**](HarEntryCache.md) |  | 
**timings** | [**HarEntryTimings**](HarEntryTimings.md) |  | 
**serverIPAddress** | **String** |  | [optional] 
**webSocketMessages** | [**[WebSocketMessage]**](WebSocketMessage.md) |  | [optional] 
**spanId** | **String** | W3C Trace Context span ID for this entry | [optional] 
**parentId** | **String** | W3C Trace Context parent span ID (typically the page span ID) | [optional] 
**traceId** | **String** | W3C Trace Context trace ID for distributed tracing | [optional] 
**connection** | **String** |  | [optional] 
**comment** | **String** |  | [optional] 


