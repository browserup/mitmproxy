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

from BrowserUpMitmProxyClient.models.har import Har

class TestHar(unittest.TestCase):
    """Har unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Har:
        """Test Har
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Har`
        """
        model = Har()
        if include_optional:
            return Har(
                log = BrowserUpMitmProxyClient.models.har_log.Har_log(
                    version = '', 
                    creator = BrowserUpMitmProxyClient.models.har_log_creator.Har_log_creator(
                        name = '', 
                        version = '', 
                        comment = '', ), 
                    browser = BrowserUpMitmProxyClient.models.har_log_creator.Har_log_creator(
                        name = '', 
                        version = '', 
                        comment = '', ), 
                    pages = [
                        { }
                        ], 
                    entries = [
                        BrowserUpMitmProxyClient.models.har_entry.HarEntry(
                            pageref = '', 
                            started_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time = 0, 
                            request = { }, 
                            response = { }, 
                            cache = BrowserUpMitmProxyClient.models.har_entry_cache.HarEntry_cache(
                                before_request = BrowserUpMitmProxyClient.models.har_entry_cache_before_request.HarEntry_cache_beforeRequest(
                                    expires = '', 
                                    last_access = '', 
                                    e_tag = '', 
                                    hit_count = 56, 
                                    comment = '', ), 
                                after_request = BrowserUpMitmProxyClient.models.har_entry_cache_before_request.HarEntry_cache_beforeRequest(
                                    expires = '', 
                                    last_access = '', 
                                    e_tag = '', 
                                    hit_count = 56, 
                                    comment = '', ), 
                                comment = '', ), 
                            timings = BrowserUpMitmProxyClient.models.har_entry_timings.HarEntry_timings(
                                dns = -1, 
                                connect = -1, 
                                blocked = -1, 
                                send = -1, 
                                wait = -1, 
                                receive = -1, 
                                ssl = -1, 
                                comment = '', ), 
                            server_ip_address = '', 
                            _web_socket_messages = [
                                BrowserUpMitmProxyClient.models.web_socket_message.WebSocketMessage(
                                    type = '', 
                                    opcode = 1.337, 
                                    data = '', 
                                    time = 1.337, )
                                ], 
                            _span_id = '', 
                            _parent_id = '', 
                            _trace_id = '', 
                            connection = '', 
                            comment = '', )
                        ], 
                    _trace_id = '', 
                    _span_id = '', 
                    comment = '', )
            )
        else:
            return Har(
                log = BrowserUpMitmProxyClient.models.har_log.Har_log(
                    version = '', 
                    creator = BrowserUpMitmProxyClient.models.har_log_creator.Har_log_creator(
                        name = '', 
                        version = '', 
                        comment = '', ), 
                    browser = BrowserUpMitmProxyClient.models.har_log_creator.Har_log_creator(
                        name = '', 
                        version = '', 
                        comment = '', ), 
                    pages = [
                        { }
                        ], 
                    entries = [
                        BrowserUpMitmProxyClient.models.har_entry.HarEntry(
                            pageref = '', 
                            started_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time = 0, 
                            request = { }, 
                            response = { }, 
                            cache = BrowserUpMitmProxyClient.models.har_entry_cache.HarEntry_cache(
                                before_request = BrowserUpMitmProxyClient.models.har_entry_cache_before_request.HarEntry_cache_beforeRequest(
                                    expires = '', 
                                    last_access = '', 
                                    e_tag = '', 
                                    hit_count = 56, 
                                    comment = '', ), 
                                after_request = BrowserUpMitmProxyClient.models.har_entry_cache_before_request.HarEntry_cache_beforeRequest(
                                    expires = '', 
                                    last_access = '', 
                                    e_tag = '', 
                                    hit_count = 56, 
                                    comment = '', ), 
                                comment = '', ), 
                            timings = BrowserUpMitmProxyClient.models.har_entry_timings.HarEntry_timings(
                                dns = -1, 
                                connect = -1, 
                                blocked = -1, 
                                send = -1, 
                                wait = -1, 
                                receive = -1, 
                                ssl = -1, 
                                comment = '', ), 
                            server_ip_address = '', 
                            _web_socket_messages = [
                                BrowserUpMitmProxyClient.models.web_socket_message.WebSocketMessage(
                                    type = '', 
                                    opcode = 1.337, 
                                    data = '', 
                                    time = 1.337, )
                                ], 
                            _span_id = '', 
                            _parent_id = '', 
                            _trace_id = '', 
                            connection = '', 
                            comment = '', )
                        ], 
                    _trace_id = '', 
                    _span_id = '', 
                    comment = '', ),
        )
        """

    def testHar(self):
        """Test Har"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
