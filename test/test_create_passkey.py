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
from akeyless.models.create_passkey import CreatePasskey  # noqa: E501
from akeyless.rest import ApiException

class TestCreatePasskey(unittest.TestCase):
    """CreatePasskey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreatePasskey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_passkey.CreatePasskey()  # noqa: E501
        if include_optional :
            return CreatePasskey(
                accessibility = 'regular', 
                alg = 'EC256', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                name = '0', 
                origin_url = [
                    '0'
                    ], 
                protection_key_name = '0', 
                tags = [
                    '0'
                    ], 
                token = '0', 
                uid_token = '0', 
                username = '0'
            )
        else :
            return CreatePasskey(
                alg = 'EC256',
                name = '0',
        )

    def testCreatePasskey(self):
        """Test CreatePasskey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()