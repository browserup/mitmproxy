# Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartedDateTime** | **time.Time** |  | 
**Id** | **string** |  | 
**Title** | **string** |  | 
**Verifications** | Pointer to [**[]VerifyResult**](VerifyResult.md) |  | [optional] [default to []]
**Metrics** | Pointer to [**[]Metric**](Metric.md) |  | [optional] [default to []]
**Errors** | Pointer to [**[]Error**](Error.md) |  | [optional] [default to []]
**SpanId** | Pointer to **string** | W3C Trace Context span ID for this page | [optional] 
**ParentId** | Pointer to **string** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] 
**PageTimings** | [**PageTimings**](PageTimings.md) |  | 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewPage

`func NewPage(startedDateTime time.Time, id string, title string, pageTimings PageTimings, ) *Page`

NewPage instantiates a new Page object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPageWithDefaults

`func NewPageWithDefaults() *Page`

NewPageWithDefaults instantiates a new Page object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStartedDateTime

`func (o *Page) GetStartedDateTime() time.Time`

GetStartedDateTime returns the StartedDateTime field if non-nil, zero value otherwise.

### GetStartedDateTimeOk

`func (o *Page) GetStartedDateTimeOk() (*time.Time, bool)`

GetStartedDateTimeOk returns a tuple with the StartedDateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedDateTime

`func (o *Page) SetStartedDateTime(v time.Time)`

SetStartedDateTime sets StartedDateTime field to given value.


### GetId

`func (o *Page) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Page) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Page) SetId(v string)`

SetId sets Id field to given value.


### GetTitle

`func (o *Page) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *Page) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *Page) SetTitle(v string)`

SetTitle sets Title field to given value.


### GetVerifications

`func (o *Page) GetVerifications() []VerifyResult`

GetVerifications returns the Verifications field if non-nil, zero value otherwise.

### GetVerificationsOk

`func (o *Page) GetVerificationsOk() (*[]VerifyResult, bool)`

GetVerificationsOk returns a tuple with the Verifications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerifications

`func (o *Page) SetVerifications(v []VerifyResult)`

SetVerifications sets Verifications field to given value.

### HasVerifications

`func (o *Page) HasVerifications() bool`

HasVerifications returns a boolean if a field has been set.

### GetMetrics

`func (o *Page) GetMetrics() []Metric`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *Page) GetMetricsOk() (*[]Metric, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *Page) SetMetrics(v []Metric)`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *Page) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.

### GetErrors

`func (o *Page) GetErrors() []Error`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *Page) GetErrorsOk() (*[]Error, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *Page) SetErrors(v []Error)`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *Page) HasErrors() bool`

HasErrors returns a boolean if a field has been set.

### GetSpanId

`func (o *Page) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *Page) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *Page) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.

### HasSpanId

`func (o *Page) HasSpanId() bool`

HasSpanId returns a boolean if a field has been set.

### GetParentId

`func (o *Page) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *Page) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *Page) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *Page) HasParentId() bool`

HasParentId returns a boolean if a field has been set.

### GetPageTimings

`func (o *Page) GetPageTimings() PageTimings`

GetPageTimings returns the PageTimings field if non-nil, zero value otherwise.

### GetPageTimingsOk

`func (o *Page) GetPageTimingsOk() (*PageTimings, bool)`

GetPageTimingsOk returns a tuple with the PageTimings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageTimings

`func (o *Page) SetPageTimings(v PageTimings)`

SetPageTimings sets PageTimings field to given value.


### GetComment

`func (o *Page) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *Page) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *Page) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *Page) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


