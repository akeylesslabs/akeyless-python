# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.splunk_log_forwarding_config import SplunkLogForwardingConfig  # noqa: E501
from akeyless.rest import ApiException

class TestSplunkLogForwardingConfig(unittest.TestCase):
    """SplunkLogForwardingConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SplunkLogForwardingConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.splunk_log_forwarding_config.SplunkLogForwardingConfig()  # noqa: E501
        if include_optional :
            return SplunkLogForwardingConfig(
                splunk_index = '0', 
                splunk_source = '0', 
                splunk_sourcetype = '0', 
                splunk_token = '0', 
                splunk_url = '0'
            )
        else :
            return SplunkLogForwardingConfig(
        )

    def testSplunkLogForwardingConfig(self):
        """Test SplunkLogForwardingConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()