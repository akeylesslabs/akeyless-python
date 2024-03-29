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
from akeyless.models.google_chronicle_forwarding_config import GoogleChronicleForwardingConfig  # noqa: E501
from akeyless.rest import ApiException

class TestGoogleChronicleForwardingConfig(unittest.TestCase):
    """GoogleChronicleForwardingConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GoogleChronicleForwardingConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.google_chronicle_forwarding_config.GoogleChronicleForwardingConfig()  # noqa: E501
        if include_optional :
            return GoogleChronicleForwardingConfig(
                customer_id = '0', 
                log_type = '0', 
                region = '0', 
                service_account_key = '0'
            )
        else :
            return GoogleChronicleForwardingConfig(
        )

    def testGoogleChronicleForwardingConfig(self):
        """Test GoogleChronicleForwardingConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
