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
from akeyless.models.azure_target_details import AzureTargetDetails  # noqa: E501
from akeyless.rest import ApiException

class TestAzureTargetDetails(unittest.TestCase):
    """AzureTargetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AzureTargetDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.azure_target_details.AzureTargetDetails()  # noqa: E501
        if include_optional :
            return AzureTargetDetails(
                azure_client_id = '0', 
                azure_client_secret = '0', 
                azure_resource_group_name = '0', 
                azure_resource_name = '0', 
                azure_subscription_id = '0', 
                azure_tenant_id = '0', 
                use_gw_cloud_identity = True
            )
        else :
            return AzureTargetDetails(
        )

    def testAzureTargetDetails(self):
        """Test AzureTargetDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
