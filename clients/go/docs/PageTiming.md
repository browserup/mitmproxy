# PageTiming

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OnContentLoad** | Pointer to **float32** | onContentLoad per the browser | [optional] 
**OnLoad** | Pointer to **float32** | onLoad per the browser | [optional] 
**FirstInputDelay** | Pointer to **float32** | firstInputDelay from the browser | [optional] 
**FirstPaint** | Pointer to **float32** | firstPaint from the browser | [optional] 
**CumulativeLayoutShift** | Pointer to **float32** | cumulativeLayoutShift metric from the browser | [optional] 
**LargestContentfulPaint** | Pointer to **float32** | largestContentfulPaint from the browser | [optional] 
**DomInteractive** | Pointer to **float32** | domInteractive from the browser | [optional] 
**FirstContentfulPaint** | Pointer to **float32** | firstContentfulPaint from the browser | [optional] 
**Dns** | Pointer to **float32** | dns lookup time from the browser | [optional] 
**Ssl** | Pointer to **float32** | Ssl connect time from the browser | [optional] 
**TimeToFirstByte** | Pointer to **float32** | Time to first byte of the page&#39;s first request per the browser | [optional] 
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

`func (o *PageTiming) GetOnContentLoad() float32`

GetOnContentLoad returns the OnContentLoad field if non-nil, zero value otherwise.

### GetOnContentLoadOk

`func (o *PageTiming) GetOnContentLoadOk() (*float32, bool)`

GetOnContentLoadOk returns a tuple with the OnContentLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnContentLoad

`func (o *PageTiming) SetOnContentLoad(v float32)`

SetOnContentLoad sets OnContentLoad field to given value.

### HasOnContentLoad

`func (o *PageTiming) HasOnContentLoad() bool`

HasOnContentLoad returns a boolean if a field has been set.

### GetOnLoad

`func (o *PageTiming) GetOnLoad() float32`

GetOnLoad returns the OnLoad field if non-nil, zero value otherwise.

### GetOnLoadOk

`func (o *PageTiming) GetOnLoadOk() (*float32, bool)`

GetOnLoadOk returns a tuple with the OnLoad field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnLoad

`func (o *PageTiming) SetOnLoad(v float32)`

SetOnLoad sets OnLoad field to given value.

### HasOnLoad

`func (o *PageTiming) HasOnLoad() bool`

HasOnLoad returns a boolean if a field has been set.

### GetFirstInputDelay

`func (o *PageTiming) GetFirstInputDelay() float32`

GetFirstInputDelay returns the FirstInputDelay field if non-nil, zero value otherwise.

### GetFirstInputDelayOk

`func (o *PageTiming) GetFirstInputDelayOk() (*float32, bool)`

GetFirstInputDelayOk returns a tuple with the FirstInputDelay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstInputDelay

`func (o *PageTiming) SetFirstInputDelay(v float32)`

SetFirstInputDelay sets FirstInputDelay field to given value.

### HasFirstInputDelay

`func (o *PageTiming) HasFirstInputDelay() bool`

HasFirstInputDelay returns a boolean if a field has been set.

### GetFirstPaint

`func (o *PageTiming) GetFirstPaint() float32`

GetFirstPaint returns the FirstPaint field if non-nil, zero value otherwise.

### GetFirstPaintOk

`func (o *PageTiming) GetFirstPaintOk() (*float32, bool)`

GetFirstPaintOk returns a tuple with the FirstPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstPaint

`func (o *PageTiming) SetFirstPaint(v float32)`

SetFirstPaint sets FirstPaint field to given value.

### HasFirstPaint

`func (o *PageTiming) HasFirstPaint() bool`

HasFirstPaint returns a boolean if a field has been set.

### GetCumulativeLayoutShift

`func (o *PageTiming) GetCumulativeLayoutShift() float32`

GetCumulativeLayoutShift returns the CumulativeLayoutShift field if non-nil, zero value otherwise.

### GetCumulativeLayoutShiftOk

`func (o *PageTiming) GetCumulativeLayoutShiftOk() (*float32, bool)`

