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
from akeyless.models.update_global_sign_atlas_target import UpdateGlobalSignAtlasTarget  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateGlobalSignAtlasTarget(unittest.TestCase):
    """UpdateGlobalSignAtlasTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateGlobalSignAtlasTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_global_sign_atlas_target.UpdateGlobalSignAtlasTarget()  # noqa: E501
        if include_optional :
            return UpdateGlobalSignAtlasTarget(
                api_key = '0', 
                api_secret = '0', 
                comment = '0', 
                description = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                mtls_cert_data_base64 = '0', 
                mtls_key_data_base64 = '0', 
                name = '0', 
                new_name = '0', 
                timeout = '5m', 
                token = '0', 
                uid_token = '0', 
                update_version = True
            )
        else :
            return UpdateGlobalSignAtlasTarget(
                api_key = '0',
                api_secret = '0',
                name = '0',
        )

    def testUpdateGlobalSignAtlasTarget(self):
        """Test UpdateGlobalSignAtlasTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
