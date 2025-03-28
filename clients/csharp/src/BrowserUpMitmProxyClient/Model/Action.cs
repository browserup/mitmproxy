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
    /// Action
    /// </summary>
    [DataContract(Name = "Action")]
    public partial class Action : IEquatable<Action>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Action" /> class.
        /// </summary>
        /// <param name="name">name.</param>
        /// <param name="id">id.</param>
        /// <param name="className">className.</param>
        /// <param name="tagName">tagName.</param>
        /// <param name="xpath">xpath.</param>
        /// <param name="dataAttributes">dataAttributes.</param>
        /// <param name="formName">formName.</param>
        /// <param name="content">content.</param>
        public Action(string name = default(string), string id = default(string), string className = default(string), string tagName = default(string), string xpath = default(string), string dataAttributes = default(string), string formName = default(string), string content = default(string))
        {
            this.Name = name;
            this.Id = id;
            this.ClassName = className;
            this.TagName = tagName;
            this.Xpath = xpath;
            this.DataAttributes = dataAttributes;
            this.FormName = formName;
            this.Content = content;
        }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets ClassName
        /// </summary>
        [DataMember(Name = "className", EmitDefaultValue = false)]
        public string ClassName { get; set; }

        /// <summary>
        /// Gets or Sets TagName
        /// </summary>
        [DataMember(Name = "tagName", EmitDefaultValue = false)]
        public string TagName { get; set; }

        /// <summary>
        /// Gets or Sets Xpath
        /// </summary>
        [DataMember(Name = "xpath", EmitDefaultValue = false)]
        public string Xpath { get; set; }

        /// <summary>
        /// Gets or Sets DataAttributes
        /// </summary>
        [DataMember(Name = "dataAttributes", EmitDefaultValue = false)]
        public string DataAttributes { get; set; }

        /// <summary>
        /// Gets or Sets FormName
        /// </summary>
        [DataMember(Name = "formName", EmitDefaultValue = false)]
        public string FormName { get; set; }

        /// <summary>
        /// Gets or Sets Content
        /// </summary>
        [DataMember(Name = "content", EmitDefaultValue = false)]
        public string Content { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class Action {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  ClassName: ").Append(ClassName).Append("\n");
            sb.Append("  TagName: ").Append(TagName).Append("\n");
            sb.Append("  Xpath: ").Append(Xpath).Append("\n");
            sb.Append("  DataAttributes: ").Append(DataAttributes).Append("\n");
            sb.Append("  FormName: ").Append(FormName).Append("\n");
            sb.Append("  Content: ").Append(Content).Append("\n");
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
            return this.Equals(input as Action);
        }

        /// <summary>
        /// Returns true if Action instances are equal
        /// </summary>
        /// <param name="input">Instance of Action to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Action input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.ClassName == input.ClassName ||
                    (this.ClassName != null &&
                    this.ClassName.Equals(input.ClassName))
                ) && 
                (
                    this.TagName == input.TagName ||
                    (this.TagName != null &&
                    this.TagName.Equals(input.TagName))
                ) && 
                (
                    this.Xpath == input.Xpath ||
                    (this.Xpath != null &&
                    this.Xpath.Equals(input.Xpath))
                ) && 
                (
                    this.DataAttributes == input.DataAttributes ||
                    (this.DataAttributes != null &&
                    this.DataAttributes.Equals(input.DataAttributes))
                ) && 
                (
                    this.FormName == input.FormName ||
                    (this.FormName != null &&
                    this.FormName.Equals(input.FormName))
                ) && 
                (
                    this.Content == input.Content ||
                    (this.Content != null &&
                    this.Content.Equals(input.Content))
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
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.Id != null)
                {
                    hashCode = (hashCode * 59) + this.Id.GetHashCode();
                }
                if (this.ClassName != null)
                {
                    hashCode = (hashCode * 59) + this.ClassName.GetHashCode();
                }
                if (this.TagName != null)
                {
                    hashCode = (hashCode * 59) + this.TagName.GetHashCode();
                }
                if (this.Xpath != null)
                {
                    hashCode = (hashCode * 59) + this.Xpath.GetHashCode();
                }
                if (this.DataAttributes != null)
                {
                    hashCode = (hashCode * 59) + this.DataAttributes.GetHashCode();
                }
                if (this.FormName != null)
                {
                    hashCode = (hashCode * 59) + this.FormName.GetHashCode();
                }
                if (this.Content != null)
                {
                    hashCode = (hashCode * 59) + this.Content.GetHashCode();
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
