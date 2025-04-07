# PageTimings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OnContentLoad** | **int64** |  | [default to -1]
**OnLoad** | **int64** |  | [default to -1]
**Href** | Pointer to **string** |  | [optional] [default to ""]
**Dns** | Pointer to **int64** |  | [optional] [default to -1]
**Ssl** | Pointer to **int64** |  | [optional] [default to -1]
**TimeToFirstByte** | Pointer to **int64** |  | [optional] [default to -1]
**CumulativeLayoutShift** | Pointer to **float32** |  | [optional] [default to -1]
**LargestContentfulPaint** | Pointer to [**LargestContentfulPaint**](LargestContentfulPaint.md) |  | [optional] 
**FirstPaint** | Pointer to **int64** |  | [optional] [default to -1]
**FirstInputDelay** | Pointer to **float32** |  | [optional] [default to -1]
**DomInteractive** | Pointer to **int64** |  | [optional] [default to -1]
**FirstContentfulPaint** | Pointer to **int64** |  | [optional] [default to -1]
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewPageTimings

`func NewPageTimings(onContentLoad int64, onLoad int64, ) *PageTimings`

NewPageTimings instantiates a new PageTimings object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPageTimingsWithDefaults

`func NewPageTimingsWithDefaults() *PageTimings`

NewPageTimingsWithDefaults instantiates a new PageTimings object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOnContentLoad

`func (o *PageTimings) GetOnContentLoad() int64`

GetOnContentLoad returns the OnContentLoad field if non-nil, zero value otherwise.

### GetOnContentLoadOk

`func (o *PageTimings) GetOnContentLoadOk() (*int64, bool)`

GetOnContentLoadOk returns a tuple with the OnContentLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnContentLoad

`func (o *PageTimings) SetOnContentLoad(v int64)`

SetOnContentLoad sets OnContentLoad field to given value.


### GetOnLoad

`func (o *PageTimings) GetOnLoad() int64`

GetOnLoad returns the OnLoad field if non-nil, zero value otherwise.

### GetOnLoadOk

`func (o *PageTimings) GetOnLoadOk() (*int64, bool)`

GetOnLoadOk returns a tuple with the OnLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnLoad

`func (o *PageTimings) SetOnLoad(v int64)`

SetOnLoad sets OnLoad field to given value.


### GetHref

`func (o *PageTimings) GetHref() string`

GetHref returns the Href field if non-nil, zero value otherwise.

### GetHrefOk

`func (o *PageTimings) GetHrefOk() (*string, bool)`

GetHrefOk returns a tuple with the Href field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHref

`func (o *PageTimings) SetHref(v string)`

SetHref sets Href field to given value.

### HasHref

`func (o *PageTimings) HasHref() bool`

HasHref returns a boolean if a field has been set.

### GetDns

`func (o *PageTimings) GetDns() int64`

GetDns returns the Dns field if non-nil, zero value otherwise.

### GetDnsOk

`func (o *PageTimings) GetDnsOk() (*int64, bool)`

GetDnsOk returns a tuple with the Dns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDns

`func (o *PageTimings) SetDns(v int64)`

SetDns sets Dns field to given value.

### HasDns

`func (o *PageTimings) HasDns() bool`

HasDns returns a boolean if a field has been set.

### GetSsl

`func (o *PageTimings) GetSsl() int64`

GetSsl returns the Ssl field if non-nil, zero value otherwise.

### GetSslOk

`func (o *PageTimings) GetSslOk() (*int64, bool)`

GetSslOk returns a tuple with the Ssl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsl

`func (o *PageTimings) SetSsl(v int64)`

SetSsl sets Ssl field to given value.

### HasSsl

`func (o *PageTimings) HasSsl() bool`

HasSsl returns a boolean if a field has been set.

### GetTimeToFirstByte

`func (o *PageTimings) GetTimeToFirstByte() int64`

GetTimeToFirstByte returns the TimeToFirstByte field if non-nil, zero value otherwise.

### GetTimeToFirstByteOk

`func (o *PageTimings) GetTimeToFirstByteOk() (*int64, bool)`

GetTimeToFirstByteOk returns a tuple with the TimeToFirstByte field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeToFirstByte

`func (o *PageTimings) SetTimeToFirstByte(v int64)`

SetTimeToFirstByte sets TimeToFirstByte field to given value.

### HasTimeToFirstByte

`func (o *PageTimings) HasTimeToFirstByte() bool`

