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
from akeyless.models.rotated_secret_update_aws import RotatedSecretUpdateAws  # noqa: E501
from akeyless.rest import ApiException

class TestRotatedSecretUpdateAws(unittest.TestCase):
    """RotatedSecretUpdateAws unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RotatedSecretUpdateAws
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.rotated_secret_update_aws.RotatedSecretUpdateAws()  # noqa: E501
        if include_optional :
            return RotatedSecretUpdateAws(
                add_tag = [
                    '0'
                    ], 
                api_id = '0', 
                api_key = '0', 
                authentication_credentials = 'use-user-creds', 
                auto_rotate = '0', 
                aws_region = 'us-east-2', 
                delete_protection = '0', 
                description = 'default_metadata', 
                grace_rotation = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                name = '0', 
                new_name = '0', 
                password_length = '0', 
                rm_tag = [
                    '0'
                    ], 
                rotate_after_disconnect = 'false', 
                rotation_hour = 56, 
                rotation_interval = '0', 
                secure_access_aws_account_id = '0', 
                secure_access_aws_native_cli = True, 
                secure_access_bastion_issuer = '0', 
                secure_access_enable = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return RotatedSecretUpdateAws(
                name = '0',
        )

    def testRotatedSecretUpdateAws(self):
        """Test RotatedSecretUpdateAws"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
