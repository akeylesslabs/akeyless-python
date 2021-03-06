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
from akeyless.models.create_auth_method_azure_ad import CreateAuthMethodAzureAD  # noqa: E501
from akeyless.rest import ApiException

class TestCreateAuthMethodAzureAD(unittest.TestCase):
    """CreateAuthMethodAzureAD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAuthMethodAzureAD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_auth_method_azure_ad.CreateAuthMethodAzureAD()  # noqa: E501
        if include_optional :
            return CreateAuthMethodAzureAD(
                access_expires = 56, 
                audience = 'https://management.azure.com/', 
                bound_group_id = [
                    '0'
                    ], 
                bound_ips = [
                    '0'
                    ], 
                bound_providers = [
                    '0'
                    ], 
                bound_resource_id = [
                    '0'
                    ], 
                bound_resource_names = [
                    '0'
                    ], 
                bound_resource_types = [
                    '0'
                    ], 
                bound_rg_id = [
                    '0'
                    ], 
                bound_spid = [
                    '0'
                    ], 
                bound_sub_id = [
                    '0'
                    ], 
                bound_tenant_id = '0', 
                issuer = 'https://sts.windows.net/---bound_tenant_id---', 
                jwks_uri = 'https://login.microsoftonline.com/common/discovery/keys', 
                name = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateAuthMethodAzureAD(
                bound_tenant_id = '0',
                name = '0',
        )

    def testCreateAuthMethodAzureAD(self):
        """Test CreateAuthMethodAzureAD"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
