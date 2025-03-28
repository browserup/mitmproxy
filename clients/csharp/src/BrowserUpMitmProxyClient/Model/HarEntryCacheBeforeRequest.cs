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
using System.Reflection;

namespace BrowserUpMitmProxyClient.Model
{
    /// <summary>
    /// HarEntryCacheBeforeRequest
    /// </summary>
    [JsonConverter(typeof(HarEntryCacheBeforeRequestJsonConverter))]
    [DataContract(Name = "HarEntry_cache_beforeRequest")]
    public partial class HarEntryCacheBeforeRequest : AbstractOpenAPISchema, IEquatable<HarEntryCacheBeforeRequest>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryCacheBeforeRequest" /> class.
        /// </summary>
        public HarEntryCacheBeforeRequest()
        {
            this.IsNullable = true;
            this.SchemaType= "oneOf";
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="HarEntryCacheBeforeRequest" /> class
        /// with the <see cref="HarEntryCacheBeforeRequestOneOf" /> class
        /// </summary>
        /// <param name="actualInstance">An instance of HarEntryCacheBeforeRequestOneOf.</param>
        public HarEntryCacheBeforeRequest(HarEntryCacheBeforeRequestOneOf actualInstance)
        {
            this.IsNullable = true;
            this.SchemaType= "oneOf";
            this.ActualInstance = actualInstance;
        }


        private Object _actualInstance;

        /// <summary>
        /// Gets or Sets ActualInstance
        /// </summary>
        public override Object ActualInstance
        {
            get
            {
                return _actualInstance;
            }
            set
            {
                if (value.GetType() == typeof(HarEntryCacheBeforeRequestOneOf))
                {
                    this._actualInstance = value;
                }
                else
                {
                    throw new ArgumentException("Invalid instance found. Must be the following types: HarEntryCacheBeforeRequestOneOf");
                }
            }
        }

        /// <summary>
        /// Get the actual instance of `HarEntryCacheBeforeRequestOneOf`. If the actual instance is not `HarEntryCacheBeforeRequestOneOf`,
        /// the InvalidClassException will be thrown
        /// </summary>
        /// <returns>An instance of HarEntryCacheBeforeRequestOneOf</returns>
        public HarEntryCacheBeforeRequestOneOf GetHarEntryCacheBeforeRequestOneOf()
        {
            return (HarEntryCacheBeforeRequestOneOf)this.ActualInstance;
        }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class HarEntryCacheBeforeRequest {\n");
            sb.Append("  ActualInstance: ").Append(this.ActualInstance).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public override string ToJson()
        {
            return JsonConvert.SerializeObject(this.ActualInstance, HarEntryCacheBeforeRequest.SerializerSettings);
        }

        /// <summary>
        /// Converts the JSON string into an instance of HarEntryCacheBeforeRequest
        /// </summary>
        /// <param name="jsonString">JSON string</param>
        /// <returns>An instance of HarEntryCacheBeforeRequest</returns>
        public static HarEntryCacheBeforeRequest FromJson(string jsonString)
        {
            HarEntryCacheBeforeRequest newHarEntryCacheBeforeRequest = null;

            if (string.IsNullOrEmpty(jsonString))
            {
                return newHarEntryCacheBeforeRequest;
            }
            int match = 0;
            List<string> matchedTypes = new List<string>();

            try
            {
                // if it does not contains "AdditionalProperties", use SerializerSettings to deserialize
                if (typeof(HarEntryCacheBeforeRequestOneOf).GetProperty("AdditionalProperties") == null)
                {
                    newHarEntryCacheBeforeRequest = new HarEntryCacheBeforeRequest(JsonConvert.DeserializeObject<HarEntryCacheBeforeRequestOneOf>(jsonString, HarEntryCacheBeforeRequest.SerializerSettings));
                }
                else
                {
                    newHarEntryCacheBeforeRequest = new HarEntryCacheBeforeRequest(JsonConvert.DeserializeObject<HarEntryCacheBeforeRequestOneOf>(jsonString, HarEntryCacheBeforeRequest.AdditionalPropertiesSerializerSettings));
                }
                matchedTypes.Add("HarEntryCacheBeforeRequestOneOf");
                match++;
            }
            catch (Exception exception)
            {
                // deserialization failed, try the next one
                System.Diagnostics.Debug.WriteLine(string.Format("Failed to deserialize `{0}` into HarEntryCacheBeforeRequestOneOf: {1}", jsonString, exception.ToString()));
            }

            if (match == 0)
            {
                throw new InvalidDataException("The JSON string `" + jsonString + "` cannot be deserialized into any schema defined.");
            }
            else if (match > 1)
            {
                throw new InvalidDataException("The JSON string `" + jsonString + "` incorrectly matches more than one schema (should be exactly one match): " + matchedTypes);
            }

            // deserialization is considered successful at this point if no exception has been thrown.
            return newHarEntryCacheBeforeRequest;
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as HarEntryCacheBeforeRequest);
        }

        /// <summary>
        /// Returns true if HarEntryCacheBeforeRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of HarEntryCacheBeforeRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(HarEntryCacheBeforeRequest input)
        {
            if (input == null)
                return false;

            return this.ActualInstance.Equals(input.ActualInstance);
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
                if (this.ActualInstance != null)
                    hashCode = hashCode * 59 + this.ActualInstance.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

    /// <summary>
    /// Custom JSON converter for HarEntryCacheBeforeRequest
    /// </summary>
    public class HarEntryCacheBeforeRequestJsonConverter : JsonConverter
    {
        /// <summary>
        /// To write the JSON string
        /// </summary>
        /// <param name="writer">JSON writer</param>
        /// <param name="value">Object to be converted into a JSON string</param>
        /// <param name="serializer">JSON Serializer</param>
        public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
        {
            writer.WriteRawValue((string)(typeof(HarEntryCacheBeforeRequest).GetMethod("ToJson").Invoke(value, null)));
        }

        /// <summary>
        /// To convert a JSON string into an object
        /// </summary>
        /// <param name="reader">JSON reader</param>
        /// <param name="objectType">Object type</param>
        /// <param name="existingValue">Existing value</param>
        /// <param name="serializer">JSON Serializer</param>
        /// <returns>The object converted from the JSON string</returns>
        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            if(reader.TokenType != JsonToken.Null)
            {
                return HarEntryCacheBeforeRequest.FromJson(JObject.Load(reader).ToString(Formatting.None));
            }
            return null;
        }

        /// <summary>
        /// Check if the object can be converted
        /// </summary>
        /// <param name="objectType">Object type</param>
        /// <returns>True if the object can be converted</returns>
        public override bool CanConvert(Type objectType)
        {
            return false;
        }
    }

}
