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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/BrowserUpMitmProxyClient/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/BrowserUpMitmProxyClient/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.BrowserUpMitmProxyClient);
  }
}(this, function(expect, BrowserUpMitmProxyClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BrowserUpMitmProxyClient.PageTiming();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('PageTiming', function() {
    it('should create an instance of PageTiming', function() {
      // uncomment below and update the code to test PageTiming
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be.a(BrowserUpMitmProxyClient.PageTiming);
    });

    it('should have the property onContentLoad (base name: "onContentLoad")', function() {
      // uncomment below and update the code to test the property onContentLoad
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property onLoad (base name: "onLoad")', function() {
      // uncomment below and update the code to test the property onLoad
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property firstInputDelay (base name: "_firstInputDelay")', function() {
      // uncomment below and update the code to test the property firstInputDelay
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property firstPaint (base name: "_firstPaint")', function() {
      // uncomment below and update the code to test the property firstPaint
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property cumulativeLayoutShift (base name: "_cumulativeLayoutShift")', function() {
      // uncomment below and update the code to test the property cumulativeLayoutShift
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property largestContentfulPaint (base name: "_largestContentfulPaint")', function() {
      // uncomment below and update the code to test the property largestContentfulPaint
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property domInteractive (base name: "_domInteractive")', function() {
      // uncomment below and update the code to test the property domInteractive
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property firstContentfulPaint (base name: "_firstContentfulPaint")', function() {
      // uncomment below and update the code to test the property firstContentfulPaint
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property dns (base name: "_dns")', function() {
      // uncomment below and update the code to test the property dns
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property ssl (base name: "_ssl")', function() {
      // uncomment below and update the code to test the property ssl
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property timeToFirstByte (base name: "_timeToFirstByte")', function() {
      // uncomment below and update the code to test the property timeToFirstByte
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property href (base name: "_href")', function() {
      // uncomment below and update the code to test the property href
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property spanId (base name: "_span_id")', function() {
      // uncomment below and update the code to test the property spanId
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "_parent_id")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new BrowserUpMitmProxyClient.PageTiming();
      //expect(instance).to.be();
    });

  });

}));
