# PageTiming

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OnContentLoad** | Pointer to **int32** | onContentLoad per the browser | [optional] 
**OnLoad** | Pointer to **int32** | onLoad per the browser | [optional] 
**FirstInputDelay** | Pointer to **int32** | firstInputDelay from the browser | [optional] 
**FirstPaint** | Pointer to **int32** | firstPaint from the browser | [optional] 
**CumulativeLayoutShift** | Pointer to **int32** | cumulativeLayoutShift metric from the browser | [optional] 
**LargestContentfulPaint** | Pointer to **int32** | largestContentfulPaint from the browser | [optional] 
**DomInteractive** | Pointer to **int32** | domInteractive from the browser | [optional] 
**FirstContentfulPaint** | Pointer to **int32** | firstContentfulPaint from the browser | [optional] 
**Dns** | Pointer to **int32** | dns lookup time from the browser | [optional] 
**Ssl** | Pointer to **int32** | Ssl connect time from the browser | [optional] 
**TimeToFirstByte** | Pointer to **int32** | Time to first byte of the page&#39;s first request per the browser | [optional] 
**Href** | Pointer to **string** | Top level href, including hashtag, etc per the browser | [optional] 
**SpanId** | Pointer to **string** | W3C Trace Context span ID for this page | [optional] 
**ParentId** | Pointer to **string** | W3C Trace Context parent span ID (typically the HAR log span ID) | [optional] 

## Methods

### NewPageTiming

`func NewPageTiming() *PageTiming`

NewPageTiming instantiates a new PageTiming object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPageTimingWithDefaults

`func NewPageTimingWithDefaults() *PageTiming`

NewPageTimingWithDefaults instantiates a new PageTiming object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOnContentLoad

`func (o *PageTiming) GetOnContentLoad() int32`

GetOnContentLoad returns the OnContentLoad field if non-nil, zero value otherwise.

### GetOnContentLoadOk

`func (o *PageTiming) GetOnContentLoadOk() (*int32, bool)`

GetOnContentLoadOk returns a tuple with the OnContentLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnContentLoad

`func (o *PageTiming) SetOnContentLoad(v int32)`

SetOnContentLoad sets OnContentLoad field to given value.

### HasOnContentLoad

`func (o *PageTiming) HasOnContentLoad() bool`

HasOnContentLoad returns a boolean if a field has been set.

### GetOnLoad

`func (o *PageTiming) GetOnLoad() int32`

GetOnLoad returns the OnLoad field if non-nil, zero value otherwise.

### GetOnLoadOk

`func (o *PageTiming) GetOnLoadOk() (*int32, bool)`

GetOnLoadOk returns a tuple with the OnLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnLoad

`func (o *PageTiming) SetOnLoad(v int32)`

SetOnLoad sets OnLoad field to given value.

### HasOnLoad

`func (o *PageTiming) HasOnLoad() bool`

HasOnLoad returns a boolean if a field has been set.

### GetFirstInputDelay

`func (o *PageTiming) GetFirstInputDelay() int32`

GetFirstInputDelay returns the FirstInputDelay field if non-nil, zero value otherwise.

### GetFirstInputDelayOk

`func (o *PageTiming) GetFirstInputDelayOk() (*int32, bool)`

GetFirstInputDelayOk returns a tuple with the FirstInputDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstInputDelay

`func (o *PageTiming) SetFirstInputDelay(v int32)`

SetFirstInputDelay sets FirstInputDelay field to given value.

### HasFirstInputDelay

`func (o *PageTiming) HasFirstInputDelay() bool`

HasFirstInputDelay returns a boolean if a field has been set.

### GetFirstPaint

`func (o *PageTiming) GetFirstPaint() int32`

GetFirstPaint returns the FirstPaint field if non-nil, zero value otherwise.

### GetFirstPaintOk

`func (o *PageTiming) GetFirstPaintOk() (*int32, bool)`

GetFirstPaintOk returns a tuple with the FirstPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstPaint

`func (o *PageTiming) SetFirstPaint(v int32)`

SetFirstPaint sets FirstPaint field to given value.

### HasFirstPaint

`func (o *PageTiming) HasFirstPaint() bool`

HasFirstPaint returns a boolean if a field has been set.

### GetCumulativeLayoutShift

`func (o *PageTiming) GetCumulativeLayoutShift() int32`

GetCumulativeLayoutShift returns the CumulativeLayoutShift field if non-nil, zero value otherwise.

### GetCumulativeLayoutShiftOk

`func (o *PageTiming) GetCumulativeLayoutShiftOk() (*int32, bool)`

GetCumulativeLayoutShiftOk returns a tuple with the CumulativeLayoutShift field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCumulativeLayoutShift

`func (o *PageTiming) SetCumulativeLayoutShift(v int32)`

SetCumulativeLayoutShift sets CumulativeLayoutShift field to given value.

