# HarEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Pageref** | Pointer to **string** |  | [optional] 
**StartedDateTime** | **time.Time** |  | 
**Time** | **int64** |  | 
**Request** | [**HarEntryRequest**](HarEntryRequest.md) |  | 
**Response** | [**HarEntryResponse**](HarEntryResponse.md) |  | 
**Cache** | [**HarEntryCache**](HarEntryCache.md) |  | 
**Timings** | [**HarEntryTimings**](HarEntryTimings.md) |  | 
**ServerIPAddress** | Pointer to **string** |  | [optional] 
**WebSocketMessages** | Pointer to [**[]WebSocketMessage**](WebSocketMessage.md) |  | [optional] 
**SpanId** | Pointer to **string** | W3C Trace Context span ID for this entry | [optional] 
**ParentId** | Pointer to **string** | W3C Trace Context parent span ID (typically the page span ID) | [optional] 
**TraceId** | Pointer to **string** | W3C Trace Context trace ID for distributed tracing | [optional] 
**Connection** | Pointer to **string** |  | [optional] 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntry

`func NewHarEntry(startedDateTime time.Time, time int64, request HarEntryRequest, response HarEntryResponse, cache HarEntryCache, timings HarEntryTimings, ) *HarEntry`

NewHarEntry instantiates a new HarEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryWithDefaults

`func NewHarEntryWithDefaults() *HarEntry`

NewHarEntryWithDefaults instantiates a new HarEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPageref

`func (o *HarEntry) GetPageref() string`

GetPageref returns the Pageref field if non-nil, zero value otherwise.

### GetPagerefOk

`func (o *HarEntry) GetPagerefOk() (*string, bool)`

GetPagerefOk returns a tuple with the Pageref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageref

`func (o *HarEntry) SetPageref(v string)`

SetPageref sets Pageref field to given value.

### HasPageref

`func (o *HarEntry) HasPageref() bool`

HasPageref returns a boolean if a field has been set.

### GetStartedDateTime

`func (o *HarEntry) GetStartedDateTime() time.Time`

GetStartedDateTime returns the StartedDateTime field if non-nil, zero value otherwise.

### GetStartedDateTimeOk

`func (o *HarEntry) GetStartedDateTimeOk() (*time.Time, bool)`

GetStartedDateTimeOk returns a tuple with the StartedDateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedDateTime

`func (o *HarEntry) SetStartedDateTime(v time.Time)`

SetStartedDateTime sets StartedDateTime field to given value.


### GetTime

`func (o *HarEntry) GetTime() int64`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *HarEntry) GetTimeOk() (*int64, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTime

`func (o *HarEntry) SetTime(v int64)`

SetTime sets Time field to given value.


### GetRequest

`func (o *HarEntry) GetRequest() HarEntryRequest`

GetRequest returns the Request field if non-nil, zero value otherwise.

### GetRequestOk

`func (o *HarEntry) GetRequestOk() (*HarEntryRequest, bool)`

GetRequestOk returns a tuple with the Request field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequest

`func (o *HarEntry) SetRequest(v HarEntryRequest)`

SetRequest sets Request field to given value.


### GetResponse

`func (o *HarEntry) GetResponse() HarEntryResponse`

GetResponse returns the Response field if non-nil, zero value otherwise.

### GetResponseOk

`func (o *HarEntry) GetResponseOk() (*HarEntryResponse, bool)`

GetResponseOk returns a tuple with the Response field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponse

`func (o *HarEntry) SetResponse(v HarEntryResponse)`

SetResponse sets Response field to given value.


### GetCache

`func (o *HarEntry) GetCache() HarEntryCache`

GetCache returns the Cache field if non-nil, zero value otherwise.

### GetCacheOk

`func (o *HarEntry) GetCacheOk() (*HarEntryCache, bool)`

GetCacheOk returns a tuple with the Cache field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCache

`func (o *HarEntry) SetCache(v HarEntryCache)`

SetCache sets Cache field to given value.


### GetTimings

`func (o *HarEntry) GetTimings() HarEntryTimings`

GetTimings returns the Timings field if non-nil, zero value otherwise.

### GetTimingsOk

`func (o *HarEntry) GetTimingsOk() (*HarEntryTimings, bool)`

GetTimingsOk returns a tuple with the Timings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimings

`func (o *HarEntry) SetTimings(v HarEntryTimings)`

SetTimings sets Timings field to given value.


### GetServerIPAddress

`func (o *HarEntry) GetServerIPAddress() string`

GetServerIPAddress returns the ServerIPAddress field if non-nil, zero value otherwise.

### GetServerIPAddressOk

`func (o *HarEntry) GetServerIPAddressOk() (*string, bool)`

GetServerIPAddressOk returns a tuple with the ServerIPAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServerIPAddress

`func (o *HarEntry) SetServerIPAddress(v string)`

SetServerIPAddress sets ServerIPAddress field to given value.

### HasServerIPAddress

`func (o *HarEntry) HasServerIPAddress() bool`

HasServerIPAddress returns a boolean if a field has been set.

### GetWebSocketMessages

`func (o *HarEntry) GetWebSocketMessages() []WebSocketMessage`

GetWebSocketMessages returns the WebSocketMessages field if non-nil, zero value otherwise.

### GetWebSocketMessagesOk

`func (o *HarEntry) GetWebSocketMessagesOk() (*[]WebSocketMessage, bool)`

GetWebSocketMessagesOk returns a tuple with the WebSocketMessages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebSocketMessages

`func (o *HarEntry) SetWebSocketMessages(v []WebSocketMessage)`

SetWebSocketMessages sets WebSocketMessages field to given value.

### HasWebSocketMessages

`func (o *HarEntry) HasWebSocketMessages() bool`

HasWebSocketMessages returns a boolean if a field has been set.

### GetSpanId

`func (o *HarEntry) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *HarEntry) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *HarEntry) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.

### HasSpanId

`func (o *HarEntry) HasSpanId() bool`

HasSpanId returns a boolean if a field has been set.

### GetParentId

`func (o *HarEntry) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *HarEntry) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *HarEntry) SetParentId(v string)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *HarEntry) HasParentId() bool`

HasParentId returns a boolean if a field has been set.

### GetTraceId

`func (o *HarEntry) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *HarEntry) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *HarEntry) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.

### HasTraceId

`func (o *HarEntry) HasTraceId() bool`

HasTraceId returns a boolean if a field has been set.

### GetConnection

`func (o *HarEntry) GetConnection() string`

GetConnection returns the Connection field if non-nil, zero value otherwise.

### GetConnectionOk

`func (o *HarEntry) GetConnectionOk() (*string, bool)`

GetConnectionOk returns a tuple with the Connection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnection

`func (o *HarEntry) SetConnection(v string)`

SetConnection sets Connection field to given value.

### HasConnection

`func (o *HarEntry) HasConnection() bool`

HasConnection returns a boolean if a field has been set.

### GetComment

`func (o *HarEntry) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntry) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntry) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntry) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


