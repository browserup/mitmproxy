=begin
#BrowserUp Proxy

#___ This is the REST API for controlling the BrowserUp Proxy.  The BrowserUp Proxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 

The version of the OpenAPI document: 1.0.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.1.1

=end

require 'spec_helper'
require 'json'
require 'date'

# Unit tests for BrowserupProxy::VerifyResult
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe BrowserupProxy::VerifyResult do
  let(:instance) { BrowserupProxy::VerifyResult.new }

  describe 'test an instance of VerifyResult' do
    it 'should create an instance of VerifyResult' do
      expect(instance).to be_instance_of(BrowserupProxy::VerifyResult)
    end
  end
  describe 'test attribute "result"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
