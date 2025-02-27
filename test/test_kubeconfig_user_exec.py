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
from akeyless.models.kubeconfig_user_exec import KubeconfigUserExec  # noqa: E501
from akeyless.rest import ApiException

class TestKubeconfigUserExec(unittest.TestCase):
    """KubeconfigUserExec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeconfigUserExec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.kubeconfig_user_exec.KubeconfigUserExec()  # noqa: E501
        if include_optional :
            return KubeconfigUserExec(
                _exec = akeyless.models.kubeconfig_exec_represents_the_exec_command_configuration/.KubeconfigExec represents the exec command configuration.(
                    api_version = '0', 
                    args = [
                        '0'
                        ], 
                    command = '0', 
                    interactive_mode = '0', )
            )
        else :
            return KubeconfigUserExec(
        )

    def testKubeconfigUserExec(self):
        """Test KubeconfigUserExec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
