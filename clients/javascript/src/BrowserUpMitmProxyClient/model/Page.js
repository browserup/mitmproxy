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
import Error from './Error';
import Metric from './Metric';
import PageTimings from './PageTimings';
import VerifyResult from './VerifyResult';

/**
 * The Page model module.
 * @module BrowserUpMitmProxyClient/model/Page
 * @version 1.0.0
 */
class Page {
    /**
     * Constructs a new <code>Page</code>.
     * @alias module:BrowserUpMitmProxyClient/model/Page
     * @extends Object
     * @param startedDateTime {Date} 
     * @param id {String} 
     * @param title {String} 
     * @param pageTimings {module:BrowserUpMitmProxyClient/model/PageTimings} 
     */
    constructor(startedDateTime, id, title, pageTimings) { 
        
        Page.initialize(this, startedDateTime, id, title, pageTimings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, startedDateTime, id, title, pageTimings) { 
        obj['startedDateTime'] = startedDateTime;
        obj['id'] = id;
        obj['title'] = title;
        obj['pageTimings'] = pageTimings;
    }

    /**
     * Constructs a <code>Page</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:BrowserUpMitmProxyClient/model/Page} obj Optional instance to populate.
     * @return {module:BrowserUpMitmProxyClient/model/Page} The populated <code>Page</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Page();

            ApiClient.constructFromObject(data, obj, 'Object');
            

            if (data.hasOwnProperty('startedDateTime')) {
                obj['startedDateTime'] = ApiClient.convertToType(data['startedDateTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('_verifications')) {
                obj['_verifications'] = ApiClient.convertToType(data['_verifications'], [VerifyResult]);
            }
            if (data.hasOwnProperty('_metrics')) {
                obj['_metrics'] = ApiClient.convertToType(data['_metrics'], [Metric]);
            }
            if (data.hasOwnProperty('_errors')) {
                obj['_errors'] = ApiClient.convertToType(data['_errors'], [Error]);
            }
            if (data.hasOwnProperty('_span_id')) {
                obj['_span_id'] = ApiClient.convertToType(data['_span_id'], 'String');
            }
            if (data.hasOwnProperty('_parent_id')) {
                obj['_parent_id'] = ApiClient.convertToType(data['_parent_id'], 'String');
            }
            if (data.hasOwnProperty('pageTimings')) {
                obj['pageTimings'] = PageTimings.constructFromObject(data['pageTimings']);
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Page</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Page</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Page.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        if (data['_verifications']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_verifications'])) {
                throw new Error("Expected the field `_verifications` to be an array in the JSON data but got " + data['_verifications']);
            }
            // validate the optional field `_verifications` (array)
            for (const item of data['_verifications']) {
                VerifyResult.validateJSON(item);
            };
        }
        if (data['_metrics']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_metrics'])) {
                throw new Error("Expected the field `_metrics` to be an array in the JSON data but got " + data['_metrics']);
            }
            // validate the optional field `_metrics` (array)
            for (const item of data['_metrics']) {
                Metric.validateJSON(item);
            };
        }
        if (data['_errors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_errors'])) {
                throw new Error("Expected the field `_errors` to be an array in the JSON data but got " + data['_errors']);
            }
            // validate the optional field `_errors` (array)
            for (const item of data['_errors']) {
                Error.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['_span_id'] && !(typeof data['_span_id'] === 'string' || data['_span_id'] instanceof String)) {
            throw new Error("Expected the field `_span_id` to be a primitive type in the JSON string but got " + data['_span_id']);
        }
        // ensure the json data is a string
        if (data['_parent_id'] && !(typeof data['_parent_id'] === 'string' || data['_parent_id'] instanceof String)) {
            throw new Error("Expected the field `_parent_id` to be a primitive type in the JSON string but got " + data['_parent_id']);
        }
        // ensure the json data is a string
        if (data['comment'] && !(typeof data['comment'] === 'string' || data['comment'] instanceof String)) {
            throw new Error("Expected the field `comment` to be a primitive type in the JSON string but got " + data['comment']);
        }

        return true;
    }


}

Page.RequiredProperties = ["startedDateTime", "id", "title", "pageTimings"];

/**
 * @member {Date} startedDateTime
 */
Page.prototype['startedDateTime'] = undefined;

/**
 * @member {String} id
 */
Page.prototype['id'] = undefined;

/**
 * @member {String} title
 */
Page.prototype['title'] = undefined;

/**
 * @member {Array.<module:BrowserUpMitmProxyClient/model/VerifyResult>} _verifications
 */
Page.prototype['_verifications'] = undefined;

/**
 * @member {Array.<module:BrowserUpMitmProxyClient/model/Metric>} _metrics
 */
Page.prototype['_metrics'] = undefined;

/**
 * @member {Array.<module:BrowserUpMitmProxyClient/model/Error>} _errors
 */
Page.prototype['_errors'] = undefined;

/**
 * W3C Trace Context span ID for this page
 * @member {String} _span_id
 */
Page.prototype['_span_id'] = undefined;

/**
 * W3C Trace Context parent span ID (typically the HAR log span ID)
 * @member {String} _parent_id
 */
Page.prototype['_parent_id'] = undefined;

/**
 * @member {module:BrowserUpMitmProxyClient/model/PageTimings} pageTimings
 */
Page.prototype['pageTimings'] = undefined;

/**
 * @member {String} comment
 */
Page.prototype['comment'] = undefined;






export default Page;

