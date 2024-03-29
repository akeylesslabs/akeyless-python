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
from akeyless.models.venafi_target_details import VenafiTargetDetails  # noqa: E501
from akeyless.rest import ApiException

class TestVenafiTargetDetails(unittest.TestCase):
    """VenafiTargetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VenafiTargetDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.venafi_target_details.VenafiTargetDetails()  # noqa: E501
        if include_optional :
            return VenafiTargetDetails(
                venafi_api_key = '0', 
                venafi_base_url = '0', 
                venafi_tpp_access_token = '0', 
                venafi_tpp_client_id = '0', 
                venafi_tpp_password = '0', 
                venafi_tpp_refresh_token = '0', 
                venafi_tpp_username = '0', 
                venafi_use_tpp = True, 
                venafi_zone = '0'
            )
        else :
            return VenafiTargetDetails(
        )

    def testVenafiTargetDetails(self):
        """Test VenafiTargetDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