HasTimeToFirstByte returns a boolean if a field has been set.

### GetCumulativeLayoutShift

`func (o *PageTimings) GetCumulativeLayoutShift() float32`

GetCumulativeLayoutShift returns the CumulativeLayoutShift field if non-nil, zero value otherwise.

### GetCumulativeLayoutShiftOk

`func (o *PageTimings) GetCumulativeLayoutShiftOk() (*float32, bool)`

GetCumulativeLayoutShiftOk returns a tuple with the CumulativeLayoutShift field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCumulativeLayoutShift

`func (o *PageTimings) SetCumulativeLayoutShift(v float32)`

SetCumulativeLayoutShift sets CumulativeLayoutShift field to given value.

### HasCumulativeLayoutShift

`func (o *PageTimings) HasCumulativeLayoutShift() bool`

HasCumulativeLayoutShift returns a boolean if a field has been set.

### GetLargestContentfulPaint

`func (o *PageTimings) GetLargestContentfulPaint() LargestContentfulPaint`

GetLargestContentfulPaint returns the LargestContentfulPaint field if non-nil, zero value otherwise.

### GetLargestContentfulPaintOk

`func (o *PageTimings) GetLargestContentfulPaintOk() (*LargestContentfulPaint, bool)`

GetLargestContentfulPaintOk returns a tuple with the LargestContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLargestContentfulPaint

`func (o *PageTimings) SetLargestContentfulPaint(v LargestContentfulPaint)`

SetLargestContentfulPaint sets LargestContentfulPaint field to given value.

### HasLargestContentfulPaint

`func (o *PageTimings) HasLargestContentfulPaint() bool`

HasLargestContentfulPaint returns a boolean if a field has been set.

### GetFirstPaint

`func (o *PageTimings) GetFirstPaint() int64`

GetFirstPaint returns the FirstPaint field if non-nil, zero value otherwise.

### GetFirstPaintOk

`func (o *PageTimings) GetFirstPaintOk() (*int64, bool)`

GetFirstPaintOk returns a tuple with the FirstPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstPaint

`func (o *PageTimings) SetFirstPaint(v int64)`

SetFirstPaint sets FirstPaint field to given value.

### HasFirstPaint

`func (o *PageTimings) HasFirstPaint() bool`

HasFirstPaint returns a boolean if a field has been set.

### GetFirstInputDelay

`func (o *PageTimings) GetFirstInputDelay() float32`

GetFirstInputDelay returns the FirstInputDelay field if non-nil, zero value otherwise.

### GetFirstInputDelayOk

`func (o *PageTimings) GetFirstInputDelayOk() (*float32, bool)`

GetFirstInputDelayOk returns a tuple with the FirstInputDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstInputDelay

`func (o *PageTimings) SetFirstInputDelay(v float32)`

SetFirstInputDelay sets FirstInputDelay field to given value.

### HasFirstInputDelay

`func (o *PageTimings) HasFirstInputDelay() bool`

HasFirstInputDelay returns a boolean if a field has been set.

### GetDomInteractive

`func (o *PageTimings) GetDomInteractive() int64`

GetDomInteractive returns the DomInteractive field if non-nil, zero value otherwise.

### GetDomInteractiveOk

`func (o *PageTimings) GetDomInteractiveOk() (*int64, bool)`

GetDomInteractiveOk returns a tuple with the DomInteractive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomInteractive

`func (o *PageTimings) SetDomInteractive(v int64)`

SetDomInteractive sets DomInteractive field to given value.

### HasDomInteractive

`func (o *PageTimings) HasDomInteractive() bool`

HasDomInteractive returns a boolean if a field has been set.

### GetFirstContentfulPaint

`func (o *PageTimings) GetFirstContentfulPaint() int64`

GetFirstContentfulPaint returns the FirstContentfulPaint field if non-nil, zero value otherwise.

### GetFirstContentfulPaintOk

`func (o *PageTimings) GetFirstContentfulPaintOk() (*int64, bool)`

GetFirstContentfulPaintOk returns a tuple with the FirstContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstContentfulPaint

`func (o *PageTimings) SetFirstContentfulPaint(v int64)`

SetFirstContentfulPaint sets FirstContentfulPaint field to given value.

### HasFirstContentfulPaint

`func (o *PageTimings) HasFirstContentfulPaint() bool`

HasFirstContentfulPaint returns a boolean if a field has been set.

### GetComment

`func (o *PageTimings) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *PageTimings) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *PageTimings) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *PageTimings) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


