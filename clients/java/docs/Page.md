

# Page


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startedDateTime** | **OffsetDateTime** |  |  |
|**id** | **String** |  |  |
|**title** | **String** |  |  |
|**verifications** | [**List&lt;VerifyResult&gt;**](VerifyResult.md) |  |  [optional] |
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) |  |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) |  |  [optional] |
|**spanId** | **String** | W3C Trace Context span ID for this page |  [optional] |
|**parentId** | **String** | W3C Trace Context parent span ID (typically the HAR log span ID) |  [optional] |
|**pageTimings** | **PageTimings** |  |  |
|**comment** | **String** |  |  [optional] |



