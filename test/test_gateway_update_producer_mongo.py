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
from akeyless.models.gateway_update_producer_mongo import GatewayUpdateProducerMongo  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateProducerMongo(unittest.TestCase):
    """GatewayUpdateProducerMongo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateProducerMongo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_producer_mongo.GatewayUpdateProducerMongo()  # noqa: E501
        if include_optional :
            return GatewayUpdateProducerMongo(
                mongodb_atlas_api_private_key = '0', 
                mongodb_atlas_api_public_key = '0', 
                mongodb_atlas_project_id = '0', 
                mongodb_default_auth_db = '0', 
                mongodb_host_port = '0', 
                mongodb_name = '0', 
                mongodb_password = '0', 
                mongodb_roles = '[]', 
                mongodb_server_uri = '0', 
                mongodb_uri_options = '0', 
                mongodb_username = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                producer_encryption_key_name = '0', 
                secure_access_bastion_issuer = '0', 
                secure_access_enable = '0', 
                secure_access_host = [
                    '0'
                    ], 
                secure_access_web = True, 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m', 
                username = '0'
            )
        else :
            return GatewayUpdateProducerMongo(
                name = '0',
        )

    def testGatewayUpdateProducerMongo(self):
        """Test GatewayUpdateProducerMongo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
