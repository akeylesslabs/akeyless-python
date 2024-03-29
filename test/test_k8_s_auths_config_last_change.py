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
from akeyless.models.k8_s_auths_config_last_change import K8SAuthsConfigLastChange  # noqa: E501
from akeyless.rest import ApiException

class TestK8SAuthsConfigLastChange(unittest.TestCase):
    """K8SAuthsConfigLastChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test K8SAuthsConfigLastChange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.k8_s_auths_config_last_change.K8SAuthsConfigLastChange()  # noqa: E501
        if include_optional :
            return K8SAuthsConfigLastChange(
                changed_k8s_auths_ids = [
                    '0'
                    ], 
                created_k8s_auths_ids = [
                    '0'
                    ], 
                deleted_k8s_auths_ids = [
                    '0'
                    ]
            )
        else :
            return K8SAuthsConfigLastChange(
        )

    def testK8SAuthsConfigLastChange(self):
        """Test K8SAuthsConfigLastChange"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
