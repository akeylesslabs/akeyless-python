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
from akeyless.models.target_update_sectigo import TargetUpdateSectigo  # noqa: E501
from akeyless.rest import ApiException

class TestTargetUpdateSectigo(unittest.TestCase):
    """TargetUpdateSectigo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetUpdateSectigo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_update_sectigo.TargetUpdateSectigo()  # noqa: E501
        if include_optional :
            return TargetUpdateSectigo(
                certificate_profile_id = 56, 
                customer_uri = '0', 
                description = '0', 
                external_requester = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                max_versions = '0', 
                name = '0', 
                new_name = '0', 
                organization_id = 56, 
                password = '0', 
                timeout = '5m', 
                token = '0', 
                uid_token = '0', 
                username = '0'
            )
        else :
            return TargetUpdateSectigo(
                certificate_profile_id = 56,
                customer_uri = '0',
                external_requester = '0',
                name = '0',
                organization_id = 56,
                password = '0',
                username = '0',
        )

    def testTargetUpdateSectigo(self):
        """Test TargetUpdateSectigo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()