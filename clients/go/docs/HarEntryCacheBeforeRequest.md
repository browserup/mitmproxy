# HarEntryCacheBeforeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Expires** | Pointer to **string** |  | [optional] 
**LastAccess** | **string** |  | 
**ETag** | **string** |  | 
**HitCount** | **int32** |  | 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryCacheBeforeRequest

`func NewHarEntryCacheBeforeRequest(lastAccess string, eTag string, hitCount int32, ) *HarEntryCacheBeforeRequest`

NewHarEntryCacheBeforeRequest instantiates a new HarEntryCacheBeforeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryCacheBeforeRequestWithDefaults

`func NewHarEntryCacheBeforeRequestWithDefaults() *HarEntryCacheBeforeRequest`

NewHarEntryCacheBeforeRequestWithDefaults instantiates a new HarEntryCacheBeforeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpires

`func (o *HarEntryCacheBeforeRequest) GetExpires() string`

GetExpires returns the Expires field if non-nil, zero value otherwise.

### GetExpiresOk

`func (o *HarEntryCacheBeforeRequest) GetExpiresOk() (*string, bool)`

GetExpiresOk returns a tuple with the Expires field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpires

`func (o *HarEntryCacheBeforeRequest) SetExpires(v string)`

SetExpires sets Expires field to given value.

### HasExpires

`func (o *HarEntryCacheBeforeRequest) HasExpires() bool`

HasExpires returns a boolean if a field has been set.

### GetLastAccess

`func (o *HarEntryCacheBeforeRequest) GetLastAccess() string`

GetLastAccess returns the LastAccess field if non-nil, zero value otherwise.

### GetLastAccessOk

`func (o *HarEntryCacheBeforeRequest) GetLastAccessOk() (*string, bool)`

GetLastAccessOk returns a tuple with the LastAccess field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastAccess

`func (o *HarEntryCacheBeforeRequest) SetLastAccess(v string)`

SetLastAccess sets LastAccess field to given value.


### GetETag

`func (o *HarEntryCacheBeforeRequest) GetETag() string`

GetETag returns the ETag field if non-nil, zero value otherwise.

### GetETagOk

`func (o *HarEntryCacheBeforeRequest) GetETagOk() (*string, bool)`

GetETagOk returns a tuple with the ETag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetETag

`func (o *HarEntryCacheBeforeRequest) SetETag(v string)`

SetETag sets ETag field to given value.


### GetHitCount

`func (o *HarEntryCacheBeforeRequest) GetHitCount() int32`

GetHitCount returns the HitCount field if non-nil, zero value otherwise.

### GetHitCountOk

`func (o *HarEntryCacheBeforeRequest) GetHitCountOk() (*int32, bool)`

GetHitCountOk returns a tuple with the HitCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHitCount

`func (o *HarEntryCacheBeforeRequest) SetHitCount(v int32)`

SetHitCount sets HitCount field to given value.


### GetComment

`func (o *HarEntryCacheBeforeRequest) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryCacheBeforeRequest) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryCacheBeforeRequest) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryCacheBeforeRequest) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


