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

from akeyless.models.share_item_output import ShareItemOutput

class TestShareItemOutput(unittest.TestCase):
    """ShareItemOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShareItemOutput:
        """Test ShareItemOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShareItemOutput`
        """
        model = ShareItemOutput()
        if include_optional:
            return ShareItemOutput(
                email_error = {
                    'key' : ''
                    },
                items_error = [
                    akeyless.models.response_stop_share_item.ResponseStopShareItem(
                        errors = [
                            akeyless.models.email_error.EmailError(
                                email = '', 
                                error = '', 
                                token = '', )
                            ], 
                        item_name = '', )
                    ],
                s_token = '',
                shared_users = [
                    ''
                    ],
                shared_users_full_info = [
                    akeyless.models.sharing_item_full_info.SharingItemFullInfo(
                        assigners = [
                            akeyless.models.rule_assigner.RuleAssigner(
                                access_id = '', 
                                unique_id = '', )
                            ], 
                        capabilities = [
                            ''
                            ], 
                        cb = 56, 
                        is_limit_access = True, 
                        name = '', 
                        number_of_access_used = 56, 
                        number_of_allowed_access = 56, 
                        path = '', 
                        start_time = 56, 
                        ttl = 56, 
                        type = '', )
                    ],
                sharing_url = ''
            )
        else:
            return ShareItemOutput(
        )
        """

    def testShareItemOutput(self):
        """Test ShareItemOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
