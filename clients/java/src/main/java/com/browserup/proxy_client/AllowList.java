/*
 * BrowserUp Proxy
 * ___ This is the REST API for controlling the BrowserUp Proxy.  The BrowserUp Proxy is a swiss army knife for automated testing. It allows traffic capture in HAR files and manipulation.  It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.browserup.proxy_client;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * AllowList
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen")
public class AllowList {
  public static final String SERIALIZED_NAME_STATUS_CODE = "status_code";
  @SerializedName(SERIALIZED_NAME_STATUS_CODE)
  private String statusCode;

  public static final String SERIALIZED_NAME_URL_PATTERN = "url_pattern";
  @SerializedName(SERIALIZED_NAME_URL_PATTERN)
  private String urlPattern;


  public AllowList statusCode(String statusCode) {
    
    this.statusCode = statusCode;
    return this;
  }

   /**
   * HTTP Status Code to match
   * @return statusCode
  **/
  @ApiModelProperty(required = true, value = "HTTP Status Code to match")

  public String getStatusCode() {
    return statusCode;
  }


  public void setStatusCode(String statusCode) {
    this.statusCode = statusCode;
  }


  public AllowList urlPattern(String urlPattern) {
    
    this.urlPattern = urlPattern;
    return this;
  }

   /**
   * URL Regex Pattern to match
   * @return urlPattern
  **/
  @ApiModelProperty(required = true, value = "URL Regex Pattern to match")

  public String getUrlPattern() {
    return urlPattern;
  }


  public void setUrlPattern(String urlPattern) {
    this.urlPattern = urlPattern;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AllowList allowList = (AllowList) o;
    return Objects.equals(this.statusCode, allowList.statusCode) &&
        Objects.equals(this.urlPattern, allowList.urlPattern);
  }

  @Override
  public int hashCode() {
    return Objects.hash(statusCode, urlPattern);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AllowList {\n");
    sb.append("    statusCode: ").append(toIndentedString(statusCode)).append("\n");
    sb.append("    urlPattern: ").append(toIndentedString(urlPattern)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
