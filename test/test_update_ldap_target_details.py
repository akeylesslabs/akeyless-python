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
from akeyless.models.update_ldap_target_details import UpdateLdapTargetDetails  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateLdapTargetDetails(unittest.TestCase):
    """UpdateLdapTargetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateLdapTargetDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_ldap_target_details.UpdateLdapTargetDetails()  # noqa: E501
        if include_optional :
            return UpdateLdapTargetDetails(
                bind_dn = '0', 
                bind_dn_password = '0', 
                keep_prev_version = '0', 
                key = '0', 
                ldap_ca_cert = '0', 
                ldap_url = '0', 
                name = '0', 
                new_version = True, 
                protection_key = '0', 
                token = '0', 
                token_expiration = '0', 
                uid_token = '0'
            )
        else :
            return UpdateLdapTargetDetails(
                name = '0',
        )

    def testUpdateLdapTargetDetails(self):
        """Test UpdateLdapTargetDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
