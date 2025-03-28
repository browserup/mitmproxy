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
    /// HarEntryResponse
    /// </summary>
    [DataContract(Name = "HarEntry_response")]
    public partial class HarEntryResponse : Dictionary<String, Object>, IEquatable<HarEntryResponse>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryResponse" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected HarEntryResponse()
        {
            this.AdditionalProperties = new Dictionary<string, object>();
        }
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryResponse" /> class.
        /// </summary>
        /// <param name="status">status (required).</param>
        /// <param name="statusText">statusText (required).</param>
        /// <param name="httpVersion">httpVersion (required).</param>
        /// <param name="cookies">cookies (required).</param>
        /// <param name="headers">headers (required).</param>
        /// <param name="content">content (required).</param>
        /// <param name="redirectURL">redirectURL (required).</param>
        /// <param name="headersSize">headersSize (required).</param>
        /// <param name="bodySize">bodySize (required).</param>
        /// <param name="comment">comment.</param>
        public HarEntryResponse(int status = default(int), string statusText = default(string), string httpVersion = default(string), List<HarEntryRequestCookiesInner> cookies = default(List<HarEntryRequestCookiesInner>), List<Header> headers = default(List<Header>), HarEntryResponseContent content = default(HarEntryResponseContent), string redirectURL = default(string), int headersSize = default(int), int bodySize = default(int), string comment = default(string)) : base()
        {
            this.Status = status;
            // to ensure "statusText" is required (not null)
            if (statusText == null)
            {
                throw new ArgumentNullException("statusText is a required property for HarEntryResponse and cannot be null");
            }
            this.StatusText = statusText;
            // to ensure "httpVersion" is required (not null)
            if (httpVersion == null)
            {
                throw new ArgumentNullException("httpVersion is a required property for HarEntryResponse and cannot be null");
            }
            this.HttpVersion = httpVersion;
            // to ensure "cookies" is required (not null)
            if (cookies == null)
            {
                throw new ArgumentNullException("cookies is a required property for HarEntryResponse and cannot be null");
            }
            this.Cookies = cookies;
            // to ensure "headers" is required (not null)
            if (headers == null)
            {
                throw new ArgumentNullException("headers is a required property for HarEntryResponse and cannot be null");
            }
            this.Headers = headers;
            // to ensure "content" is required (not null)
            if (content == null)
            {
                throw new ArgumentNullException("content is a required property for HarEntryResponse and cannot be null");
            }
            this.Content = content;
            // to ensure "redirectURL" is required (not null)
            if (redirectURL == null)
            {
                throw new ArgumentNullException("redirectURL is a required property for HarEntryResponse and cannot be null");
            }
            this.RedirectURL = redirectURL;
            this.HeadersSize = headersSize;
            this.BodySize = bodySize;
            this.Comment = comment;
            this.AdditionalProperties = new Dictionary<string, object>();
        }

        /// <summary>
        /// Gets or Sets Status
        /// </summary>
        [DataMember(Name = "status", IsRequired = true, EmitDefaultValue = true)]
        public int Status { get; set; }

        /// <summary>
        /// Gets or Sets StatusText
        /// </summary>
        [DataMember(Name = "statusText", IsRequired = true, EmitDefaultValue = true)]
        public string StatusText { get; set; }

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
        /// Gets or Sets Content
        /// </summary>
        [DataMember(Name = "content", IsRequired = true, EmitDefaultValue = true)]
        public HarEntryResponseContent Content { get; set; }

        /// <summary>
        /// Gets or Sets RedirectURL
        /// </summary>
        [DataMember(Name = "redirectURL", IsRequired = true, EmitDefaultValue = true)]
        public string RedirectURL { get; set; }

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
            sb.Append("class HarEntryResponse {\n");
            sb.Append("  ").Append(base.ToString().Replace("\n", "\n  ")).Append("\n");
            sb.Append("  Status: ").Append(Status).Append("\n");
            sb.Append("  StatusText: ").Append(StatusText).Append("\n");
            sb.Append("  HttpVersion: ").Append(HttpVersion).Append("\n");
            sb.Append("  Cookies: ").Append(Cookies).Append("\n");
            sb.Append("  Headers: ").Append(Headers).Append("\n");
            sb.Append("  Content: ").Append(Content).Append("\n");
            sb.Append("  RedirectURL: ").Append(RedirectURL).Append("\n");
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
            return this.Equals(input as HarEntryResponse);
        }

        /// <summary>
        /// Returns true if HarEntryResponse instances are equal
        /// </summary>
        /// <param name="input">Instance of HarEntryResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(HarEntryResponse input)
        {
            if (input == null)
            {
                return false;
            }
            return base.Equals(input) && 
                (
                    this.Status == input.Status ||
                    this.Status.Equals(input.Status)
                ) && base.Equals(input) && 
                (
                    this.StatusText == input.StatusText ||
                    (this.StatusText != null &&
                    this.StatusText.Equals(input.StatusText))
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
                    this.Content == input.Content ||
                    (this.Content != null &&
                    this.Content.Equals(input.Content))
                ) && base.Equals(input) && 
                (
                    this.RedirectURL == input.RedirectURL ||
                    (this.RedirectURL != null &&
                    this.RedirectURL.Equals(input.RedirectURL))
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
                hashCode = (hashCode * 59) + this.Status.GetHashCode();
                if (this.StatusText != null)
                {
                    hashCode = (hashCode * 59) + this.StatusText.GetHashCode();
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
                if (this.Content != null)
                {
                    hashCode = (hashCode * 59) + this.Content.GetHashCode();
                }
                if (this.RedirectURL != null)
                {
                    hashCode = (hashCode * 59) + this.RedirectURL.GetHashCode();
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
