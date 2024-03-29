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
from akeyless.models.active_directory_payload import ActiveDirectoryPayload  # noqa: E501
from akeyless.rest import ApiException

class TestActiveDirectoryPayload(unittest.TestCase):
    """ActiveDirectoryPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActiveDirectoryPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.active_directory_payload.ActiveDirectoryPayload()  # noqa: E501
        if include_optional :
            return ActiveDirectoryPayload(
                active_directory_target_id = 56, 
                auto_rotate = True, 
                auto_rotate_interval_in_days = 56, 
                auto_rotate_rotation_hour = 56, 
                computer_base_dn = '0', 
                discover_local_users = True, 
                domain_name = '0', 
                domain_server_targets_path_template = '0', 
                domain_users_rotated_secrets_path_template = '0', 
                enable_rdp_sra = True, 
                local_users_ignore_list = {
                    'key' : True
                    }, 
                local_users_rotated_secrets_path_template = '0', 
                ssh_port = '0', 
                user_base_dn = '0', 
                user_groups = [
                    '0'
                    ]
            )
        else :
            return ActiveDirectoryPayload(
        )

    def testActiveDirectoryPayload(self):
        """Test ActiveDirectoryPayload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
