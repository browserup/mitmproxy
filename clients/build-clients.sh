#!/bin/bash

# requires openapi-generator-cli installed and accessible in your PATH

DIR="$(dirname "${BASH_SOURCE[0]}")"
SCHEMA="${DIR}/../browserup-proxy.schema.json"

# Generate Markdown documentation
rm -rf markdown && openapi-generator-cli generate \
    -g markdown -i "${SCHEMA}" \
    -o markdown

# Generate C# (.NET Core) client
rm -rf csharp && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g csharp -i "${SCHEMA}" \
    -o csharp -c config-csharp.yaml

# Generate Java client
rm -rf java && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g java -i "${SCHEMA}" \
    -o java -c config-java.yaml

# Generate JavaScript client
rm -rf javascript && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g javascript -i "${SCHEMA}" \
    -o javascript -c config-javascript.yaml

# Generate Python client
rm -rf python && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g python -i "${SCHEMA}" \
    -o python -c config-python.yaml

# Generate Ruby client
rm -rf ruby && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g ruby -i "${SCHEMA}" \
    -o ruby -c config-ruby.yaml

rm -rf ruby && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g ruby -i "${SCHEMA}" \
    -o ruby -c config-ruby.yaml

rm -rf go && openapi-generator-cli generate \
    --package-name BrowserUpMitmProxyClient \
    -g go -i "${SCHEMA}" \
    -o go -c config-go.yaml

./post-build-java-client.sh
