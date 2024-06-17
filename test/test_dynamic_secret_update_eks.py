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
from akeyless.models.dynamic_secret_update_eks import DynamicSecretUpdateEks  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretUpdateEks(unittest.TestCase):
    """DynamicSecretUpdateEks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretUpdateEks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_update_eks.DynamicSecretUpdateEks()  # noqa: E501
        if include_optional :
            return DynamicSecretUpdateEks(
                delete_protection = '0', 
                description = '0', 
                eks_access_key_id = '0', 
                eks_assume_role = '0', 
                eks_cluster_ca_cert = '0', 
                eks_cluster_endpoint = '0', 
                eks_cluster_name = '0', 
                eks_region = 'us-east-2', 
                eks_secret_access_key = '0', 
                json = True, 
                name = '0', 
                new_name = '0', 
                producer_encryption_key_name = '0', 
                secure_access_allow_port_forwading = True, 
                secure_access_bastion_issuer = '0', 
                secure_access_cluster_endpoint = '0', 
                secure_access_enable = '0', 
                secure_access_web = True, 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '15m'
            )
        else :
            return DynamicSecretUpdateEks(
                name = '0',
        )

    def testDynamicSecretUpdateEks(self):
        """Test DynamicSecretUpdateEks"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()