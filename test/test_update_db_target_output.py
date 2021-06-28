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
from akeyless.models.update_db_target_output import UpdateDBTargetOutput  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateDBTargetOutput(unittest.TestCase):
    """UpdateDBTargetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateDBTargetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_db_target_output.UpdateDBTargetOutput()  # noqa: E501
        if include_optional :
            return UpdateDBTargetOutput(
                target_id = 56
            )
        else :
            return UpdateDBTargetOutput(
        )

    def testUpdateDBTargetOutput(self):
        """Test UpdateDBTargetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()