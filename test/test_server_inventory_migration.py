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
from akeyless.models.server_inventory_migration import ServerInventoryMigration  # noqa: E501
from akeyless.rest import ApiException

class TestServerInventoryMigration(unittest.TestCase):
    """ServerInventoryMigration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServerInventoryMigration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.server_inventory_migration.ServerInventoryMigration()  # noqa: E501
        if include_optional :
            return ServerInventoryMigration(
                general = akeyless.models.migration_general.MigrationGeneral(
                    id = '0', 
                    name = '0', 
                    new_name = '0', 
                    prefix = '0', 
                    protection_key = '0', 
                    status = '0', 
                    type = '0', ), 
                payload = akeyless.models.server_inventory_payload.ServerInventoryPayload(
                    auto_rotate = True, 
                    auto_rotate_interval_in_days = 56, 
                    auto_rotate_rotation_hour = 56, 
                    enable_rdp_sra = True, 
                    migration_target_id = 56, 
                    server_targets_path_template = '0', 
                    users_ignore_list = {
                        'key' : True
                        }, 
                    users_rotated_secrets_path_template = '0', )
            )
        else :
            return ServerInventoryMigration(
        )

    def testServerInventoryMigration(self):
        """Test ServerInventoryMigration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()