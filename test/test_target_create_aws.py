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
from akeyless.models.target_create_aws import TargetCreateAws  # noqa: E501
from akeyless.rest import ApiException

class TestTargetCreateAws(unittest.TestCase):
    """TargetCreateAws unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetCreateAws
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_create_aws.TargetCreateAws()  # noqa: E501
        if include_optional :
            return TargetCreateAws(
                access_key = '0', 
                access_key_id = '0', 
                description = '0', 
                json = True, 
                key = '0', 
                max_versions = '0', 
                name = '0', 
                region = 'us-east-2', 
                session_token = '0', 
                token = '0', 
                uid_token = '0', 
                use_gw_cloud_identity = True
            )
        else :
            return TargetCreateAws(
                access_key = '0',
                access_key_id = '0',
                name = '0',
        )

    def testTargetCreateAws(self):
        """Test TargetCreateAws"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
