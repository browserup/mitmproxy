# Page
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startedDateTime** | **Date** |  | [default to null] |
| **id** | **String** |  | [default to null] |
| **title** | **String** |  | [default to null] |
| **\_verifications** | [**List**](VerifyResult.md) |  | [optional] [default to []] |
| **\_metrics** | [**List**](Metric.md) |  | [optional] [default to []] |
| **\_errors** | [**List**](Error.md) |  | [optional] [default to []] |
| **\_span\_id** | **String** | W3C Trace Context span ID for this page | [optional] [default to null] |
| **\_parent\_id** | **String** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] [default to null] |
| **pageTimings** | [**PageTimings**](PageTimings.md) |  | [default to null] |
| **comment** | **String** |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

