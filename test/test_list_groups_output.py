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
from akeyless.models.list_groups_output import ListGroupsOutput  # noqa: E501
from akeyless.rest import ApiException

class TestListGroupsOutput(unittest.TestCase):
    """ListGroupsOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListGroupsOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.list_groups_output.ListGroupsOutput()  # noqa: E501
        if include_optional :
            return ListGroupsOutput(
                groups = [
                    akeyless.models.group.Group(
                        account_id = '0', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '0', 
                        group_alias = '0', 
                        group_id = '0', 
                        group_name = '0', 
                        modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_assignments = [
                            akeyless.models.access_permission_assignment.AccessPermissionAssignment(
                                access_id = '0', 
                                sub_claims = {
                                    'key' : [
                                        '0'
                                        ]
                                    }, )
                            ], )
                    ], 
                next_page = '0'
            )
        else :
            return ListGroupsOutput(
        )

    def testListGroupsOutput(self):
        """Test ListGroupsOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
