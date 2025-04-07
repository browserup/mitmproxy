# WebSocketMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**Opcode** | **float32** |  | 
**Data** | **string** |  | 
**Time** | **float32** |  | 

## Methods

### NewWebSocketMessage

`func NewWebSocketMessage(type_ string, opcode float32, data string, time float32, ) *WebSocketMessage`

NewWebSocketMessage instantiates a new WebSocketMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebSocketMessageWithDefaults

`func NewWebSocketMessageWithDefaults() *WebSocketMessage`

NewWebSocketMessageWithDefaults instantiates a new WebSocketMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *WebSocketMessage) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *WebSocketMessage) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *WebSocketMessage) SetType(v string)`

SetType sets Type field to given value.


### GetOpcode

`func (o *WebSocketMessage) GetOpcode() float32`

GetOpcode returns the Opcode field if non-nil, zero value otherwise.

### GetOpcodeOk

`func (o *WebSocketMessage) GetOpcodeOk() (*float32, bool)`

GetOpcodeOk returns a tuple with the Opcode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpcode

`func (o *WebSocketMessage) SetOpcode(v float32)`

SetOpcode sets Opcode field to given value.


### GetData

`func (o *WebSocketMessage) GetData() string`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *WebSocketMessage) GetDataOk() (*string, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *WebSocketMessage) SetData(v string)`

SetData sets Data field to given value.


### GetTime

`func (o *WebSocketMessage) GetTime() float32`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *WebSocketMessage) GetTimeOk() (*float32, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTime

`func (o *WebSocketMessage) SetTime(v float32)`

SetTime sets Time field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


