#!/bin/bash

# requires openapi-generator installed and accessible in your PATH

DIR="$(dirname "${BASH_SOURCE[0]}")"
SCHEMA="${DIR}/../browserup-proxy.schema.json"

# Generate Markdown documentation
rm -rf markdown && openapi-generator generate \
    -g markdown -i "${SCHEMA}" \
    -o markdown

# Generate C# (.NET Core) client
rm -rf csharp && openapi-generator generate \
    --package-name BrowserUpMitmProxyClient \
    -g csharp-netcore -i "${SCHEMA}" \
    -o csharp -c config-csharp.yaml

# Generate Java client
rm -rf java && openapi-generator generate \
    --package-name BrowserUpMitmProxyClient \
    -g java -i "${SCHEMA}" \
    -o java -c config-java.yaml

# Generate JavaScript client
rm -rf javascript && openapi-generator generate \
    --package-name BrowserUpMitmProxyClient \
    -g javascript -i "${SCHEMA}" \
    -o javascript -c config-javascript.yaml

# Generate Python client
rm -rf python && openapi-generator generate \
    --package-name BrowserUpMitmProxyClient \
    -g python -i "${SCHEMA}" \
    -o python -c config-python.yaml

# Generate Ruby client
rm -rf ruby && openapi-generator generate \
    --package-name BrowserUpMitmProxyClient \
    -g ruby -i "${SCHEMA}" \
    -o ruby -c config-ruby.yaml

./post-build-java-client.sh
