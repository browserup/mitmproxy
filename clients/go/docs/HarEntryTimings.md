# HarEntryTimings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Dns** | **int64** |  | [default to -1]
**Connect** | **int64** |  | [default to -1]
**Blocked** | **int64** |  | [default to -1]
**Send** | **int64** |  | [default to -1]
**Wait** | **int64** |  | [default to -1]
**Receive** | **int64** |  | [default to -1]
**Ssl** | **int64** |  | [default to -1]
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHarEntryTimings

`func NewHarEntryTimings(dns int64, connect int64, blocked int64, send int64, wait int64, receive int64, ssl int64, ) *HarEntryTimings`

NewHarEntryTimings instantiates a new HarEntryTimings object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHarEntryTimingsWithDefaults

`func NewHarEntryTimingsWithDefaults() *HarEntryTimings`

NewHarEntryTimingsWithDefaults instantiates a new HarEntryTimings object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDns

`func (o *HarEntryTimings) GetDns() int64`

GetDns returns the Dns field if non-nil, zero value otherwise.

### GetDnsOk

`func (o *HarEntryTimings) GetDnsOk() (*int64, bool)`

GetDnsOk returns a tuple with the Dns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDns

`func (o *HarEntryTimings) SetDns(v int64)`

SetDns sets Dns field to given value.


### GetConnect

`func (o *HarEntryTimings) GetConnect() int64`

GetConnect returns the Connect field if non-nil, zero value otherwise.

### GetConnectOk

`func (o *HarEntryTimings) GetConnectOk() (*int64, bool)`

GetConnectOk returns a tuple with the Connect field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnect

`func (o *HarEntryTimings) SetConnect(v int64)`

SetConnect sets Connect field to given value.


### GetBlocked

`func (o *HarEntryTimings) GetBlocked() int64`

GetBlocked returns the Blocked field if non-nil, zero value otherwise.

### GetBlockedOk

`func (o *HarEntryTimings) GetBlockedOk() (*int64, bool)`

GetBlockedOk returns a tuple with the Blocked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlocked

`func (o *HarEntryTimings) SetBlocked(v int64)`

SetBlocked sets Blocked field to given value.


### GetSend

`func (o *HarEntryTimings) GetSend() int64`

GetSend returns the Send field if non-nil, zero value otherwise.

### GetSendOk

`func (o *HarEntryTimings) GetSendOk() (*int64, bool)`

GetSendOk returns a tuple with the Send field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSend

`func (o *HarEntryTimings) SetSend(v int64)`

SetSend sets Send field to given value.


### GetWait

`func (o *HarEntryTimings) GetWait() int64`

GetWait returns the Wait field if non-nil, zero value otherwise.

### GetWaitOk

`func (o *HarEntryTimings) GetWaitOk() (*int64, bool)`

GetWaitOk returns a tuple with the Wait field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWait

`func (o *HarEntryTimings) SetWait(v int64)`

SetWait sets Wait field to given value.


### GetReceive

`func (o *HarEntryTimings) GetReceive() int64`

GetReceive returns the Receive field if non-nil, zero value otherwise.

### GetReceiveOk

`func (o *HarEntryTimings) GetReceiveOk() (*int64, bool)`

GetReceiveOk returns a tuple with the Receive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReceive

`func (o *HarEntryTimings) SetReceive(v int64)`

SetReceive sets Receive field to given value.


### GetSsl

`func (o *HarEntryTimings) GetSsl() int64`

GetSsl returns the Ssl field if non-nil, zero value otherwise.

### GetSslOk

`func (o *HarEntryTimings) GetSslOk() (*int64, bool)`

GetSslOk returns a tuple with the Ssl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsl

`func (o *HarEntryTimings) SetSsl(v int64)`

SetSsl sets Ssl field to given value.


### GetComment

`func (o *HarEntryTimings) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *HarEntryTimings) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *HarEntryTimings) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *HarEntryTimings) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


