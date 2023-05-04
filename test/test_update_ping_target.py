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
from akeyless.models.update_ping_target import UpdatePingTarget  # noqa: E501
from akeyless.rest import ApiException

class TestUpdatePingTarget(unittest.TestCase):
    """UpdatePingTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdatePingTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_ping_target.UpdatePingTarget()  # noqa: E501
        if include_optional :
            return UpdatePingTarget(
                administrative_port = '9999', 
                authorization_port = '9031', 
                comment = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                ping_url = '0', 
                privileged_user = '0', 
                token = '0', 
                uid_token = '0', 
                update_version = True
            )
        else :
            return UpdatePingTarget(
                name = '0',
        )

    def testUpdatePingTarget(self):
        """Test UpdatePingTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()