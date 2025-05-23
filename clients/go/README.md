# Go API client for BrowserUpMitmProxyClient

___
This is the REST API for controlling the BrowserUp MitmProxy.
The BrowserUp MitmProxy is a swiss army knife for automated testing that
captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests.
___


## Overview
This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [OpenAPI-spec](https://www.openapis.org/) from a remote server, you can easily generate an API client.

- API version: 1.25
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.GoClientCodegen

## Installation

Install the following dependencies:

```sh
go get github.com/stretchr/testify/assert
go get golang.org/x/net/context
```

Put the package under your project folder and add the following in import:

```go
import BrowserUpMitmProxyClient "github.com/GIT_USER_ID/GIT_REPO_ID"
```

To use a proxy, set the environment variable `HTTP_PROXY`:

```go
os.Setenv("HTTP_PROXY", "http://proxy_name:proxy_port")
```

## Configuration of Server URL

Default configuration comes with `Servers` field that contains server objects as defined in the OpenAPI specification.

### Select Server Configuration

For using other server than the one defined on index 0 set context value `BrowserUpMitmProxyClient.ContextServerIndex` of type `int`.

```go
ctx := context.WithValue(context.Background(), BrowserUpMitmProxyClient.ContextServerIndex, 1)
```

### Templated Server URL

Templated server URL is formatted using default variables from configuration or from context value `BrowserUpMitmProxyClient.ContextServerVariables` of type `map[string]string`.

```go
ctx := context.WithValue(context.Background(), BrowserUpMitmProxyClient.ContextServerVariables, map[string]string{
	"basePath": "v2",
})
```

Note, enum values are always validated and all unused variables are silently ignored.

### URLs Configuration per Operation

Each operation can use different server URL defined using `OperationServers` map in the `Configuration`.
An operation is uniquely identified by `"{classname}Service.{nickname}"` string.
Similar rules for overriding default operation server index and variables applies by using `BrowserUpMitmProxyClient.ContextOperationServerIndices` and `BrowserUpMitmProxyClient.ContextOperationServerVariables` context maps.

```go
ctx := context.WithValue(context.Background(), BrowserUpMitmProxyClient.ContextOperationServerIndices, map[string]int{
	"{classname}Service.{nickname}": 2,
})
ctx = context.WithValue(context.Background(), BrowserUpMitmProxyClient.ContextOperationServerVariables, map[string]map[string]string{
	"{classname}Service.{nickname}": {
		"port": "8443",
	},
})
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:48088*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrowserUpProxyAPI* | [**AddError**](docs/BrowserUpProxyAPI.md#adderror) | **Post** /har/errors | 
*BrowserUpProxyAPI* | [**AddMetric**](docs/BrowserUpProxyAPI.md#addmetric) | **Post** /har/metrics | 
*BrowserUpProxyAPI* | [**GetHarLog**](docs/BrowserUpProxyAPI.md#getharlog) | **Get** /har | 
*BrowserUpProxyAPI* | [**Healthcheck**](docs/BrowserUpProxyAPI.md#healthcheck) | **Get** /healthcheck | 
*BrowserUpProxyAPI* | [**NewPage**](docs/BrowserUpProxyAPI.md#newpage) | **Post** /har/page | 
*BrowserUpProxyAPI* | [**ResetHarLog**](docs/BrowserUpProxyAPI.md#resetharlog) | **Put** /har | 
*BrowserUpProxyAPI* | [**VerifyNotPresent**](docs/BrowserUpProxyAPI.md#verifynotpresent) | **Post** /verify/not_present/{name} | 
*BrowserUpProxyAPI* | [**VerifyPresent**](docs/BrowserUpProxyAPI.md#verifypresent) | **Post** /verify/present/{name} | 
*BrowserUpProxyAPI* | [**VerifySLA**](docs/BrowserUpProxyAPI.md#verifysla) | **Post** /verify/sla/{time}/{name} | 
*BrowserUpProxyAPI* | [**VerifySize**](docs/BrowserUpProxyAPI.md#verifysize) | **Post** /verify/size/{size}/{name} | 


## Documentation For Models

 - [Action](docs/Action.md)
 - [Error](docs/Error.md)
 - [Har](docs/Har.md)
 - [HarEntry](docs/HarEntry.md)
 - [HarEntryCache](docs/HarEntryCache.md)
 - [HarEntryCacheBeforeRequest](docs/HarEntryCacheBeforeRequest.md)
 - [HarEntryRequest](docs/HarEntryRequest.md)
 - [HarEntryRequestCookiesInner](docs/HarEntryRequestCookiesInner.md)
 - [HarEntryRequestPostData](docs/HarEntryRequestPostData.md)
 - [HarEntryRequestPostDataParamsInner](docs/HarEntryRequestPostDataParamsInner.md)
 - [HarEntryRequestQueryStringInner](docs/HarEntryRequestQueryStringInner.md)
 - [HarEntryResponse](docs/HarEntryResponse.md)
 - [HarEntryResponseContent](docs/HarEntryResponseContent.md)
 - [HarEntryTimings](docs/HarEntryTimings.md)
 - [HarLog](docs/HarLog.md)
 - [HarLogCreator](docs/HarLogCreator.md)
 - [Header](docs/Header.md)
 - [LargestContentfulPaint](docs/LargestContentfulPaint.md)
 - [MatchCriteria](docs/MatchCriteria.md)
 - [Metric](docs/Metric.md)
 - [NameValuePair](docs/NameValuePair.md)
 - [Page](docs/Page.md)
 - [PageTiming](docs/PageTiming.md)
 - [PageTimings](docs/PageTimings.md)
 - [VerifyResult](docs/VerifyResult.md)
 - [WebSocketMessage](docs/WebSocketMessage.md)


## Documentation For Authorization

Endpoints do not require authorization.


## Documentation for Utility Methods

Due to the fact that model structure members are all pointers, this package contains
a number of utility functions to easily obtain pointers to values of basic types.
Each of these functions takes a value of the given basic type and returns a pointer to it:

* `PtrBool`
* `PtrInt`
* `PtrInt32`
* `PtrInt64`
* `PtrFloat`
* `PtrFloat32`
* `PtrFloat64`
* `PtrString`
* `PtrTime`

## Author



