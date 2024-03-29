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
from akeyless.models.gateway_update_producer_azure import GatewayUpdateProducerAzure  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateProducerAzure(unittest.TestCase):
    """GatewayUpdateProducerAzure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateProducerAzure
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_producer_azure.GatewayUpdateProducerAzure()  # noqa: E501
        if include_optional :
            return GatewayUpdateProducerAzure(
                app_obj_id = '0', 
                azure_client_id = '0', 
                azure_client_secret = '0', 
                azure_tenant_id = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                producer_encryption_key_name = '0', 
                secure_access_enable = '0', 
                secure_access_web = True, 
                secure_access_web_browsing = True, 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_group_obj_id = '0', 
                user_portal_access = True, 
                user_principal_name = '0', 
                user_programmatic_access = True, 
                user_role_template_id = '0', 
                user_ttl = '60m', 
                username = '0'
            )
        else :
            return GatewayUpdateProducerAzure(
                name = '0',
        )

    def testGatewayUpdateProducerAzure(self):
        """Test GatewayUpdateProducerAzure"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
