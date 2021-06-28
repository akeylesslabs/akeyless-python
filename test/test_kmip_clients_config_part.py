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
from akeyless.models.kmip_clients_config_part import KMIPClientsConfigPart  # noqa: E501
from akeyless.rest import ApiException

class TestKMIPClientsConfigPart(unittest.TestCase):
    """KMIPClientsConfigPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KMIPClientsConfigPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.kmip_clients_config_part.KMIPClientsConfigPart()  # noqa: E501
        if include_optional :
            return KMIPClientsConfigPart(
                clients = {
                    'key' : akeyless.models.kmip_client.KMIPClient(
                        name = '0', 
                        rules = [
                            akeyless.models.path_rule_is_a_single_rule_used_in_akeyless_rbac/.PathRule is a single rule used in AKEYLESS RBAC.(
                                capabilities = [
                                    '0'
                                    ], 
                                path = '0', 
                                type = '0', )
                            ], )
                    }
            )
        else :
            return KMIPClientsConfigPart(
        )

    def testKMIPClientsConfigPart(self):
        """Test KMIPClientsConfigPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()