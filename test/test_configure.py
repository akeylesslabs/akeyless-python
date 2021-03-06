# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.configure import Configure  # noqa: E501
from akeyless.rest import ApiException

class TestConfigure(unittest.TestCase):
    """Configure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Configure
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.configure.Configure()  # noqa: E501
        if include_optional :
            return Configure(
                access_id = '0', 
                access_key = '0', 
                access_type = 'access_key', 
                admin_email = '0', 
                admin_password = '0', 
                azure_ad_object_id = '0', 
                ldap_proxy_url = '0'
            )
        else :
            return Configure(
        )

    def testConfigure(self):
        """Test Configure"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
