# Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name of Custom Metric to add to the page under _metrics | [optional] 
**Value** | Pointer to **float64** | Value for the metric | [optional] 

## Methods

### NewMetric

`func NewMetric() *Metric`

NewMetric instantiates a new Metric object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMetricWithDefaults

`func NewMetricWithDefaults() *Metric`

NewMetricWithDefaults instantiates a new Metric object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Metric) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Metric) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Metric) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Metric) HasName() bool`

HasName returns a boolean if a field has been set.

### GetValue

`func (o *Metric) GetValue() float64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Metric) GetValueOk() (*float64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Metric) SetValue(v float64)`

SetValue sets Value field to given value.

### HasValue

`func (o *Metric) HasValue() bool`

HasValue returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


