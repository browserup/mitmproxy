/*
 * BrowserUp MitmProxy
 * ___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.24
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.browserup.proxy_client;

import java.util.Objects;
import java.util.Arrays;
import com.browserup.proxy_client.HarEntryRequestCookiesInner;
import com.browserup.proxy_client.HarEntryResponseContent;
import com.browserup.proxy_client.Header;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import com.browserup.proxy_client.JSON;

/**
 * HarEntryResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen")
public class HarEntryResponse {
  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private Integer status;

  public static final String SERIALIZED_NAME_STATUS_TEXT = "statusText";
  @SerializedName(SERIALIZED_NAME_STATUS_TEXT)
  private String statusText;

  public static final String SERIALIZED_NAME_HTTP_VERSION = "httpVersion";
  @SerializedName(SERIALIZED_NAME_HTTP_VERSION)
  private String httpVersion;

  public static final String SERIALIZED_NAME_COOKIES = "cookies";
  @SerializedName(SERIALIZED_NAME_COOKIES)
  private List<HarEntryRequestCookiesInner> cookies = new ArrayList<>();

  public static final String SERIALIZED_NAME_HEADERS = "headers";
  @SerializedName(SERIALIZED_NAME_HEADERS)
  private List<Header> headers = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONTENT = "content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private HarEntryResponseContent content;

  public static final String SERIALIZED_NAME_REDIRECT_U_R_L = "redirectURL";
  @SerializedName(SERIALIZED_NAME_REDIRECT_U_R_L)
  private String redirectURL;

  public static final String SERIALIZED_NAME_HEADERS_SIZE = "headersSize";
  @SerializedName(SERIALIZED_NAME_HEADERS_SIZE)
  private Integer headersSize;

  public static final String SERIALIZED_NAME_BODY_SIZE = "bodySize";
  @SerializedName(SERIALIZED_NAME_BODY_SIZE)
  private Integer bodySize;

  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public HarEntryResponse() {
  }

  public HarEntryResponse status(Integer status) {
    
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @javax.annotation.Nonnull

  public Integer getStatus() {
    return status;
  }


  public void setStatus(Integer status) {
    this.status = status;
  }


  public HarEntryResponse statusText(String statusText) {
    
    this.statusText = statusText;
    return this;
  }

   /**
   * Get statusText
   * @return statusText
  **/
  @javax.annotation.Nonnull

  public String getStatusText() {
    return statusText;
  }


  public void setStatusText(String statusText) {
    this.statusText = statusText;
  }


  public HarEntryResponse httpVersion(String httpVersion) {
    
    this.httpVersion = httpVersion;
    return this;
  }

   /**
   * Get httpVersion
   * @return httpVersion
  **/
  @javax.annotation.Nonnull

  public String getHttpVersion() {
    return httpVersion;
  }


  public void setHttpVersion(String httpVersion) {
    this.httpVersion = httpVersion;
  }


  public HarEntryResponse cookies(List<HarEntryRequestCookiesInner> cookies) {
    
    this.cookies = cookies;
    return this;
  }

  public HarEntryResponse addCookiesItem(HarEntryRequestCookiesInner cookiesItem) {
    this.cookies.add(cookiesItem);
    return this;
  }

   /**
   * Get cookies
   * @return cookies
  **/
  @javax.annotation.Nonnull

  public List<HarEntryRequestCookiesInner> getCookies() {
    return cookies;
  }


  public void setCookies(List<HarEntryRequestCookiesInner> cookies) {
    this.cookies = cookies;
  }


  public HarEntryResponse headers(List<Header> headers) {
    
    this.headers = headers;
    return this;
  }

  public HarEntryResponse addHeadersItem(Header headersItem) {
    this.headers.add(headersItem);
    return this;
  }

   /**
   * Get headers
   * @return headers
  **/
  @javax.annotation.Nonnull

  public List<Header> getHeaders() {
    return headers;
  }


  public void setHeaders(List<Header> headers) {
    this.headers = headers;
  }


  public HarEntryResponse content(HarEntryResponseContent content) {
    
    this.content = content;
    return this;
  }

   /**
   * Get content
   * @return content
  **/
  @javax.annotation.Nonnull

  public HarEntryResponseContent getContent() {
    return content;
  }


  public void setContent(HarEntryResponseContent content) {
    this.content = content;
  }


  public HarEntryResponse redirectURL(String redirectURL) {
    
    this.redirectURL = redirectURL;
    return this;
  }

   /**
   * Get redirectURL
   * @return redirectURL
  **/
  @javax.annotation.Nonnull

  public String getRedirectURL() {
    return redirectURL;
  }


  public void setRedirectURL(String redirectURL) {
    this.redirectURL = redirectURL;
  }


  public HarEntryResponse headersSize(Integer headersSize) {
    
    this.headersSize = headersSize;
    return this;
  }

   /**
   * Get headersSize
   * @return headersSize
  **/
  @javax.annotation.Nonnull

  public Integer getHeadersSize() {
    return headersSize;
  }


  public void setHeadersSize(Integer headersSize) {
    this.headersSize = headersSize;
  }


  public HarEntryResponse bodySize(Integer bodySize) {
    
    this.bodySize = bodySize;
    return this;
  }

   /**
   * Get bodySize
   * @return bodySize
  **/
  @javax.annotation.Nonnull

  public Integer getBodySize() {
    return bodySize;
  }


  public void setBodySize(Integer bodySize) {
    this.bodySize = bodySize;
  }


  public HarEntryResponse comment(String comment) {
    
    this.comment = comment;
    return this;
  }

   /**
   * Get comment
   * @return comment
  **/
  @javax.annotation.Nullable

  public String getComment() {
    return comment;
  }


  public void setComment(String comment) {
    this.comment = comment;
  }

  /**
   * A container for additional, undeclared properties.
   * This is a holder for any undeclared properties as specified with
   * the 'additionalProperties' keyword in the OAS document.
   */
  private Map<String, Object> additionalProperties;

  /**
   * Set the additional (undeclared) property with the specified name and value.
   * If the property does not already exist, create it otherwise replace it.
   *
   * @param key name of the property
   * @param value value of the property
   * @return the HarEntryResponse instance itself
   */
  public HarEntryResponse putAdditionalProperty(String key, Object value) {
    if (this.additionalProperties == null) {
        this.additionalProperties = new HashMap<String, Object>();
    }
    this.additionalProperties.put(key, value);
    return this;
  }

  /**
   * Return the additional (undeclared) property.
   *
   * @return a map of objects
   */
  public Map<String, Object> getAdditionalProperties() {
    return additionalProperties;
  }

  /**
   * Return the additional (undeclared) property with the specified name.
   *
   * @param key name of the property
   * @return an object
   */
  public Object getAdditionalProperty(String key) {
    if (this.additionalProperties == null) {
        return null;
    }
    return this.additionalProperties.get(key);
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HarEntryResponse harEntryResponse = (HarEntryResponse) o;
    return Objects.equals(this.status, harEntryResponse.status) &&
        Objects.equals(this.statusText, harEntryResponse.statusText) &&
        Objects.equals(this.httpVersion, harEntryResponse.httpVersion) &&
        Objects.equals(this.cookies, harEntryResponse.cookies) &&
        Objects.equals(this.headers, harEntryResponse.headers) &&
        Objects.equals(this.content, harEntryResponse.content) &&
        Objects.equals(this.redirectURL, harEntryResponse.redirectURL) &&
        Objects.equals(this.headersSize, harEntryResponse.headersSize) &&
        Objects.equals(this.bodySize, harEntryResponse.bodySize) &&
        Objects.equals(this.comment, harEntryResponse.comment)&&
        Objects.equals(this.additionalProperties, harEntryResponse.additionalProperties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(status, statusText, httpVersion, cookies, headers, content, redirectURL, headersSize, bodySize, comment, additionalProperties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HarEntryResponse {\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusText: ").append(toIndentedString(statusText)).append("\n");
    sb.append("    httpVersion: ").append(toIndentedString(httpVersion)).append("\n");
    sb.append("    cookies: ").append(toIndentedString(cookies)).append("\n");
    sb.append("    headers: ").append(toIndentedString(headers)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    redirectURL: ").append(toIndentedString(redirectURL)).append("\n");
    sb.append("    headersSize: ").append(toIndentedString(headersSize)).append("\n");
    sb.append("    bodySize: ").append(toIndentedString(bodySize)).append("\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    additionalProperties: ").append(toIndentedString(additionalProperties)).append("\n");
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


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("status");
    openapiFields.add("statusText");
    openapiFields.add("httpVersion");
    openapiFields.add("cookies");
    openapiFields.add("headers");
    openapiFields.add("content");
    openapiFields.add("redirectURL");
    openapiFields.add("headersSize");
    openapiFields.add("bodySize");
    openapiFields.add("comment");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("statusText");
    openapiRequiredFields.add("httpVersion");
    openapiRequiredFields.add("cookies");
    openapiRequiredFields.add("headers");
    openapiRequiredFields.add("content");
    openapiRequiredFields.add("redirectURL");
    openapiRequiredFields.add("headersSize");
    openapiRequiredFields.add("bodySize");
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to HarEntryResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (!HarEntryResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON object is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HarEntryResponse is not found in the empty JSON string", HarEntryResponse.openapiRequiredFields.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HarEntryResponse.openapiRequiredFields) {
        if (jsonObj.get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonObj.toString()));
        }
      }
      if (!jsonObj.get("statusText").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `statusText` to be a primitive type in the JSON string but got `%s`", jsonObj.get("statusText").toString()));
      }
      if (!jsonObj.get("httpVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `httpVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("httpVersion").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("cookies").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `cookies` to be an array in the JSON string but got `%s`", jsonObj.get("cookies").toString()));
      }

      JsonArray jsonArraycookies = jsonObj.getAsJsonArray("cookies");
      // validate the required field `cookies` (array)
      for (int i = 0; i < jsonArraycookies.size(); i++) {
        HarEntryRequestCookiesInner.validateJsonObject(jsonArraycookies.get(i).getAsJsonObject());
      };
      // ensure the json data is an array
      if (!jsonObj.get("headers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `headers` to be an array in the JSON string but got `%s`", jsonObj.get("headers").toString()));
      }

      JsonArray jsonArrayheaders = jsonObj.getAsJsonArray("headers");
      // validate the required field `headers` (array)
      for (int i = 0; i < jsonArrayheaders.size(); i++) {
        Header.validateJsonObject(jsonArrayheaders.get(i).getAsJsonObject());
      };
      // validate the required field `content`
      HarEntryResponseContent.validateJsonObject(jsonObj.getAsJsonObject("content"));
      if (!jsonObj.get("redirectURL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `redirectURL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("redirectURL").toString()));
      }
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HarEntryResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HarEntryResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HarEntryResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HarEntryResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<HarEntryResponse>() {
           @Override
           public void write(JsonWriter out, HarEntryResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             obj.remove("additionalProperties");
             // serialize additional properties
             if (value.getAdditionalProperties() != null) {
               for (Map.Entry<String, Object> entry : value.getAdditionalProperties().entrySet()) {
                 if (entry.getValue() instanceof String)
                   obj.addProperty(entry.getKey(), (String) entry.getValue());
                 else if (entry.getValue() instanceof Number)
                   obj.addProperty(entry.getKey(), (Number) entry.getValue());
                 else if (entry.getValue() instanceof Boolean)
                   obj.addProperty(entry.getKey(), (Boolean) entry.getValue());
                 else if (entry.getValue() instanceof Character)
                   obj.addProperty(entry.getKey(), (Character) entry.getValue());
                 else {
                   obj.add(entry.getKey(), gson.toJsonTree(entry.getValue()).getAsJsonObject());
                 }
               }
             }
             elementAdapter.write(out, obj);
           }

           @Override
           public HarEntryResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             // store additional fields in the deserialized instance
             HarEntryResponse instance = thisAdapter.fromJsonTree(jsonObj);
             for (Map.Entry<String, JsonElement> entry : jsonObj.entrySet()) {
               if (!openapiFields.contains(entry.getKey())) {
                 if (entry.getValue().isJsonPrimitive()) { // primitive type
                   if (entry.getValue().getAsJsonPrimitive().isString())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsString());
                   else if (entry.getValue().getAsJsonPrimitive().isNumber())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsNumber());
                   else if (entry.getValue().getAsJsonPrimitive().isBoolean())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsBoolean());
                   else
                     throw new IllegalArgumentException(String.format("The field `%s` has unknown primitive type. Value: %s", entry.getKey(), entry.getValue().toString()));
                 } else if (entry.getValue().isJsonArray()) {
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), List.class));
                 } else { // JSON object
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), HashMap.class));
                 }
               }
             }
             return instance;
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of HarEntryResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of HarEntryResponse
  * @throws IOException if the JSON string is invalid with respect to HarEntryResponse
  */
  public static HarEntryResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HarEntryResponse.class);
  }

 /**
  * Convert an instance of HarEntryResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

