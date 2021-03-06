/**
 * BrowserUp Proxy
 * ___ This is the REST API for controlling the BrowserUp Proxy. The BrowserUp Proxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PagePageTimings from './PagePageTimings';

/**
 * The Page model module.
 * @module BrowserUpProxyClient/model/Page
 * @version 1.0.0
 */
class Page {
    /**
     * Constructs a new <code>Page</code>.
     * @alias module:BrowserUpProxyClient/model/Page
     * @param startedDateTime {Date} 
     * @param id {String} 
     * @param title {String} 
     * @param pageTimings {module:BrowserUpProxyClient/model/PagePageTimings} 
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
     * @param {module:BrowserUpProxyClient/model/Page} obj Optional instance to populate.
     * @return {module:BrowserUpProxyClient/model/Page} The populated <code>Page</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Page();

            if (data.hasOwnProperty('startedDateTime')) {
                obj['startedDateTime'] = ApiClient.convertToType(data['startedDateTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('pageTimings')) {
                obj['pageTimings'] = PagePageTimings.constructFromObject(data['pageTimings']);
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
            }
        }
        return obj;
    }


}

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
 * @member {module:BrowserUpProxyClient/model/PagePageTimings} pageTimings
 */
Page.prototype['pageTimings'] = undefined;

/**
 * @member {String} comment
 */
Page.prototype['comment'] = undefined;






export default Page;

