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
from akeyless.models.update_group import UpdateGroup  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateGroup(unittest.TestCase):
    """UpdateGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_group.UpdateGroup()  # noqa: E501
        if include_optional :
            return UpdateGroup(
                description = '0', 
                group_alias = '0', 
                json = True, 
                name = '0', 
                new_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_assignment = '0'
            )
        else :
            return UpdateGroup(
                group_alias = '0',
                name = '0',
        )

    def testUpdateGroup(self):
        """Test UpdateGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
