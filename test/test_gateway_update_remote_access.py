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
from akeyless.models.gateway_update_remote_access import GatewayUpdateRemoteAccess  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateRemoteAccess(unittest.TestCase):
    """GatewayUpdateRemoteAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateRemoteAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_remote_access.GatewayUpdateRemoteAccess()  # noqa: E501
        if include_optional :
            return GatewayUpdateRemoteAccess(
                allowed_urls = 'use-existing', 
                hide_session_recording = '0', 
                json = True, 
                kexalgs = 'use-existing', 
                keyboard_layout = 'use-existing', 
                legacy_ssh_algorithm = '0', 
                rdp_target_configuration = 'use-existing', 
                ssh_target_configuration = 'use-existing', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return GatewayUpdateRemoteAccess(
        )

    def testGatewayUpdateRemoteAccess(self):
        """Test GatewayUpdateRemoteAccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()