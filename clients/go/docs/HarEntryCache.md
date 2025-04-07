# HarEntryCache

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BeforeRequest** | Pointer to [**NullableHarEntryCacheBeforeRequest**](HarEntryCacheBeforeRequest.md) |  | [optional] 
**AfterRequest** | Pointer to [**NullableHarEntryCacheBeforeRequest**](HarEntryCacheBeforeRequest.md) |  | [optional] 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryCache

`func NewHarEntryCache() *HarEntryCache`

NewHarEntryCache instantiates a new HarEntryCache object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryCacheWithDefaults

`func NewHarEntryCacheWithDefaults() *HarEntryCache`

NewHarEntryCacheWithDefaults instantiates a new HarEntryCache object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBeforeRequest

`func (o *HarEntryCache) GetBeforeRequest() HarEntryCacheBeforeRequest`

GetBeforeRequest returns the BeforeRequest field if non-nil, zero value otherwise.

### GetBeforeRequestOk

`func (o *HarEntryCache) GetBeforeRequestOk() (*HarEntryCacheBeforeRequest, bool)`

GetBeforeRequestOk returns a tuple with the BeforeRequest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBeforeRequest

`func (o *HarEntryCache) SetBeforeRequest(v HarEntryCacheBeforeRequest)`

SetBeforeRequest sets BeforeRequest field to given value.

### HasBeforeRequest

`func (o *HarEntryCache) HasBeforeRequest() bool`

HasBeforeRequest returns a boolean if a field has been set.

### SetBeforeRequestNil

`func (o *HarEntryCache) SetBeforeRequestNil(b bool)`

 SetBeforeRequestNil sets the value for BeforeRequest to be an explicit nil

### UnsetBeforeRequest
`func (o *HarEntryCache) UnsetBeforeRequest()`

UnsetBeforeRequest ensures that no value is present for BeforeRequest, not even an explicit nil
### GetAfterRequest

`func (o *HarEntryCache) GetAfterRequest() HarEntryCacheBeforeRequest`

GetAfterRequest returns the AfterRequest field if non-nil, zero value otherwise.

### GetAfterRequestOk

`func (o *HarEntryCache) GetAfterRequestOk() (*HarEntryCacheBeforeRequest, bool)`

GetAfterRequestOk returns a tuple with the AfterRequest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAfterRequest

`func (o *HarEntryCache) SetAfterRequest(v HarEntryCacheBeforeRequest)`

SetAfterRequest sets AfterRequest field to given value.

### HasAfterRequest

`func (o *HarEntryCache) HasAfterRequest() bool`

HasAfterRequest returns a boolean if a field has been set.

### SetAfterRequestNil

`func (o *HarEntryCache) SetAfterRequestNil(b bool)`

 SetAfterRequestNil sets the value for AfterRequest to be an explicit nil

### UnsetAfterRequest
`func (o *HarEntryCache) UnsetAfterRequest()`

UnsetAfterRequest ensures that no value is present for AfterRequest, not even an explicit nil
### GetComment

`func (o *HarEntryCache) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryCache) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryCache) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryCache) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


