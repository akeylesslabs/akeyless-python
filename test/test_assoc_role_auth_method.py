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
from akeyless.models.assoc_role_auth_method import AssocRoleAuthMethod  # noqa: E501
from akeyless.rest import ApiException

class TestAssocRoleAuthMethod(unittest.TestCase):
    """AssocRoleAuthMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AssocRoleAuthMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.assoc_role_auth_method.AssocRoleAuthMethod()  # noqa: E501
        if include_optional :
            return AssocRoleAuthMethod(
                am_name = '0', 
                role_name = '0', 
                sub_claims = {
                    'key' : '0'
                    }, 
                token = '0', 
                uid_token = '0'
            )
        else :
            return AssocRoleAuthMethod(
                am_name = '0',
                role_name = '0',
        )

    def testAssocRoleAuthMethod(self):
        """Test AssocRoleAuthMethod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
