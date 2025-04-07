# MatchCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | Pointer to **string** | Request URL regexp to match | [optional] 
**Page** | Pointer to **string** | current|all | [optional] 
**Status** | Pointer to **string** | HTTP Status code to match. | [optional] 
**Content** | Pointer to **string** | Body content regexp content to match | [optional] 
**ContentType** | Pointer to **string** | Content type | [optional] 
**WebsocketMessage** | Pointer to **string** | Websocket message text to match | [optional] 
**RequestHeader** | Pointer to [**NameValuePair**](NameValuePair.md) |  | [optional] 
**RequestCookie** | Pointer to [**NameValuePair**](NameValuePair.md) |  | [optional] 
**ResponseHeader** | Pointer to [**NameValuePair**](NameValuePair.md) |  | [optional] 
**ResponseCookie** | Pointer to [**NameValuePair**](NameValuePair.md) |  | [optional] 
**JsonValid** | Pointer to **bool** | Is valid JSON | [optional] 
**JsonPath** | Pointer to **string** | Has JSON path | [optional] 
**JsonSchema** | Pointer to **string** | Validates against passed JSON schema | [optional] 
**ErrorIfNoTraffic** | Pointer to **bool** | If the proxy has NO traffic at all, return error | [optional] [default to true]

## Methods

### NewMatchCriteria

`func NewMatchCriteria() *MatchCriteria`

NewMatchCriteria instantiates a new MatchCriteria object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMatchCriteriaWithDefaults

`func NewMatchCriteriaWithDefaults() *MatchCriteria`

NewMatchCriteriaWithDefaults instantiates a new MatchCriteria object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *MatchCriteria) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *MatchCriteria) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *MatchCriteria) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *MatchCriteria) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetPage

`func (o *MatchCriteria) GetPage() string`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *MatchCriteria) GetPageOk() (*string, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *MatchCriteria) SetPage(v string)`

SetPage sets Page field to given value.

### HasPage

`func (o *MatchCriteria) HasPage() bool`

HasPage returns a boolean if a field has been set.

### GetStatus

`func (o *MatchCriteria) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *MatchCriteria) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *MatchCriteria) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *MatchCriteria) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetContent

`func (o *MatchCriteria) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *MatchCriteria) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *MatchCriteria) SetContent(v string)`

SetContent sets Content field to given value.

### HasContent

