# HarEntryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Method** | **string** |  | 
**Url** | **string** |  | 
**HttpVersion** | **string** |  | 
**Cookies** | [**[]HarEntryRequestCookiesInner**](HarEntryRequestCookiesInner.md) |  | 
**Headers** | [**[]Header**](Header.md) |  | 
**QueryString** | [**[]HarEntryRequestQueryStringInner**](HarEntryRequestQueryStringInner.md) |  | 
**PostData** | Pointer to [**HarEntryRequestPostData**](HarEntryRequestPostData.md) |  | [optional] 
**HeadersSize** | **int32** |  | 
**BodySize** | **int32** |  | 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryRequest

`func NewHarEntryRequest(method string, url string, httpVersion string, cookies []HarEntryRequestCookiesInner, headers []Header, queryString []HarEntryRequestQueryStringInner, headersSize int32, bodySize int32, ) *HarEntryRequest`

NewHarEntryRequest instantiates a new HarEntryRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryRequestWithDefaults

`func NewHarEntryRequestWithDefaults() *HarEntryRequest`

NewHarEntryRequestWithDefaults instantiates a new HarEntryRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMethod

`func (o *HarEntryRequest) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *HarEntryRequest) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *HarEntryRequest) SetMethod(v string)`

SetMethod sets Method field to given value.


### GetUrl

`func (o *HarEntryRequest) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *HarEntryRequest) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *HarEntryRequest) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetHttpVersion

`func (o *HarEntryRequest) GetHttpVersion() string`

GetHttpVersion returns the HttpVersion field if non-nil, zero value otherwise.

### GetHttpVersionOk

`func (o *HarEntryRequest) GetHttpVersionOk() (*string, bool)`

GetHttpVersionOk returns a tuple with the HttpVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHttpVersion

`func (o *HarEntryRequest) SetHttpVersion(v string)`

SetHttpVersion sets HttpVersion field to given value.


### GetCookies

`func (o *HarEntryRequest) GetCookies() []HarEntryRequestCookiesInner`

GetCookies returns the Cookies field if non-nil, zero value otherwise.

### GetCookiesOk

`func (o *HarEntryRequest) GetCookiesOk() (*[]HarEntryRequestCookiesInner, bool)`

GetCookiesOk returns a tuple with the Cookies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCookies

`func (o *HarEntryRequest) SetCookies(v []HarEntryRequestCookiesInner)`

SetCookies sets Cookies field to given value.


### GetHeaders

`func (o *HarEntryRequest) GetHeaders() []Header`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *HarEntryRequest) GetHeadersOk() (*[]Header, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *HarEntryRequest) SetHeaders(v []Header)`

SetHeaders sets Headers field to given value.


### GetQueryString

`func (o *HarEntryRequest) GetQueryString() []HarEntryRequestQueryStringInner`

GetQueryString returns the QueryString field if non-nil, zero value otherwise.

### GetQueryStringOk

`func (o *HarEntryRequest) GetQueryStringOk() (*[]HarEntryRequestQueryStringInner, bool)`

GetQueryStringOk returns a tuple with the QueryString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryString

`func (o *HarEntryRequest) SetQueryString(v []HarEntryRequestQueryStringInner)`

SetQueryString sets QueryString field to given value.


### GetPostData

`func (o *HarEntryRequest) GetPostData() HarEntryRequestPostData`

GetPostData returns the PostData field if non-nil, zero value otherwise.

### GetPostDataOk

`func (o *HarEntryRequest) GetPostDataOk() (*HarEntryRequestPostData, bool)`

GetPostDataOk returns a tuple with the PostData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostData

`func (o *HarEntryRequest) SetPostData(v HarEntryRequestPostData)`

SetPostData sets PostData field to given value.

### HasPostData

`func (o *HarEntryRequest) HasPostData() bool`

HasPostData returns a boolean if a field has been set.

### GetHeadersSize

`func (o *HarEntryRequest) GetHeadersSize() int32`

GetHeadersSize returns the HeadersSize field if non-nil, zero value otherwise.

### GetHeadersSizeOk

`func (o *HarEntryRequest) GetHeadersSizeOk() (*int32, bool)`

GetHeadersSizeOk returns a tuple with the HeadersSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadersSize

`func (o *HarEntryRequest) SetHeadersSize(v int32)`

SetHeadersSize sets HeadersSize field to given value.


### GetBodySize

`func (o *HarEntryRequest) GetBodySize() int32`

GetBodySize returns the BodySize field if non-nil, zero value otherwise.

### GetBodySizeOk

`func (o *HarEntryRequest) GetBodySizeOk() (*int32, bool)`

GetBodySizeOk returns a tuple with the BodySize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBodySize

`func (o *HarEntryRequest) SetBodySize(v int32)`

SetBodySize sets BodySize field to given value.


### GetComment

`func (o *HarEntryRequest) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryRequest) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryRequest) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryRequest) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


