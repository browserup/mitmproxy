/**
 * BrowserUp MitmProxy
 * ___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.25
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HarEntryCacheBeforeRequest model module.
 * @module BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequest
 * @version 1.0.0
 */
class HarEntryCacheBeforeRequest {
    /**
     * Constructs a new <code>HarEntryCacheBeforeRequest</code>.
     * @alias module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequest
     * @param lastAccess {String} 
     * @param eTag {String} 
     * @param hitCount {Number} 
     */
    constructor(lastAccess, eTag, hitCount) { 
        
        HarEntryCacheBeforeRequest.initialize(this, lastAccess, eTag, hitCount);
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
     * Constructs a <code>HarEntryCacheBeforeRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequest} obj Optional instance to populate.
     * @return {module:BrowserUpMitmProxyClient/model/HarEntryCacheBeforeRequest} The populated <code>HarEntryCacheBeforeRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HarEntryCacheBeforeRequest();

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
     * Validates the JSON data with respect to <code>HarEntryCacheBeforeRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HarEntryCacheBeforeRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HarEntryCacheBeforeRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
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

HarEntryCacheBeforeRequest.RequiredProperties = ["lastAccess", "eTag", "hitCount"];

/**
 * @member {String} expires
 */
HarEntryCacheBeforeRequest.prototype['expires'] = undefined;

/**
 * @member {String} lastAccess
 */
HarEntryCacheBeforeRequest.prototype['lastAccess'] = undefined;

/**
 * @member {String} eTag
 */
HarEntryCacheBeforeRequest.prototype['eTag'] = undefined;

/**
 * @member {Number} hitCount
 */
HarEntryCacheBeforeRequest.prototype['hitCount'] = undefined;

/**
 * @member {String} comment
 */
HarEntryCacheBeforeRequest.prototype['comment'] = undefined;






export default HarEntryCacheBeforeRequest;

