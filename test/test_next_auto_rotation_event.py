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
from akeyless.models.next_auto_rotation_event import NextAutoRotationEvent  # noqa: E501
from akeyless.rest import ApiException

class TestNextAutoRotationEvent(unittest.TestCase):
    """NextAutoRotationEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NextAutoRotationEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.next_auto_rotation_event.NextAutoRotationEvent()  # noqa: E501
        if include_optional :
            return NextAutoRotationEvent(
                seconds_before = 56
            )
        else :
            return NextAutoRotationEvent(
        )

    def testNextAutoRotationEvent(self):
        """Test NextAutoRotationEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()