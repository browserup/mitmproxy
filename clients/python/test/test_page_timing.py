# coding: utf-8

"""
BrowserUp MitmProxy

___ This is the REST API for controlling the BrowserUp MitmProxy. The BrowserUp MitmProxy is a swiss army knife for automated testing that captures HTTP traffic in HAR files. It is also useful for Selenium/Cypress tests. ___

The version of the OpenAPI document: 1.0.0
Contact: developers@browserup.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest


class TestPageTiming(unittest.TestCase):
    """PageTiming unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageTiming
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PageTiming`
        """
        model = BrowserUpMitmProxyClient.models.page_timing.PageTiming()  # noqa: E501
        if include_optional :
            return PageTiming(
                on_content_load = 1.337, 
                on_load = 1.337, 
                first_input_delay = 1.337, 
                first_paint = 1.337, 
                cumulative_layout_shift = 1.337, 
                largest_contentful_paint = 1.337, 
                dom_interactive = 1.337, 
                first_contentful_paint = 1.337, 
                dns = 1.337, 
                ssl = 1.337, 
                time_to_first_byte = 1.337, 
                href = ''
            )
        else :
            return PageTiming(
        )
        """

    def testPageTiming(self):
        """Test PageTiming"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
