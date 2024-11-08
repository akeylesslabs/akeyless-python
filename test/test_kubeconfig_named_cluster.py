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
from akeyless.models.kubeconfig_named_cluster import KubeconfigNamedCluster  # noqa: E501
from akeyless.rest import ApiException

class TestKubeconfigNamedCluster(unittest.TestCase):
    """KubeconfigNamedCluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeconfigNamedCluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.kubeconfig_named_cluster.KubeconfigNamedCluster()  # noqa: E501
        if include_optional :
            return KubeconfigNamedCluster(
                cluster = akeyless.models.kubeconfig_cluster_represents_the_cluster_details/.KubeconfigCluster represents the cluster details.(
                    certificate_authority = '0', 
                    certificate_authority_data = '0', 
                    server = '0', ), 
                name = '0'
            )
        else :
            return KubeconfigNamedCluster(
        )

    def testKubeconfigNamedCluster(self):
        """Test KubeconfigNamedCluster"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
