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
from akeyless.models.bastions_list import BastionsList  # noqa: E501
from akeyless.rest import ApiException

class TestBastionsList(unittest.TestCase):
    """BastionsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BastionsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.bastions_list.BastionsList()  # noqa: E501
        if include_optional :
            return BastionsList(
                clusters = [
                    akeyless.models.bastion_list_entry.BastionListEntry(
                        access_id = '0', 
                        allowed_access_ids = [
                            '0'
                            ], 
                        allowed_urls = [
                            '0'
                            ], 
                        cluster_name = '0', 
                        display_name = '0', 
                        last_report = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return BastionsList(
        )

    def testBastionsList(self):
        """Test BastionsList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
