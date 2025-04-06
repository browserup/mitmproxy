This is a customized fork of the mitmproxy project, maintained by a company named browserup. The mitmproxy 
is used to man-in-the-middle connections to provide debugging info, allow for security research
and other uses.

The Browserup proxy fork uses a variation of the mitmproxy's "mitmdump" (no UI) mode  to capture traffic from within containers that are run during a load test. 
This captured traffic, captured through mitmproxy addons, is 
used to build a HAR (HTTP Archive) file. The HAR file is made available via an API. The HAR also gets decorated with custom data, which start with an underscore.

The proxy offers an API that is also used to control the proxy, and to add custom metrics to a har at runtime, as well as adding verifications for HAR 
content. Clients for this API are generated in multiple languages via the open api specification.  The clients live in /clients which should be ignored, as 
they are generated files. 

Unusually, the schema .json files are regenerated when the tests are run. The definitions of the schemas are in mitmproxy/addons/browserup/har/har_schemas.py.
They are defined in marshmallow.

The Browserup proxy extends mitmproxy's mitmdump executable with addons. The most important code for browserup lives in the subfolder mitmproxy/addons/browserup.
It is implemented almost entirely by changes and additions to addons. It is undesirable to change files outside of this path, and the corresponding test path, as that
makes it difficult to take merges from the upstream mitmproxy project. 

It is also ok to change items in the subfolder mitmproxy/tools/browserup_proxy.py as new
addons are added. This is where they are loaded.