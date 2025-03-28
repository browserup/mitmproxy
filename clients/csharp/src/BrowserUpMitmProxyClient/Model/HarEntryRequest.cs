/*
 * BrowserUp MitmProxy
 *
 * ___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.24
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = BrowserUpMitmProxyClient.Client.OpenAPIDateConverter;

namespace BrowserUpMitmProxyClient.Model
{
    /// <summary>
    /// HarEntryRequest
    /// </summary>
    [DataContract(Name = "HarEntry_request")]
    public partial class HarEntryRequest : Dictionary<String, Object>, IEquatable<HarEntryRequest>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryRequest" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected HarEntryRequest()
        {
            this.AdditionalProperties = new Dictionary<string, object>();
        }
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryRequest" /> class.
        /// </summary>
        /// <param name="method">method (required).</param>
        /// <param name="url">url (required).</param>
        /// <param name="httpVersion">httpVersion (required).</param>
        /// <param name="cookies">cookies (required).</param>
        /// <param name="headers">headers (required).</param>
        /// <param name="queryString">queryString (required).</param>
        /// <param name="postData">postData.</param>
        /// <param name="headersSize">headersSize (required).</param>
        /// <param name="bodySize">bodySize (required).</param>
        /// <param name="comment">comment.</param>
        public HarEntryRequest(string method = default(string), string url = default(string), string httpVersion = default(string), List<HarEntryRequestCookiesInner> cookies = default(List<HarEntryRequestCookiesInner>), List<Header> headers = default(List<Header>), List<HarEntryRequestQueryStringInner> queryString = default(List<HarEntryRequestQueryStringInner>), HarEntryRequestPostData postData = default(HarEntryRequestPostData), int headersSize = default(int), int bodySize = default(int), string comment = default(string)) : base()
        {
            // to ensure "method" is required (not null)
            if (method == null)
            {
                throw new ArgumentNullException("method is a required property for HarEntryRequest and cannot be null");
            }
            this.Method = method;
            // to ensure "url" is required (not null)
            if (url == null)
            {
                throw new ArgumentNullException("url is a required property for HarEntryRequest and cannot be null");
            }
            this.Url = url;
            // to ensure "httpVersion" is required (not null)
            if (httpVersion == null)
            {
                throw new ArgumentNullException("httpVersion is a required property for HarEntryRequest and cannot be null");
            }
            this.HttpVersion = httpVersion;
            // to ensure "cookies" is required (not null)
            if (cookies == null)
            {
                throw new ArgumentNullException("cookies is a required property for HarEntryRequest and cannot be null");
            }
            this.Cookies = cookies;
            // to ensure "headers" is required (not null)
            if (headers == null)
            {
                throw new ArgumentNullException("headers is a required property for HarEntryRequest and cannot be null");
            }
            this.Headers = headers;
            // to ensure "queryString" is required (not null)
            if (queryString == null)
            {
                throw new ArgumentNullException("queryString is a required property for HarEntryRequest and cannot be null");
            }
            this.QueryString = queryString;
            this.HeadersSize = headersSize;
            this.BodySize = bodySize;
            this.PostData = postData;
            this.Comment = comment;
            this.AdditionalProperties = new Dictionary<string, object>();
        }

        /// <summary>
        /// Gets or Sets Method
        /// </summary>
        [DataMember(Name = "method", IsRequired = true, EmitDefaultValue = true)]
        public string Method { get; set; }

        /// <summary>
        /// Gets or Sets Url
        /// </summary>
        [DataMember(Name = "url", IsRequired = true, EmitDefaultValue = true)]
        public string Url { get; set; }

        /// <summary>
        /// Gets or Sets HttpVersion
        /// </summary>
        [DataMember(Name = "httpVersion", IsRequired = true, EmitDefaultValue = true)]
        public string HttpVersion { get; set; }

        /// <summary>
        /// Gets or Sets Cookies
        /// </summary>
        [DataMember(Name = "cookies", IsRequired = true, EmitDefaultValue = true)]
        public List<HarEntryRequestCookiesInner> Cookies { get; set; }

        /// <summary>
        /// Gets or Sets Headers
        /// </summary>
        [DataMember(Name = "headers", IsRequired = true, EmitDefaultValue = true)]
        public List<Header> Headers { get; set; }

        /// <summary>
        /// Gets or Sets QueryString
        /// </summary>
        [DataMember(Name = "queryString", IsRequired = true, EmitDefaultValue = true)]
        public List<HarEntryRequestQueryStringInner> QueryString { get; set; }

        /// <summary>
        /// Gets or Sets PostData
        /// </summary>
        [DataMember(Name = "postData", EmitDefaultValue = false)]
        public HarEntryRequestPostData PostData { get; set; }

        /// <summary>
        /// Gets or Sets HeadersSize
        /// </summary>
        [DataMember(Name = "headersSize", IsRequired = true, EmitDefaultValue = true)]
        public int HeadersSize { get; set; }

        /// <summary>
        /// Gets or Sets BodySize
        /// </summary>
        [DataMember(Name = "bodySize", IsRequired = true, EmitDefaultValue = true)]
        public int BodySize { get; set; }

        /// <summary>
        /// Gets or Sets Comment
        /// </summary>
        [DataMember(Name = "comment", EmitDefaultValue = false)]
        public string Comment { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public IDictionary<string, object> AdditionalProperties { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class HarEntryRequest {\n");
            sb.Append("  ").Append(base.ToString().Replace("\n", "\n  ")).Append("\n");
            sb.Append("  Method: ").Append(Method).Append("\n");
            sb.Append("  Url: ").Append(Url).Append("\n");
            sb.Append("  HttpVersion: ").Append(HttpVersion).Append("\n");
            sb.Append("  Cookies: ").Append(Cookies).Append("\n");
            sb.Append("  Headers: ").Append(Headers).Append("\n");
            sb.Append("  QueryString: ").Append(QueryString).Append("\n");
            sb.Append("  PostData: ").Append(PostData).Append("\n");
            sb.Append("  HeadersSize: ").Append(HeadersSize).Append("\n");
            sb.Append("  BodySize: ").Append(BodySize).Append("\n");
            sb.Append("  Comment: ").Append(Comment).Append("\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as HarEntryRequest);
        }

        /// <summary>
        /// Returns true if HarEntryRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of HarEntryRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(HarEntryRequest input)
        {
            if (input == null)
            {
                return false;
            }
            return base.Equals(input) && 
                (
                    this.Method == input.Method ||
                    (this.Method != null &&
                    this.Method.Equals(input.Method))
                ) && base.Equals(input) && 
                (
                    this.Url == input.Url ||
                    (this.Url != null &&
                    this.Url.Equals(input.Url))
                ) && base.Equals(input) && 
                (
                    this.HttpVersion == input.HttpVersion ||
                    (this.HttpVersion != null &&
                    this.HttpVersion.Equals(input.HttpVersion))
                ) && base.Equals(input) && 
                (
                    this.Cookies == input.Cookies ||
                    this.Cookies != null &&
                    input.Cookies != null &&
                    this.Cookies.SequenceEqual(input.Cookies)
                ) && base.Equals(input) && 
                (
                    this.Headers == input.Headers ||
                    this.Headers != null &&
                    input.Headers != null &&
                    this.Headers.SequenceEqual(input.Headers)
                ) && base.Equals(input) && 
                (
                    this.QueryString == input.QueryString ||
                    this.QueryString != null &&
                    input.QueryString != null &&
                    this.QueryString.SequenceEqual(input.QueryString)
                ) && base.Equals(input) && 
                (
                    this.PostData == input.PostData ||
                    (this.PostData != null &&
                    this.PostData.Equals(input.PostData))
                ) && base.Equals(input) && 
                (
                    this.HeadersSize == input.HeadersSize ||
                    this.HeadersSize.Equals(input.HeadersSize)
                ) && base.Equals(input) && 
                (
                    this.BodySize == input.BodySize ||
                    this.BodySize.Equals(input.BodySize)
                ) && base.Equals(input) && 
                (
                    this.Comment == input.Comment ||
                    (this.Comment != null &&
                    this.Comment.Equals(input.Comment))
                )
                && (this.AdditionalProperties.Count == input.AdditionalProperties.Count && !this.AdditionalProperties.Except(input.AdditionalProperties).Any());
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = base.GetHashCode();
                if (this.Method != null)
                {
                    hashCode = (hashCode * 59) + this.Method.GetHashCode();
                }
                if (this.Url != null)
                {
                    hashCode = (hashCode * 59) + this.Url.GetHashCode();
                }
                if (this.HttpVersion != null)
                {
                    hashCode = (hashCode * 59) + this.HttpVersion.GetHashCode();
                }
                if (this.Cookies != null)
                {
                    hashCode = (hashCode * 59) + this.Cookies.GetHashCode();
                }
                if (this.Headers != null)
                {
                    hashCode = (hashCode * 59) + this.Headers.GetHashCode();
                }
                if (this.QueryString != null)
                {
                    hashCode = (hashCode * 59) + this.QueryString.GetHashCode();
                }
                if (this.PostData != null)
                {
                    hashCode = (hashCode * 59) + this.PostData.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.HeadersSize.GetHashCode();
                hashCode = (hashCode * 59) + this.BodySize.GetHashCode();
                if (this.Comment != null)
                {
                    hashCode = (hashCode * 59) + this.Comment.GetHashCode();
                }
                if (this.AdditionalProperties != null)
                {
                    hashCode = (hashCode * 59) + this.AdditionalProperties.GetHashCode();
                }
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        public IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
