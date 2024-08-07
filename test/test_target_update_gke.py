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
from akeyless.models.target_update_gke import TargetUpdateGke  # noqa: E501
from akeyless.rest import ApiException

class TestTargetUpdateGke(unittest.TestCase):
    """TargetUpdateGke unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetUpdateGke
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_update_gke.TargetUpdateGke()  # noqa: E501
        if include_optional :
            return TargetUpdateGke(
                description = '0', 
                gke_account_key = '0', 
                gke_cluster_cert = '0', 
                gke_cluster_endpoint = '0', 
                gke_cluster_name = '0', 
                gke_service_account_email = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                max_versions = '0', 
                name = '0', 
                new_name = '0', 
                token = '0', 
                uid_token = '0', 
                use_gw_cloud_identity = True
            )
        else :
            return TargetUpdateGke(
                name = '0',
        )

    def testTargetUpdateGke(self):
        """Test TargetUpdateGke"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
