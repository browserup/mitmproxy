# BrowserUp.Mitmproxy.Client - the C# library for the BrowserUp MitmProxy

___
This is the REST API for controlling the BrowserUp MitmProxy.
The BrowserUp MitmProxy is a swiss army knife for automated testing that
captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests.
___


This C# SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- SDK version: 1.0.0
- Build package: org.openapitools.codegen.languages.CSharpNetCoreClientCodegen

<a id="frameworks-supported"></a>
## Frameworks supported

<a id="dependencies"></a>
## Dependencies

- [RestSharp](https://www.nuget.org/packages/RestSharp) - 106.13.0 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 13.0.2 or later
- [JsonSubTypes](https://www.nuget.org/packages/JsonSubTypes/) - 1.8.0 or later
- [System.ComponentModel.Annotations](https://www.nuget.org/packages/System.ComponentModel.Annotations) - 5.0.0 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the packages:
```
Install-Package RestSharp
Install-Package Newtonsoft.Json
Install-Package JsonSubTypes
Install-Package System.ComponentModel.Annotations
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742).
NOTE: RestSharp for .Net Core creates a new socket for each api call, which can lead to a socket exhaustion problem. See [RestSharp#1406](https://github.com/restsharp/RestSharp/issues/1406).

<a id="installation"></a>
## Installation
Run the following command to generate the DLL
- [Mac/Linux] `/bin/sh build.sh`
- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:
```csharp
using BrowserUp.Mitmproxy.Client.Api;
using BrowserUp.Mitmproxy.Client.Client;
using BrowserUp.Mitmproxy.Client.Model;
```
<a id="packaging"></a>
## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package) and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package) packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj` directly:

```
nuget pack -Build -OutputDirectory out BrowserUp.Mitmproxy.Client.csproj
```

Then, publish to a [local feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and consume the new package via Nuget as usual.

<a id="usage"></a>
## Usage

To use the API client with a HTTP proxy, setup a `System.Net.WebProxy`
```csharp
Configuration c = new Configuration();
System.Net.WebProxy webProxy = new System.Net.WebProxy("http://myProxyUrl:80/");
webProxy.Credentials = System.Net.CredentialCache.DefaultCredentials;
c.Proxy = webProxy;
```

<a id="getting-started"></a>
## Getting Started

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using BrowserUp.Mitmproxy.Client.Api;
using BrowserUp.Mitmproxy.Client.Client;
using BrowserUp.Mitmproxy.Client.Model;

namespace Example
{
    public class Example
    {
        public static void Main()
        {

            Configuration config = new Configuration();
            config.BasePath = "http://localhost:48088";
            var apiInstance = new BrowserUpProxyApi(config);
            var counter = new Counter(); // Counter | Receives a new counter to add. The counter is stored, under the hood, in an array in the har under the _counters key

            try
            {
                apiInstance.AddCounter(counter);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling BrowserUpProxyApi.AddCounter: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }

        }
    }
}
```

<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost:48088*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrowserUpProxyApi* | [**AddCounter**](docs/BrowserUpProxyApi.md#addcounter) | **POST** /har/counters | 
*BrowserUpProxyApi* | [**AddError**](docs/BrowserUpProxyApi.md#adderror) | **POST** /har/errors | 
*BrowserUpProxyApi* | [**GetHarLog**](docs/BrowserUpProxyApi.md#getharlog) | **GET** /har | 
*BrowserUpProxyApi* | [**Healthcheck**](docs/BrowserUpProxyApi.md#healthcheck) | **GET** /healthcheck | 
*BrowserUpProxyApi* | [**NewPage**](docs/BrowserUpProxyApi.md#newpage) | **POST** /har/page | 
*BrowserUpProxyApi* | [**ResetHarLog**](docs/BrowserUpProxyApi.md#resetharlog) | **PUT** /har | 
*BrowserUpProxyApi* | [**VerifyNotPresent**](docs/BrowserUpProxyApi.md#verifynotpresent) | **POST** /verify/not_present/{name} | 
*BrowserUpProxyApi* | [**VerifyPresent**](docs/BrowserUpProxyApi.md#verifypresent) | **POST** /verify/present/{name} | 
*BrowserUpProxyApi* | [**VerifySLA**](docs/BrowserUpProxyApi.md#verifysla) | **POST** /verify/sla/{time}/{name} | 
*BrowserUpProxyApi* | [**VerifySize**](docs/BrowserUpProxyApi.md#verifysize) | **POST** /verify/size/{size}/{name} | 


<a id="documentation-for-models"></a>
## Documentation for Models

 - [Model.Counter](docs/Counter.md)
 - [Model.Error](docs/Error.md)
 - [Model.Har](docs/Har.md)
 - [Model.HarEntry](docs/HarEntry.md)
 - [Model.HarEntryCache](docs/HarEntryCache.md)
 - [Model.HarEntryCacheBeforeRequest](docs/HarEntryCacheBeforeRequest.md)
 - [Model.HarEntryCacheBeforeRequestOneOf](docs/HarEntryCacheBeforeRequestOneOf.md)
 - [Model.HarEntryRequest](docs/HarEntryRequest.md)
 - [Model.HarEntryRequestCookiesInner](docs/HarEntryRequestCookiesInner.md)
 - [Model.HarEntryRequestPostData](docs/HarEntryRequestPostData.md)
 - [Model.HarEntryRequestPostDataParamsInner](docs/HarEntryRequestPostDataParamsInner.md)
 - [Model.HarEntryRequestQueryStringInner](docs/HarEntryRequestQueryStringInner.md)
 - [Model.HarEntryResponse](docs/HarEntryResponse.md)
 - [Model.HarEntryResponseContent](docs/HarEntryResponseContent.md)
 - [Model.HarEntryTimings](docs/HarEntryTimings.md)
 - [Model.HarLog](docs/HarLog.md)
 - [Model.HarLogCreator](docs/HarLogCreator.md)
 - [Model.Header](docs/Header.md)
 - [Model.LargestContentfulPaint](docs/LargestContentfulPaint.md)
 - [Model.MatchCriteria](docs/MatchCriteria.md)
 - [Model.MatchCriteriaRequestHeader](docs/MatchCriteriaRequestHeader.md)
 - [Model.NameValuePair](docs/NameValuePair.md)
 - [Model.Page](docs/Page.md)
 - [Model.PageTiming](docs/PageTiming.md)
 - [Model.PageTimings](docs/PageTimings.md)
 - [Model.VerifyResult](docs/VerifyResult.md)
 - [Model.WebSocketMessage](docs/WebSocketMessage.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.

