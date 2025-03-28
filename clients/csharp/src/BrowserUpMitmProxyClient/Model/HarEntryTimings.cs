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
    /// HarEntryTimings
    /// </summary>
    [DataContract(Name = "HarEntry_timings")]
    public partial class HarEntryTimings : IEquatable<HarEntryTimings>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryTimings" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected HarEntryTimings() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryTimings" /> class.
        /// </summary>
        /// <param name="dns">dns (required) (default to -1).</param>
        /// <param name="connect">connect (required) (default to -1).</param>
        /// <param name="blocked">blocked (required) (default to -1).</param>
        /// <param name="send">send (required) (default to -1).</param>
        /// <param name="wait">wait (required) (default to -1).</param>
        /// <param name="receive">receive (required) (default to -1).</param>
        /// <param name="ssl">ssl (required) (default to -1).</param>
        /// <param name="comment">comment.</param>
        public HarEntryTimings(long dns = -1, long connect = -1, long blocked = -1, long send = -1, long wait = -1, long receive = -1, long ssl = -1, string comment = default(string))
        {
            this.Dns = dns;
            this.Connect = connect;
            this.Blocked = blocked;
            this.Send = send;
            this.Wait = wait;
            this.Receive = receive;
            this.Ssl = ssl;
            this.Comment = comment;
        }

        /// <summary>
        /// Gets or Sets Dns
        /// </summary>
        [DataMember(Name = "dns", IsRequired = true, EmitDefaultValue = true)]
        public long Dns { get; set; }

        /// <summary>
        /// Gets or Sets Connect
        /// </summary>
        [DataMember(Name = "connect", IsRequired = true, EmitDefaultValue = true)]
        public long Connect { get; set; }

        /// <summary>
        /// Gets or Sets Blocked
        /// </summary>
        [DataMember(Name = "blocked", IsRequired = true, EmitDefaultValue = true)]
        public long Blocked { get; set; }

        /// <summary>
        /// Gets or Sets Send
        /// </summary>
        [DataMember(Name = "send", IsRequired = true, EmitDefaultValue = true)]
        public long Send { get; set; }

        /// <summary>
        /// Gets or Sets Wait
        /// </summary>
        [DataMember(Name = "wait", IsRequired = true, EmitDefaultValue = true)]
        public long Wait { get; set; }

        /// <summary>
        /// Gets or Sets Receive
        /// </summary>
        [DataMember(Name = "receive", IsRequired = true, EmitDefaultValue = true)]
        public long Receive { get; set; }

        /// <summary>
        /// Gets or Sets Ssl
        /// </summary>
        [DataMember(Name = "ssl", IsRequired = true, EmitDefaultValue = true)]
        public long Ssl { get; set; }

        /// <summary>
        /// Gets or Sets Comment
        /// </summary>
        [DataMember(Name = "comment", EmitDefaultValue = false)]
        public string Comment { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class HarEntryTimings {\n");
            sb.Append("  Dns: ").Append(Dns).Append("\n");
            sb.Append("  Connect: ").Append(Connect).Append("\n");
            sb.Append("  Blocked: ").Append(Blocked).Append("\n");
            sb.Append("  Send: ").Append(Send).Append("\n");
            sb.Append("  Wait: ").Append(Wait).Append("\n");
            sb.Append("  Receive: ").Append(Receive).Append("\n");
            sb.Append("  Ssl: ").Append(Ssl).Append("\n");
            sb.Append("  Comment: ").Append(Comment).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
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
            return this.Equals(input as HarEntryTimings);
        }

        /// <summary>
        /// Returns true if HarEntryTimings instances are equal
        /// </summary>
        /// <param name="input">Instance of HarEntryTimings to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(HarEntryTimings input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Dns == input.Dns ||
                    this.Dns.Equals(input.Dns)
                ) && 
                (
                    this.Connect == input.Connect ||
                    this.Connect.Equals(input.Connect)
                ) && 
                (
                    this.Blocked == input.Blocked ||
                    this.Blocked.Equals(input.Blocked)
                ) && 
                (
                    this.Send == input.Send ||
                    this.Send.Equals(input.Send)
                ) && 
                (
                    this.Wait == input.Wait ||
                    this.Wait.Equals(input.Wait)
                ) && 
                (
                    this.Receive == input.Receive ||
                    this.Receive.Equals(input.Receive)
                ) && 
                (
                    this.Ssl == input.Ssl ||
                    this.Ssl.Equals(input.Ssl)
                ) && 
                (
                    this.Comment == input.Comment ||
                    (this.Comment != null &&
                    this.Comment.Equals(input.Comment))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                hashCode = (hashCode * 59) + this.Dns.GetHashCode();
                hashCode = (hashCode * 59) + this.Connect.GetHashCode();
                hashCode = (hashCode * 59) + this.Blocked.GetHashCode();
                hashCode = (hashCode * 59) + this.Send.GetHashCode();
                hashCode = (hashCode * 59) + this.Wait.GetHashCode();
                hashCode = (hashCode * 59) + this.Receive.GetHashCode();
                hashCode = (hashCode * 59) + this.Ssl.GetHashCode();
                if (this.Comment != null)
                {
                    hashCode = (hashCode * 59) + this.Comment.GetHashCode();
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
            // Dns (long) minimum
            if (this.Dns < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Dns, must be a value greater than or equal to -1.", new [] { "Dns" });
            }

            // Connect (long) minimum
            if (this.Connect < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Connect, must be a value greater than or equal to -1.", new [] { "Connect" });
            }

            // Blocked (long) minimum
            if (this.Blocked < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Blocked, must be a value greater than or equal to -1.", new [] { "Blocked" });
            }

            // Send (long) minimum
            if (this.Send < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Send, must be a value greater than or equal to -1.", new [] { "Send" });
            }

            // Wait (long) minimum
            if (this.Wait < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Wait, must be a value greater than or equal to -1.", new [] { "Wait" });
            }

            // Receive (long) minimum
            if (this.Receive < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Receive, must be a value greater than or equal to -1.", new [] { "Receive" });
            }

            // Ssl (long) minimum
            if (this.Ssl < (long)-1)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Ssl, must be a value greater than or equal to -1.", new [] { "Ssl" });
            }

            yield break;
        }
    }

}
