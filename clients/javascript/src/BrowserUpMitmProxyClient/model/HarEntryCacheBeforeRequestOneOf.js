/**
 * BrowserUp MitmProxy
 * ___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.24
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HarEntryCacheBeforeRequestOneOf model module.
 * @module BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequestOneOf
 * @version 1.0.0
 */
class HarEntryCacheBeforeRequestOneOf {
    /**
     * Constructs a new <code>HarEntryCacheBeforeRequestOneOf</code>.
     * @alias module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequestOneOf
     * @param lastAccess {String} 
     * @param eTag {String} 
     * @param hitCount {Number} 
     */
    constructor(lastAccess, eTag, hitCount) { 
        
        HarEntryCacheBeforeRequestOneOf.initialize(this, lastAccess, eTag, hitCount);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, lastAccess, eTag, hitCount) { 
        obj['lastAccess'] = lastAccess;
        obj['eTag'] = eTag;
        obj['hitCount'] = hitCount;
    }

    /**
     * Constructs a <code>HarEntryCacheBeforeRequestOneOf</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequestOneOf} obj Optional instance to populate.
     * @return {module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequestOneOf} The populated <code>HarEntryCacheBeforeRequestOneOf</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HarEntryCacheBeforeRequestOneOf();

            if (data.hasOwnProperty('expires')) {
                obj['expires'] = ApiClient.convertToType(data['expires'], 'String');
            }
            if (data.hasOwnProperty('lastAccess')) {
                obj['lastAccess'] = ApiClient.convertToType(data['lastAccess'], 'String');
            }
            if (data.hasOwnProperty('eTag')) {
                obj['eTag'] = ApiClient.convertToType(data['eTag'], 'String');
            }
            if (data.hasOwnProperty('hitCount')) {
                obj['hitCount'] = ApiClient.convertToType(data['hitCount'], 'Number');
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HarEntryCacheBeforeRequestOneOf</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HarEntryCacheBeforeRequestOneOf</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HarEntryCacheBeforeRequestOneOf.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['expires'] && !(typeof data['expires'] === 'string' || data['expires'] instanceof String)) {
            throw new Error("Expected the field `expires` to be a primitive type in the JSON string but got " + data['expires']);
        }
        // ensure the json data is a string
        if (data['lastAccess'] && !(typeof data['lastAccess'] === 'string' || data['lastAccess'] instanceof String)) {
            throw new Error("Expected the field `lastAccess` to be a primitive type in the JSON string but got " + data['lastAccess']);
        }
        // ensure the json data is a string
        if (data['eTag'] && !(typeof data['eTag'] === 'string' || data['eTag'] instanceof String)) {
            throw new Error("Expected the field `eTag` to be a primitive type in the JSON string but got " + data['eTag']);
        }
        // ensure the json data is a string
        if (data['comment'] && !(typeof data['comment'] === 'string' || data['comment'] instanceof String)) {
            throw new Error("Expected the field `comment` to be a primitive type in the JSON string but got " + data['comment']);
        }

        return true;
    }


}

HarEntryCacheBeforeRequestOneOf.RequiredProperties = ["lastAccess", "eTag", "hitCount"];

/**
 * @member {String} expires
 */
HarEntryCacheBeforeRequestOneOf.prototype['expires'] = undefined;

/**
 * @member {String} lastAccess
 */
HarEntryCacheBeforeRequestOneOf.prototype['lastAccess'] = undefined;

/**
 * @member {String} eTag
 */
HarEntryCacheBeforeRequestOneOf.prototype['eTag'] = undefined;

/**
 * @member {Number} hitCount
 */
HarEntryCacheBeforeRequestOneOf.prototype['hitCount'] = undefined;

/**
 * @member {String} comment
 */
HarEntryCacheBeforeRequestOneOf.prototype['comment'] = undefined;






export default HarEntryCacheBeforeRequestOneOf;

