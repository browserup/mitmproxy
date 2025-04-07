# Har_log
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version** | **String** |  | [default to null] |
| **creator** | [**Har_log_creator**](Har_log_creator.md) |  | [default to null] |
| **browser** | [**Har_log_creator**](Har_log_creator.md) |  | [optional] [default to null] |
| **pages** | [**List**](Page.md) |  | [default to null] |
| **entries** | [**List**](HarEntry.md) |  | [default to null] |
| **\_trace\_id** | **String** | W3C Trace Context trace ID for distributed tracing | [optional] [default to null] |
| **\_span\_id** | **String** | W3C Trace Context span ID for this HAR trace root | [optional] [default to null] |
| **comment** | **String** |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

