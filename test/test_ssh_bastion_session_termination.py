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
from akeyless.models.ssh_bastion_session_termination import SshBastionSessionTermination  # noqa: E501
from akeyless.rest import ApiException

class TestSshBastionSessionTermination(unittest.TestCase):
    """SshBastionSessionTermination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SshBastionSessionTermination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.ssh_bastion_session_termination.SshBastionSessionTermination()  # noqa: E501
        if include_optional :
            return SshBastionSessionTermination(
                api_password = '0', 
                api_token = '0', 
                api_url = '0', 
                api_username = '0', 
                enabled = True
            )
        else :
            return SshBastionSessionTermination(
        )

    def testSshBastionSessionTermination(self):
        """Test SshBastionSessionTermination"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()