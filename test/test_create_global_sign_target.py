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
from akeyless.models.create_global_sign_target import CreateGlobalSignTarget  # noqa: E501
from akeyless.rest import ApiException

class TestCreateGlobalSignTarget(unittest.TestCase):
    """CreateGlobalSignTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateGlobalSignTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_global_sign_target.CreateGlobalSignTarget()  # noqa: E501
        if include_optional :
            return CreateGlobalSignTarget(
                comment = '0', 
                contact_email = '0', 
                contact_first_name = '0', 
                contact_last_name = '0', 
                contact_phone = '0', 
                description = '0', 
                json = True, 
                key = '0', 
                name = '0', 
                password = '0', 
                profile_id = '0', 
                timeout = '5m', 
                token = '0', 
                uid_token = '0', 
                username = '0'
            )
        else :
            return CreateGlobalSignTarget(
                contact_email = '0',
                contact_first_name = '0',
                contact_last_name = '0',
                contact_phone = '0',
                name = '0',
                password = '0',
                profile_id = '0',
                username = '0',
        )

    def testCreateGlobalSignTarget(self):
        """Test CreateGlobalSignTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()