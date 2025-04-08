# BrowserUpMitmProxyClient.Model.Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartedDateTime** | **DateTime** |  | 
**Id** | **string** |  | 
**Title** | **string** |  | 
**PageTimings** | [**PageTimings**](PageTimings.md) |  | 
**Verifications** | [**List&lt;VerifyResult&gt;**](VerifyResult.md) |  | [optional] 
**Metrics** | [**List&lt;Metric&gt;**](Metric.md) |  | [optional] 
**Errors** | [**List&lt;Error&gt;**](Error.md) |  | [optional] 
**SpanId** | **string** | W3C Trace Context span ID for this page | [optional] 
**ParentId** | **string** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] 
**Comment** | **string** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

