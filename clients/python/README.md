# BrowserUpMitmProxyClient
___
This is the REST API for controlling the BrowserUp MitmProxy.
The BrowserUp MitmProxy is a swiss army knife for automated testing that
captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests.
___


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.25
- Package version: 1.0.1
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import BrowserUpMitmProxyClient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import BrowserUpMitmProxyClient
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import BrowserUpMitmProxyClient
from BrowserUpMitmProxyClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:48088
# See configuration.py for a list of all supported configuration parameters.
configuration = BrowserUpMitmProxyClient.Configuration(
    host = "http://localhost:48088"
)



# Enter a context with an instance of the API client
with BrowserUpMitmProxyClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = BrowserUpMitmProxyClient.BrowserUpProxyApi(api_client)
    error = BrowserUpMitmProxyClient.Error() # Error | Receives an error to track. Internally, the error is stored in an array in the har under the _errors key

    try:
        api_instance.add_error(error)
    except ApiException as e:
        print("Exception when calling BrowserUpProxyApi->add_error: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:48088*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrowserUpProxyApi* | [**add_error**](docs/BrowserUpProxyApi.md#add_error) | **POST** /har/errors | 
*BrowserUpProxyApi* | [**add_metric**](docs/BrowserUpProxyApi.md#add_metric) | **POST** /har/metrics | 
*BrowserUpProxyApi* | [**get_har_log**](docs/BrowserUpProxyApi.md#get_har_log) | **GET** /har | 
*BrowserUpProxyApi* | [**healthcheck**](docs/BrowserUpProxyApi.md#healthcheck) | **GET** /healthcheck | 
*BrowserUpProxyApi* | [**new_page**](docs/BrowserUpProxyApi.md#new_page) | **POST** /har/page | 
*BrowserUpProxyApi* | [**reset_har_log**](docs/BrowserUpProxyApi.md#reset_har_log) | **PUT** /har | 
*BrowserUpProxyApi* | [**verify_not_present**](docs/BrowserUpProxyApi.md#verify_not_present) | **POST** /verify/not_present/{name} | 
*BrowserUpProxyApi* | [**verify_present**](docs/BrowserUpProxyApi.md#verify_present) | **POST** /verify/present/{name} | 
*BrowserUpProxyApi* | [**verify_size**](docs/BrowserUpProxyApi.md#verify_size) | **POST** /verify/size/{size}/{name} | 
*BrowserUpProxyApi* | [**verify_sla**](docs/BrowserUpProxyApi.md#verify_sla) | **POST** /verify/sla/{time}/{name} | 


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


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

developers@browserup.com


