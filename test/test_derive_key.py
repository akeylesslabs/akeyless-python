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
from akeyless.models.derive_key import DeriveKey  # noqa: E501
from akeyless.rest import ApiException

class TestDeriveKey(unittest.TestCase):
    """DeriveKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeriveKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.derive_key.DeriveKey()  # noqa: E501
        if include_optional :
            return DeriveKey(
                accessibility = 'regular', 
                alg = 'pbkdf2', 
                hash_function = 'sha256', 
                iter = 56, 
                json = True, 
                key_len = 56, 
                mem = 56, 
                name = '0', 
                parallelism = 56, 
                salt = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return DeriveKey(
                alg = 'pbkdf2',
                iter = 56,
                key_len = 56,
                name = '0',
        )

    def testDeriveKey(self):
        """Test DeriveKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()