`func (o *MatchCriteria) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetContentType

`func (o *MatchCriteria) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *MatchCriteria) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *MatchCriteria) SetContentType(v string)`

SetContentType sets ContentType field to given value.

### HasContentType

`func (o *MatchCriteria) HasContentType() bool`

HasContentType returns a boolean if a field has been set.

### GetWebsocketMessage

`func (o *MatchCriteria) GetWebsocketMessage() string`

GetWebsocketMessage returns the WebsocketMessage field if non-nil, zero value otherwise.

### GetWebsocketMessageOk

`func (o *MatchCriteria) GetWebsocketMessageOk() (*string, bool)`

GetWebsocketMessageOk returns a tuple with the WebsocketMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsocketMessage

`func (o *MatchCriteria) SetWebsocketMessage(v string)`

SetWebsocketMessage sets WebsocketMessage field to given value.

### HasWebsocketMessage

`func (o *MatchCriteria) HasWebsocketMessage() bool`

HasWebsocketMessage returns a boolean if a field has been set.

### GetRequestHeader

`func (o *MatchCriteria) GetRequestHeader() NameValuePair`

GetRequestHeader returns the RequestHeader field if non-nil, zero value otherwise.

### GetRequestHeaderOk

`func (o *MatchCriteria) GetRequestHeaderOk() (*NameValuePair, bool)`

GetRequestHeaderOk returns a tuple with the RequestHeader field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestHeader

`func (o *MatchCriteria) SetRequestHeader(v NameValuePair)`

SetRequestHeader sets RequestHeader field to given value.

### HasRequestHeader

`func (o *MatchCriteria) HasRequestHeader() bool`

HasRequestHeader returns a boolean if a field has been set.

### GetRequestCookie

`func (o *MatchCriteria) GetRequestCookie() NameValuePair`

GetRequestCookie returns the RequestCookie field if non-nil, zero value otherwise.

### GetRequestCookieOk

`func (o *MatchCriteria) GetRequestCookieOk() (*NameValuePair, bool)`

GetRequestCookieOk returns a tuple with the RequestCookie field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestCookie

`func (o *MatchCriteria) SetRequestCookie(v NameValuePair)`

SetRequestCookie sets RequestCookie field to given value.

### HasRequestCookie

`func (o *MatchCriteria) HasRequestCookie() bool`

HasRequestCookie returns a boolean if a field has been set.

### GetResponseHeader

`func (o *MatchCriteria) GetResponseHeader() NameValuePair`

GetResponseHeader returns the ResponseHeader field if non-nil, zero value otherwise.

### GetResponseHeaderOk

`func (o *MatchCriteria) GetResponseHeaderOk() (*NameValuePair, bool)`

GetResponseHeaderOk returns a tuple with the ResponseHeader field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseHeader

`func (o *MatchCriteria) SetResponseHeader(v NameValuePair)`

SetResponseHeader sets ResponseHeader field to given value.

### HasResponseHeader

`func (o *MatchCriteria) HasResponseHeader() bool`

HasResponseHeader returns a boolean if a field has been set.

### GetResponseCookie

`func (o *MatchCriteria) GetResponseCookie() NameValuePair`

GetResponseCookie returns the ResponseCookie field if non-nil, zero value otherwise.

### GetResponseCookieOk

`func (o *MatchCriteria) GetResponseCookieOk() (*NameValuePair, bool)`

GetResponseCookieOk returns a tuple with the ResponseCookie field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseCookie

`func (o *MatchCriteria) SetResponseCookie(v NameValuePair)`

SetResponseCookie sets ResponseCookie field to given value.

### HasResponseCookie

`func (o *MatchCriteria) HasResponseCookie() bool`

HasResponseCookie returns a boolean if a field has been set.

### GetJsonValid

`func (o *MatchCriteria) GetJsonValid() bool`

GetJsonValid returns the JsonValid field if non-nil, zero value otherwise.

### GetJsonValidOk

`func (o *MatchCriteria) GetJsonValidOk() (*bool, bool)`

GetJsonValidOk returns a tuple with the JsonValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonValid

`func (o *MatchCriteria) SetJsonValid(v bool)`

SetJsonValid sets JsonValid field to given value.

### HasJsonValid

`func (o *MatchCriteria) HasJsonValid() bool`

HasJsonValid returns a boolean if a field has been set.

### GetJsonPath

`func (o *MatchCriteria) GetJsonPath() string`

GetJsonPath returns the JsonPath field if non-nil, zero value otherwise.

### GetJsonPathOk

`func (o *MatchCriteria) GetJsonPathOk() (*string, bool)`

GetJsonPathOk returns a tuple with the JsonPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonPath

`func (o *MatchCriteria) SetJsonPath(v string)`

SetJsonPath sets JsonPath field to given value.

### HasJsonPath

`func (o *MatchCriteria) HasJsonPath() bool`

HasJsonPath returns a boolean if a field has been set.

### GetJsonSchema

`func (o *MatchCriteria) GetJsonSchema() string`

GetJsonSchema returns the JsonSchema field if non-nil, zero value otherwise.

### GetJsonSchemaOk

`func (o *MatchCriteria) GetJsonSchemaOk() (*string, bool)`

GetJsonSchemaOk returns a tuple with the JsonSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonSchema

`func (o *MatchCriteria) SetJsonSchema(v string)`

SetJsonSchema sets JsonSchema field to given value.

### HasJsonSchema

`func (o *MatchCriteria) HasJsonSchema() bool`

HasJsonSchema returns a boolean if a field has been set.

### GetErrorIfNoTraffic

`func (o *MatchCriteria) GetErrorIfNoTraffic() bool`

GetErrorIfNoTraffic returns the ErrorIfNoTraffic field if non-nil, zero value otherwise.

### GetErrorIfNoTrafficOk

`func (o *MatchCriteria) GetErrorIfNoTrafficOk() (*bool, bool)`

GetErrorIfNoTrafficOk returns a tuple with the ErrorIfNoTraffic field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorIfNoTraffic

`func (o *MatchCriteria) SetErrorIfNoTraffic(v bool)`

SetErrorIfNoTraffic sets ErrorIfNoTraffic field to given value.

### HasErrorIfNoTraffic

`func (o *MatchCriteria) HasErrorIfNoTraffic() bool`

HasErrorIfNoTraffic returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


