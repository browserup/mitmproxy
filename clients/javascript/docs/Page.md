# BrowserUpMitmProxyClient.Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startedDateTime** | **Date** |  | 
**id** | **String** |  | 
**title** | **String** |  | 
**verifications** | [**[VerifyResult]**](VerifyResult.md) |  | [optional] 
**metrics** | [**[Metric]**](Metric.md) |  | [optional] 
**errors** | [**[Error]**](Error.md) |  | [optional] 
**spanId** | **String** | W3C Trace Context span ID for this page | [optional] 
**parentId** | **String** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] 
**pageTimings** | [**PageTimings**](PageTimings.md) |  | 
**comment** | **String** |  | [optional] 


