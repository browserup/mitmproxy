# Header

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Value** | **string** |  | 
**Comment** | Pointer to **string** |  | [optional] 

## Methods

### NewHeader

`func NewHeader(name string, value string, ) *Header`

NewHeader instantiates a new Header object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeaderWithDefaults

`func NewHeaderWithDefaults() *Header`

NewHeaderWithDefaults instantiates a new Header object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Header) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Header) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Header) SetName(v string)`

SetName sets Name field to given value.


### GetValue

`func (o *Header) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Header) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Header) SetValue(v string)`

SetValue sets Value field to given value.


### GetComment

`func (o *Header) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *Header) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *Header) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *Header) HasComment() bool`

HasComment returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