GetCumulativeLayoutShiftOk returns a tuple with the CumulativeLayoutShift field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCumulativeLayoutShift

`func (o *PageTiming) SetCumulativeLayoutShift(v float32)`

SetCumulativeLayoutShift sets CumulativeLayoutShift field to given value.

### HasCumulativeLayoutShift

`func (o *PageTiming) HasCumulativeLayoutShift() bool`

HasCumulativeLayoutShift returns a boolean if a field has been set.

### GetLargestContentfulPaint

`func (o *PageTiming) GetLargestContentfulPaint() float32`

GetLargestContentfulPaint returns the LargestContentfulPaint field if non-nil, zero value otherwise.

### GetLargestContentfulPaintOk

`func (o *PageTiming) GetLargestContentfulPaintOk() (*float32, bool)`

GetLargestContentfulPaintOk returns a tuple with the LargestContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLargestContentfulPaint

`func (o *PageTiming) SetLargestContentfulPaint(v float32)`

SetLargestContentfulPaint sets LargestContentfulPaint field to given value.

### HasLargestContentfulPaint

`func (o *PageTiming) HasLargestContentfulPaint() bool`

HasLargestContentfulPaint returns a boolean if a field has been set.

### GetDomInteractive

`func (o *PageTiming) GetDomInteractive() float32`

GetDomInteractive returns the DomInteractive field if non-nil, zero value otherwise.

### GetDomInteractiveOk

`func (o *PageTiming) GetDomInteractiveOk() (*float32, bool)`

GetDomInteractiveOk returns a tuple with the DomInteractive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomInteractive

`func (o *PageTiming) SetDomInteractive(v float32)`

SetDomInteractive sets DomInteractive field to given value.

### HasDomInteractive

`func (o *PageTiming) HasDomInteractive() bool`

HasDomInteractive returns a boolean if a field has been set.

### GetFirstContentfulPaint

`func (o *PageTiming) GetFirstContentfulPaint() float32`

GetFirstContentfulPaint returns the FirstContentfulPaint field if non-nil, zero value otherwise.

### GetFirstContentfulPaintOk

`func (o *PageTiming) GetFirstContentfulPaintOk() (*float32, bool)`

GetFirstContentfulPaintOk returns a tuple with the FirstContentfulPaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstContentfulPaint

`func (o *PageTiming) SetFirstContentfulPaint(v float32)`

SetFirstContentfulPaint sets FirstContentfulPaint field to given value.

### HasFirstContentfulPaint

`func (o *PageTiming) HasFirstContentfulPaint() bool`

HasFirstContentfulPaint returns a boolean if a field has been set.

### GetDns

`func (o *PageTiming) GetDns() float32`

GetDns returns the Dns field if non-nil, zero value otherwise.

### GetDnsOk

`func (o *PageTiming) GetDnsOk() (*float32, bool)`

GetDnsOk returns a tuple with the Dns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDns

`func (o *PageTiming) SetDns(v float32)`

SetDns sets Dns field to given value.

### HasDns

`func (o *PageTiming) HasDns() bool`

HasDns returns a boolean if a field has been set.

### GetSsl

`func (o *PageTiming) GetSsl() float32`

GetSsl returns the Ssl field if non-nil, zero value otherwise.

### GetSslOk

`func (o *PageTiming) GetSslOk() (*float32, bool)`

GetSslOk returns a tuple with the Ssl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsl

`func (o *PageTiming) SetSsl(v float32)`

SetSsl sets Ssl field to given value.

### HasSsl

`func (o *PageTiming) HasSsl() bool`

HasSsl returns a boolean if a field has been set.

### GetTimeToFirstByte

`func (o *PageTiming) GetTimeToFirstByte() float32`

GetTimeToFirstByte returns the TimeToFirstByte field if non-nil, zero value otherwise.

### GetTimeToFirstByteOk

`func (o *PageTiming) GetTimeToFirstByteOk() (*float32, bool)`

GetTimeToFirstByteOk returns a tuple with the TimeToFirstByte field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeToFirstByte

`func (o *PageTiming) SetTimeToFirstByte(v float32)`

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


