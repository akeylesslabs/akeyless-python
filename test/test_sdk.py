import os
import time
import unittest

import akeyless
from akeyless.rest import ApiException


class TestSDK(unittest.TestCase):
    def setUp(self):
        host = os.getenv('AKEYLESS_TEST_HOST')
        configuration = akeyless.Configuration(host=host)

        with akeyless.ApiClient(configuration) as api_client:
            self.api = akeyless.V2Api(api_client)

        self.access_id = os.getenv('AKEYLESS_TEST_ACCESS_ID')
        self.access_key = os.getenv('AKEYLESS_TEST_ACCESS_KEY')

        if not self.access_id or not self.access_key:
            self.fail("missing access credentials")

    def tearDown(self):
        pass

    def test_roles(self):
        t = time.time()

        body = akeyless.Auth(access_id=self.access_id, access_key=self.access_key)
        res = self.api.auth(body)
        token = res.token

        role_name = 'pyrole-{}'.format(t)
        body = akeyless.CreateRole(token=token, name=role_name)
        self.api.create_role(body)

        body = akeyless.SetRoleRule(capability=['list', 'read'], path='/pytest-item/*',
                role_name=role_name, token=token)

        for rule_type in ['role-rule', 'item-rule', 'auth-method-rule']:
            body.rule_type = rule_type
            self.api.set_role_rule(body)

        am_name = 'pyam-{}'.format(t)
        body = akeyless.CreateAuthMethod(name=am_name, token=token)
        res = self.api.create_auth_method(body)

        amID = res.access_id
        amKey = res.access_key

        body = akeyless.AssocRoleAuthMethod(am_name=am_name, role_name=role_name,
                token=token)
        self.api.assoc_role_auth_method(body)

        secret_name = '/pytest-item/secret-{}'.format(t)
        secret_value = 'secret-{}'.format(t)

        body = akeyless.CreateSecret(name=secret_name, value=secret_value, token=token)
        self.api.create_secret(body)

        body = akeyless.Auth(access_id=amID, access_key=amKey)
        res = self.api.auth(body)
        amToken = res.token

        body = akeyless.GetSecretValue(names=[secret_name], token=token)
        res = self.api.get_secret_value(body)
        self.assertEqual(res[secret_name], secret_value)

        body = akeyless.ListItems(token=amToken)
        res = self.api.list_items(body)
        self.assertTrue(len(res.items) > 0)

        for item in res.items:
            if item.item_name.startswith('/pytest-item/'):
                body = akeyless.DeleteItem(delete_immediately=True,
                        delete_in_days=-1, name=item.item_name, token=token)
                self.api.delete_item(body)

        body = akeyless.ListAuthMethods(token=token)
        res = self.api.list_auth_methods(body)

        for am in res.auth_methods:
            if am.auth_method_name.startswith('pyam'):
                body = akeyless.DeleteAuthMethod(token=token,
                        name=am.auth_method_name)
                self.api.delete_auth_method(body)

        body = akeyless.ListRoles(token=token)
        res = self.api.list_roles(body)

        for role in res.roles:
            if role.role_name.startswith('pyrole'):
                body = akeyless.DeleteRole(token=token,
                        name=role.role_name)
                self.api.delete_role(body)


if __name__ == "__main__":
    unittest.main()
