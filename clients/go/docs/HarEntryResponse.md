# HarEntryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **int32** |  | 
**StatusText** | **string** |  | 
**HttpVersion** | **string** |  | 
**Cookies** | [**[]HarEntryRequestCookiesInner**](HarEntryRequestCookiesInner.md) |  | 
**Headers** | [**[]Header**](Header.md) |  | 
**Content** | [**HarEntryResponseContent**](HarEntryResponseContent.md) |  | 
**RedirectURL** | **string** |  | 
**HeadersSize** | **int32** |  | 
**BodySize** | **int32** |  | 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryResponse

`func NewHarEntryResponse(status int32, statusText string, httpVersion string, cookies []HarEntryRequestCookiesInner, headers []Header, content HarEntryResponseContent, redirectURL string, headersSize int32, bodySize int32, ) *HarEntryResponse`

NewHarEntryResponse instantiates a new HarEntryResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryResponseWithDefaults

`func NewHarEntryResponseWithDefaults() *HarEntryResponse`

NewHarEntryResponseWithDefaults instantiates a new HarEntryResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *HarEntryResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HarEntryResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HarEntryResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.


### GetStatusText

`func (o *HarEntryResponse) GetStatusText() string`

GetStatusText returns the StatusText field if non-nil, zero value otherwise.

### GetStatusTextOk

`func (o *HarEntryResponse) GetStatusTextOk() (*string, bool)`

GetStatusTextOk returns a tuple with the StatusText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusText

`func (o *HarEntryResponse) SetStatusText(v string)`

SetStatusText sets StatusText field to given value.


### GetHttpVersion

`func (o *HarEntryResponse) GetHttpVersion() string`

GetHttpVersion returns the HttpVersion field if non-nil, zero value otherwise.

### GetHttpVersionOk

`func (o *HarEntryResponse) GetHttpVersionOk() (*string, bool)`

GetHttpVersionOk returns a tuple with the HttpVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHttpVersion

`func (o *HarEntryResponse) SetHttpVersion(v string)`

SetHttpVersion sets HttpVersion field to given value.


### GetCookies

`func (o *HarEntryResponse) GetCookies() []HarEntryRequestCookiesInner`

GetCookies returns the Cookies field if non-nil, zero value otherwise.

### GetCookiesOk

`func (o *HarEntryResponse) GetCookiesOk() (*[]HarEntryRequestCookiesInner, bool)`

GetCookiesOk returns a tuple with the Cookies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCookies

`func (o *HarEntryResponse) SetCookies(v []HarEntryRequestCookiesInner)`

SetCookies sets Cookies field to given value.


### GetHeaders

`func (o *HarEntryResponse) GetHeaders() []Header`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *HarEntryResponse) GetHeadersOk() (*[]Header, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *HarEntryResponse) SetHeaders(v []Header)`

SetHeaders sets Headers field to given value.


### GetContent

`func (o *HarEntryResponse) GetContent() HarEntryResponseContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *HarEntryResponse) GetContentOk() (*HarEntryResponseContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *HarEntryResponse) SetContent(v HarEntryResponseContent)`

SetContent sets Content field to given value.


### GetRedirectURL

`func (o *HarEntryResponse) GetRedirectURL() string`

GetRedirectURL returns the RedirectURL field if non-nil, zero value otherwise.

### GetRedirectURLOk

`func (o *HarEntryResponse) GetRedirectURLOk() (*string, bool)`

GetRedirectURLOk returns a tuple with the RedirectURL field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectURL

`func (o *HarEntryResponse) SetRedirectURL(v string)`

SetRedirectURL sets RedirectURL field to given value.


### GetHeadersSize

`func (o *HarEntryResponse) GetHeadersSize() int32`

GetHeadersSize returns the HeadersSize field if non-nil, zero value otherwise.

### GetHeadersSizeOk

`func (o *HarEntryResponse) GetHeadersSizeOk() (*int32, bool)`

GetHeadersSizeOk returns a tuple with the HeadersSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadersSize

`func (o *HarEntryResponse) SetHeadersSize(v int32)`

SetHeadersSize sets HeadersSize field to given value.


### GetBodySize

`func (o *HarEntryResponse) GetBodySize() int32`

GetBodySize returns the BodySize field if non-nil, zero value otherwise.

### GetBodySizeOk

`func (o *HarEntryResponse) GetBodySizeOk() (*int32, bool)`

GetBodySizeOk returns a tuple with the BodySize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBodySize

`func (o *HarEntryResponse) SetBodySize(v int32)`

SetBodySize sets BodySize field to given value.


### GetComment

`func (o *HarEntryResponse) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryResponse) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryResponse) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryResponse) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


