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
from akeyless.models.rotated_secret_create_redshift import RotatedSecretCreateRedshift  # noqa: E501
from akeyless.rest import ApiException

class TestRotatedSecretCreateRedshift(unittest.TestCase):
    """RotatedSecretCreateRedshift unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RotatedSecretCreateRedshift
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.rotated_secret_create_redshift.RotatedSecretCreateRedshift()  # noqa: E501
        if include_optional :
            return RotatedSecretCreateRedshift(
                authentication_credentials = 'use-user-creds', 
                auto_rotate = '0', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                key = '0', 
                name = '0', 
                password_length = '0', 
                rotate_after_disconnect = 'false', 
                rotated_password = '0', 
                rotated_username = '0', 
                rotation_hour = 56, 
                rotation_interval = '0', 
                rotator_type = '0', 
                secure_access_db_name = '0', 
                secure_access_enable = '0', 
                secure_access_host = [
                    '0'
                    ], 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return RotatedSecretCreateRedshift(
                name = '0',
                rotator_type = '0',
                target_name = '0',
        )

    def testRotatedSecretCreateRedshift(self):
        """Test RotatedSecretCreateRedshift"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
