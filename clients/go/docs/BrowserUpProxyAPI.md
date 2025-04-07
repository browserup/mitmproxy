# \BrowserUpProxyAPI

All URIs are relative to *http://localhost:48088*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddError**](BrowserUpProxyAPI.md#AddError) | **Post** /har/errors | 
[**AddMetric**](BrowserUpProxyAPI.md#AddMetric) | **Post** /har/metrics | 
[**GetHarLog**](BrowserUpProxyAPI.md#GetHarLog) | **Get** /har | 
[**Healthcheck**](BrowserUpProxyAPI.md#Healthcheck) | **Get** /healthcheck | 
[**NewPage**](BrowserUpProxyAPI.md#NewPage) | **Post** /har/page | 
[**ResetHarLog**](BrowserUpProxyAPI.md#ResetHarLog) | **Put** /har | 
[**VerifyNotPresent**](BrowserUpProxyAPI.md#VerifyNotPresent) | **Post** /verify/not_present/{name} | 
[**VerifyPresent**](BrowserUpProxyAPI.md#VerifyPresent) | **Post** /verify/present/{name} | 
[**VerifySLA**](BrowserUpProxyAPI.md#VerifySLA) | **Post** /verify/sla/{time}/{name} | 
[**VerifySize**](BrowserUpProxyAPI.md#VerifySize) | **Post** /verify/size/{size}/{name} | 



## AddError

> AddError(ctx).Error_(error_).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	error_ := *openapiclient.NewError() // Error | Receives an error to track. Internally, the error is stored in an array in the har under the _errors key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BrowserUpProxyAPI.AddError(context.Background()).Error_(error_).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.AddError``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddErrorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_** | [**Error**](Error.md) | Receives an error to track. Internally, the error is stored in an array in the har under the _errors key | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AddMetric

> AddMetric(ctx).Metric(metric).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	metric := *openapiclient.NewMetric() // Metric | Receives a new metric to add. The metric is stored, under the hood, in an array in the har under the _metrics key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BrowserUpProxyAPI.AddMetric(context.Background()).Metric(metric).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.AddMetric``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddMetricRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | [**Metric**](Metric.md) | Receives a new metric to add. The metric is stored, under the hood, in an array in the har under the _metrics key | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHarLog

> Har GetHarLog(ctx).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.GetHarLog(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.GetHarLog``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHarLog`: Har
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.GetHarLog`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetHarLogRequest struct via the builder pattern


### Return type

[**Har**](Har.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Healthcheck

> Healthcheck(ctx).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BrowserUpProxyAPI.Healthcheck(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.Healthcheck``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiHealthcheckRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NewPage

> Har NewPage(ctx, title).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	title := "title_example" // string | The unique title for this har page/step.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.NewPage(context.Background(), title).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.NewPage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `NewPage`: Har
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.NewPage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**title** | **string** | The unique title for this har page/step. | 

### Other Parameters

Other parameters are passed through a pointer to a apiNewPageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Har**](Har.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ResetHarLog

> Har ResetHarLog(ctx).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.ResetHarLog(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.ResetHarLog``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ResetHarLog`: Har
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.ResetHarLog`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiResetHarLogRequest struct via the builder pattern


### Return type

[**Har**](Har.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VerifyNotPresent

> VerifyResult VerifyNotPresent(ctx, name).MatchCriteria(matchCriteria).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	name := "name_example" // string | The unique name for this verification operation
	matchCriteria := *openapiclient.NewMatchCriteria() // MatchCriteria | Match criteria to select requests - response pairs for size tests

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.VerifyNotPresent(context.Background(), name).MatchCriteria(matchCriteria).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.VerifyNotPresent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VerifyNotPresent`: VerifyResult
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.VerifyNotPresent`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | The unique name for this verification operation | 

### Other Parameters

Other parameters are passed through a pointer to a apiVerifyNotPresentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **matchCriteria** | [**MatchCriteria**](MatchCriteria.md) | Match criteria to select requests - response pairs for size tests | 

### Return type

[**VerifyResult**](VerifyResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VerifyPresent

> VerifyResult VerifyPresent(ctx, name).MatchCriteria(matchCriteria).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	name := "name_example" // string | The unique name for this verification operation
	matchCriteria := *openapiclient.NewMatchCriteria() // MatchCriteria | Match criteria to select requests - response pairs for size tests

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.VerifyPresent(context.Background(), name).MatchCriteria(matchCriteria).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.VerifyPresent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VerifyPresent`: VerifyResult
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.VerifyPresent`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**name** | **string** | The unique name for this verification operation | 

### Other Parameters

Other parameters are passed through a pointer to a apiVerifyPresentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **matchCriteria** | [**MatchCriteria**](MatchCriteria.md) | Match criteria to select requests - response pairs for size tests | 

### Return type

[**VerifyResult**](VerifyResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VerifySLA

> VerifyResult VerifySLA(ctx, time, name).MatchCriteria(matchCriteria).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	time := int32(56) // int32 | The time used for comparison
	name := "name_example" // string | The unique name for this verification operation
	matchCriteria := *openapiclient.NewMatchCriteria() // MatchCriteria | Match criteria to select requests - response pairs for size tests

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.VerifySLA(context.Background(), time, name).MatchCriteria(matchCriteria).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.VerifySLA``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VerifySLA`: VerifyResult
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.VerifySLA`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**time** | **int32** | The time used for comparison | 
**name** | **string** | The unique name for this verification operation | 

### Other Parameters

Other parameters are passed through a pointer to a apiVerifySLARequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **matchCriteria** | [**MatchCriteria**](MatchCriteria.md) | Match criteria to select requests - response pairs for size tests | 

### Return type

[**VerifyResult**](VerifyResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VerifySize

> VerifyResult VerifySize(ctx, size, name).MatchCriteria(matchCriteria).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	size := int32(56) // int32 | The size used for comparison, in kilobytes
	name := "name_example" // string | The unique name for this verification operation
	matchCriteria := *openapiclient.NewMatchCriteria() // MatchCriteria | Match criteria to select requests - response pairs for size tests

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserUpProxyAPI.VerifySize(context.Background(), size, name).MatchCriteria(matchCriteria).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserUpProxyAPI.VerifySize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VerifySize`: VerifyResult
	fmt.Fprintf(os.Stdout, "Response from `BrowserUpProxyAPI.VerifySize`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**size** | **int32** | The size used for comparison, in kilobytes | 
**name** | **string** | The unique name for this verification operation | 

### Other Parameters

Other parameters are passed through a pointer to a apiVerifySizeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **matchCriteria** | [**MatchCriteria**](MatchCriteria.md) | Match criteria to select requests - response pairs for size tests | 

### Return type

[**VerifyResult**](VerifyResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

