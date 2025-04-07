# HarLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Version** | **string** |  | 
**Creator** | [**HarLogCreator**](HarLogCreator.md) |  | 
**Browser** | Pointer to [**HarLogCreator**](HarLogCreator.md) |  | [optional] 
**Pages** | [**[]Page**](Page.md) |  | 
**Entries** | [**[]HarEntry**](HarEntry.md) |  | 
**TraceId** | Pointer to **string** | W3C Trace Context trace ID for distributed tracing | [optional] 
**SpanId** | Pointer to **string** | W3C Trace Context span ID for this HAR trace root | [optional] 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarLog

`func NewHarLog(version string, creator HarLogCreator, pages []Page, entries []HarEntry, ) *HarLog`

NewHarLog instantiates a new HarLog object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarLogWithDefaults

`func NewHarLogWithDefaults() *HarLog`

NewHarLogWithDefaults instantiates a new HarLog object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVersion

`func (o *HarLog) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *HarLog) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *HarLog) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetCreator

`func (o *HarLog) GetCreator() HarLogCreator`

GetCreator returns the Creator field if non-nil, zero value otherwise.

### GetCreatorOk

`func (o *HarLog) GetCreatorOk() (*HarLogCreator, bool)`

GetCreatorOk returns a tuple with the Creator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreator

`func (o *HarLog) SetCreator(v HarLogCreator)`

SetCreator sets Creator field to given value.


### GetBrowser

`func (o *HarLog) GetBrowser() HarLogCreator`

GetBrowser returns the Browser field if non-nil, zero value otherwise.

### GetBrowserOk

`func (o *HarLog) GetBrowserOk() (*HarLogCreator, bool)`

GetBrowserOk returns a tuple with the Browser field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowser

`func (o *HarLog) SetBrowser(v HarLogCreator)`

SetBrowser sets Browser field to given value.

### HasBrowser

`func (o *HarLog) HasBrowser() bool`

HasBrowser returns a boolean if a field has been set.

### GetPages

`func (o *HarLog) GetPages() []Page`

GetPages returns the Pages field if non-nil, zero value otherwise.

### GetPagesOk

`func (o *HarLog) GetPagesOk() (*[]Page, bool)`

GetPagesOk returns a tuple with the Pages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPages

`func (o *HarLog) SetPages(v []Page)`

SetPages sets Pages field to given value.


### GetEntries

`func (o *HarLog) GetEntries() []HarEntry`

GetEntries returns the Entries field if non-nil, zero value otherwise.

### GetEntriesOk

`func (o *HarLog) GetEntriesOk() (*[]HarEntry, bool)`

GetEntriesOk returns a tuple with the Entries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntries

`func (o *HarLog) SetEntries(v []HarEntry)`

SetEntries sets Entries field to given value.


### GetTraceId

`func (o *HarLog) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *HarLog) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *HarLog) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.

### HasTraceId

`func (o *HarLog) HasTraceId() bool`

HasTraceId returns a boolean if a field has been set.

### GetSpanId

`func (o *HarLog) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *HarLog) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *HarLog) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.

### HasSpanId

`func (o *HarLog) HasSpanId() bool`

HasSpanId returns a boolean if a field has been set.

### GetComment

`func (o *HarLog) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarLog) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarLog) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarLog) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


