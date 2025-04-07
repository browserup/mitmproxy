# HarEntry
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **pageref** | **String** |  | [optional] [default to null] |
| **startedDateTime** | **Date** |  | [default to null] |
| **time** | **Long** |  | [default to null] |
| **request** | [**HarEntry_request**](HarEntry_request.md) |  | [default to null] |
| **response** | [**HarEntry_response**](HarEntry_response.md) |  | [default to null] |
| **cache** | [**HarEntry_cache**](HarEntry_cache.md) |  | [default to null] |
| **timings** | [**HarEntry_timings**](HarEntry_timings.md) |  | [default to null] |
| **serverIPAddress** | **String** |  | [optional] [default to null] |
| **\_webSocketMessages** | [**List**](WebSocketMessage.md) |  | [optional] [default to null] |
| **\_span\_id** | **String** | W3C Trace Context span ID for this entry | [optional] [default to null] |
| **\_parent\_id** | **String** | W3C Trace Context parent span ID (typically the page span ID) | [optional] [default to null] |
| **\_trace\_id** | **String** | W3C Trace Context trace ID for distributed tracing | [optional] [default to null] |
| **connection** | **String** |  | [optional] [default to null] |
| **comment** | **String** |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

