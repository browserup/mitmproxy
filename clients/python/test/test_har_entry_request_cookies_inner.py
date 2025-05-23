# coding: utf-8

"""
    BrowserUp MitmProxy

    ___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___ 

    The version of the OpenAPI document: 1.25
    Contact: developers@browserup.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from BrowserUpMitmProxyClient.models.har_entry_request_cookies_inner import HarEntryRequestCookiesInner

class TestHarEntryRequestCookiesInner(unittest.TestCase):
    """HarEntryRequestCookiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HarEntryRequestCookiesInner:
        """Test HarEntryRequestCookiesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HarEntryRequestCookiesInner`
        """
        model = HarEntryRequestCookiesInner()
        if include_optional:
            return HarEntryRequestCookiesInner(
                name = '',
                value = '',
                path = '',
                domain = '',
                expires = '',
                http_only = True,
                secure = True,
                comment = ''
            )
        else:
            return HarEntryRequestCookiesInner(
                name = '',
                value = '',
        )
        """

    def testHarEntryRequestCookiesInner(self):
        """Test HarEntryRequestCookiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
