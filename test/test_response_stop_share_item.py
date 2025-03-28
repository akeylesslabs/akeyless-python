# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from akeyless.models.response_stop_share_item import ResponseStopShareItem

class TestResponseStopShareItem(unittest.TestCase):
    """ResponseStopShareItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseStopShareItem:
        """Test ResponseStopShareItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseStopShareItem`
        """
        model = ResponseStopShareItem()
        if include_optional:
            return ResponseStopShareItem(
                errors = [
                    akeyless.models.email_error.EmailError(
                        email = '', 
                        error = '', 
                        token = '', )
                    ],
                item_name = ''
            )
        else:
            return ResponseStopShareItem(
        )
        """

    def testResponseStopShareItem(self):
        """Test ResponseStopShareItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
