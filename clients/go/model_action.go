/*
BrowserUp MitmProxy

___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 

API version: 1.25
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package BrowserUpMitmProxyClient

import (
	"encoding/json"
)

// checks if the Action type satisfies the MappedNullable interface at compile time
var _ MappedNullable = &Action{}

// Action struct for Action
type Action struct {
	Name *string `json:"name,omitempty"`
	Id *string `json:"id,omitempty"`
	ClassName *string `json:"className,omitempty"`
	TagName *string `json:"tagName,omitempty"`
	Xpath *string `json:"xpath,omitempty"`
	DataAttributes *string `json:"dataAttributes,omitempty"`
	FormName *string `json:"formName,omitempty"`
	Content *string `json:"content,omitempty"`
}

// NewAction instantiates a new Action object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewAction() *Action {
	this := Action{}
	return &this
}

// NewActionWithDefaults instantiates a new Action object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewActionWithDefaults() *Action {
	this := Action{}
	return &this
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Action) GetName() string {
	if o == nil || IsNil(o.Name) {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetNameOk() (*string, bool) {
	if o == nil || IsNil(o.Name) {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Action) HasName() bool {
	if o != nil && !IsNil(o.Name) {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Action) SetName(v string) {
	o.Name = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Action) GetId() string {
	if o == nil || IsNil(o.Id) {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetIdOk() (*string, bool) {
	if o == nil || IsNil(o.Id) {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Action) HasId() bool {
	if o != nil && !IsNil(o.Id) {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *Action) SetId(v string) {
	o.Id = &v
}

// GetClassName returns the ClassName field value if set, zero value otherwise.
func (o *Action) GetClassName() string {
	if o == nil || IsNil(o.ClassName) {
		var ret string
		return ret
	}
	return *o.ClassName
}

// GetClassNameOk returns a tuple with the ClassName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetClassNameOk() (*string, bool) {
	if o == nil || IsNil(o.ClassName) {
		return nil, false
	}
	return o.ClassName, true
}

// HasClassName returns a boolean if a field has been set.
func (o *Action) HasClassName() bool {
	if o != nil && !IsNil(o.ClassName) {
		return true
	}

	return false
}

// SetClassName gets a reference to the given string and assigns it to the ClassName field.
func (o *Action) SetClassName(v string) {
	o.ClassName = &v
}

// GetTagName returns the TagName field value if set, zero value otherwise.
func (o *Action) GetTagName() string {
	if o == nil || IsNil(o.TagName) {
		var ret string
		return ret
	}
	return *o.TagName
}

// GetTagNameOk returns a tuple with the TagName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetTagNameOk() (*string, bool) {
	if o == nil || IsNil(o.TagName) {
		return nil, false
	}
	return o.TagName, true
}

// HasTagName returns a boolean if a field has been set.
func (o *Action) HasTagName() bool {
	if o != nil && !IsNil(o.TagName) {
		return true
	}

	return false
}

// SetTagName gets a reference to the given string and assigns it to the TagName field.
func (o *Action) SetTagName(v string) {
	o.TagName = &v
}

// GetXpath returns the Xpath field value if set, zero value otherwise.
func (o *Action) GetXpath() string {
	if o == nil || IsNil(o.Xpath) {
		var ret string
		return ret
	}
	return *o.Xpath
}

// GetXpathOk returns a tuple with the Xpath field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetXpathOk() (*string, bool) {
	if o == nil || IsNil(o.Xpath) {
		return nil, false
	}
	return o.Xpath, true
}

// HasXpath returns a boolean if a field has been set.
func (o *Action) HasXpath() bool {
	if o != nil && !IsNil(o.Xpath) {
		return true
	}

	return false
}

// SetXpath gets a reference to the given string and assigns it to the Xpath field.
func (o *Action) SetXpath(v string) {
	o.Xpath = &v
}

// GetDataAttributes returns the DataAttributes field value if set, zero value otherwise.
func (o *Action) GetDataAttributes() string {
	if o == nil || IsNil(o.DataAttributes) {
		var ret string
		return ret
	}
	return *o.DataAttributes
}

// GetDataAttributesOk returns a tuple with the DataAttributes field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetDataAttributesOk() (*string, bool) {
	if o == nil || IsNil(o.DataAttributes) {
		return nil, false
	}
	return o.DataAttributes, true
}

// HasDataAttributes returns a boolean if a field has been set.
func (o *Action) HasDataAttributes() bool {
	if o != nil && !IsNil(o.DataAttributes) {
		return true
	}

	return false
}

// SetDataAttributes gets a reference to the given string and assigns it to the DataAttributes field.
func (o *Action) SetDataAttributes(v string) {
	o.DataAttributes = &v
}

// GetFormName returns the FormName field value if set, zero value otherwise.
func (o *Action) GetFormName() string {
	if o == nil || IsNil(o.FormName) {
		var ret string
		return ret
	}
	return *o.FormName
}

// GetFormNameOk returns a tuple with the FormName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetFormNameOk() (*string, bool) {
	if o == nil || IsNil(o.FormName) {
		return nil, false
	}
	return o.FormName, true
}

// HasFormName returns a boolean if a field has been set.
func (o *Action) HasFormName() bool {
	if o != nil && !IsNil(o.FormName) {
		return true
	}

	return false
}

// SetFormName gets a reference to the given string and assigns it to the FormName field.
func (o *Action) SetFormName(v string) {
	o.FormName = &v
}

// GetContent returns the Content field value if set, zero value otherwise.
func (o *Action) GetContent() string {
	if o == nil || IsNil(o.Content) {
		var ret string
		return ret
	}
	return *o.Content
}

// GetContentOk returns a tuple with the Content field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Action) GetContentOk() (*string, bool) {
	if o == nil || IsNil(o.Content) {
		return nil, false
	}
	return o.Content, true
}

// HasContent returns a boolean if a field has been set.
func (o *Action) HasContent() bool {
	if o != nil && !IsNil(o.Content) {
		return true
	}

	return false
}

// SetContent gets a reference to the given string and assigns it to the Content field.
func (o *Action) SetContent(v string) {
	o.Content = &v
}

func (o Action) MarshalJSON() ([]byte, error) {
	toSerialize,err := o.ToMap()
	if err != nil {
		return []byte{}, err
	}
	return json.Marshal(toSerialize)
}

func (o Action) ToMap() (map[string]interface{}, error) {
	toSerialize := map[string]interface{}{}
	if !IsNil(o.Name) {
		toSerialize["name"] = o.Name
	}
	if !IsNil(o.Id) {
		toSerialize["id"] = o.Id
	}
	if !IsNil(o.ClassName) {
		toSerialize["className"] = o.ClassName
	}
	if !IsNil(o.TagName) {
		toSerialize["tagName"] = o.TagName
	}
	if !IsNil(o.Xpath) {
		toSerialize["xpath"] = o.Xpath
	}
	if !IsNil(o.DataAttributes) {
		toSerialize["dataAttributes"] = o.DataAttributes
	}
	if !IsNil(o.FormName) {
		toSerialize["formName"] = o.FormName
	}
	if !IsNil(o.Content) {
		toSerialize["content"] = o.Content
	}
	return toSerialize, nil
}

type NullableAction struct {
	value *Action
	isSet bool
}

func (v NullableAction) Get() *Action {
	return v.value
}

func (v *NullableAction) Set(val *Action) {
	v.value = val
	v.isSet = true
}

func (v NullableAction) IsSet() bool {
	return v.isSet
}

func (v *NullableAction) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableAction(val *Action) *NullableAction {
	return &NullableAction{value: val, isSet: true}
}

func (v NullableAction) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableAction) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