### HasCumulativeLayoutShift

`func (o *PageTiming) HasCumulativeLayoutShift() bool`

HasCumulativeLayoutShift returns a boolean if a field has been set.

### GetLargestContentfulPaint

`func (o *PageTiming) GetLargestContentfulPaint() int32`

GetLargestContentfulPaint returns the LargestContentfulPaint field if non-nil, zero value otherwise.

### GetLargestContentfulPaintOk

`func (o *PageTiming) GetLargestContentfulPaintOk() (*int32, bool)`

GetLargestContentfulPaintOk returns a tuple with the LargestContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLargestContentfulPaint

`func (o *PageTiming) SetLargestContentfulPaint(v int32)`

SetLargestContentfulPaint sets LargestContentfulPaint field to given value.

### HasLargestContentfulPaint

`func (o *PageTiming) HasLargestContentfulPaint() bool`

HasLargestContentfulPaint returns a boolean if a field has been set.

### GetDomInteractive

`func (o *PageTiming) GetDomInteractive() int32`

GetDomInteractive returns the DomInteractive field if non-nil, zero value otherwise.

### GetDomInteractiveOk

`func (o *PageTiming) GetDomInteractiveOk() (*int32, bool)`

GetDomInteractiveOk returns a tuple with the DomInteractive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomInteractive

`func (o *PageTiming) SetDomInteractive(v int32)`

SetDomInteractive sets DomInteractive field to given value.

### HasDomInteractive

`func (o *PageTiming) HasDomInteractive() bool`

HasDomInteractive returns a boolean if a field has been set.

### GetFirstContentfulPaint

`func (o *PageTiming) GetFirstContentfulPaint() int32`

GetFirstContentfulPaint returns the FirstContentfulPaint field if non-nil, zero value otherwise.

### GetFirstContentfulPaintOk

`func (o *PageTiming) GetFirstContentfulPaintOk() (*int32, bool)`

GetFirstContentfulPaintOk returns a tuple with the FirstContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstContentfulPaint

`func (o *PageTiming) SetFirstContentfulPaint(v int32)`

SetFirstContentfulPaint sets FirstContentfulPaint field to given value.

### HasFirstContentfulPaint

`func (o *PageTiming) HasFirstContentfulPaint() bool`

HasFirstContentfulPaint returns a boolean if a field has been set.

### GetDns

`func (o *PageTiming) GetDns() int32`

GetDns returns the Dns field if non-nil, zero value otherwise.

### GetDnsOk

`func (o *PageTiming) GetDnsOk() (*int32, bool)`

GetDnsOk returns a tuple with the Dns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDns

`func (o *PageTiming) SetDns(v int32)`

SetDns sets Dns field to given value.

### HasDns

`func (o *PageTiming) HasDns() bool`

HasDns returns a boolean if a field has been set.

### GetSsl

`func (o *PageTiming) GetSsl() int32`

GetSsl returns the Ssl field if non-nil, zero value otherwise.

### GetSslOk

`func (o *PageTiming) GetSslOk() (*int32, bool)`

GetSslOk returns a tuple with the Ssl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsl

`func (o *PageTiming) SetSsl(v int32)`

SetSsl sets Ssl field to given value.

### HasSsl

`func (o *PageTiming) HasSsl() bool`

HasSsl returns a boolean if a field has been set.

### GetTimeToFirstByte

`func (o *PageTiming) GetTimeToFirstByte() int32`

GetTimeToFirstByte returns the TimeToFirstByte field if non-nil, zero value otherwise.

### GetTimeToFirstByteOk

`func (o *PageTiming) GetTimeToFirstByteOk() (*int32, bool)`

GetTimeToFirstByteOk returns a tuple with the TimeToFirstByte field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeToFirstByte

`func (o *PageTiming) SetTimeToFirstByte(v int32)`

SetTimeToFirstByte sets TimeToFirstByte field to given value.

### HasTimeToFirstByte

`func (o *PageTiming) HasTimeToFirstByte() bool`

HasTimeToFirstByte returns a boolean if a field has been set.

### GetHref

`func (o *PageTiming) GetHref() string`

GetHref returns the Href field if non-nil, zero value otherwise.

### GetHrefOk

`func (o *PageTiming) GetHrefOk() (*string, bool)`

GetHrefOk returns a tuple with the Href field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHref

`func (o *PageTiming) SetHref(v string)`

SetHref sets Href field to given value.

### HasHref

`func (o *PageTiming) HasHref() bool`

HasHref returns a boolean if a field has been set.

### GetSpanId

`func (o *PageTiming) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *PageTiming) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *PageTiming) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.

### HasSpanId

`func (o *PageTiming) HasSpanId() bool`

HasSpanId returns a boolean if a field has been set.

### GetParentId

`func (o *PageTiming) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *PageTiming) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *PageTiming) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *PageTiming) HasParentId() bool`

HasParentId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


