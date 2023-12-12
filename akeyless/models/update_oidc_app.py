# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class UpdateOidcApp(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'audience': 'str',
        'json': 'bool',
        'key': 'str',
        'name': 'str',
        'permission_assignment': 'str',
        'public': 'bool',
        'redirect_uris': 'str',
        'scopes': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'json': 'json',
        'key': 'key',
        'name': 'name',
        'permission_assignment': 'permission-assignment',
        'public': 'public',
        'redirect_uris': 'redirect-uris',
        'scopes': 'scopes',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, audience=None, json=False, key=None, name=None, permission_assignment=None, public=None, redirect_uris=None, scopes='openid', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateOidcApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._json = None
        self._key = None
        self._name = None
        self._permission_assignment = None
        self._public = None
        self._redirect_uris = None
        self._scopes = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if audience is not None:
            self.audience = audience
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        self.name = name
        if permission_assignment is not None:
            self.permission_assignment = permission_assignment
        if public is not None:
            self.public = public
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if scopes is not None:
            self.scopes = scopes
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def audience(self):
        """Gets the audience of this UpdateOidcApp.  # noqa: E501

        A comma separated list of allowed audiences  # noqa: E501

        :return: The audience of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this UpdateOidcApp.

        A comma separated list of allowed audiences  # noqa: E501

        :param audience: The audience of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def json(self):
        """Gets the json of this UpdateOidcApp.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateOidcApp.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateOidcApp.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateOidcApp.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this UpdateOidcApp.  # noqa: E501

        The name of a key that used to encrypt the OIDC application (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateOidcApp.

        The name of a key that used to encrypt the OIDC application (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateOidcApp.  # noqa: E501

        OIDC application name  # noqa: E501

        :return: The name of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateOidcApp.

        OIDC application name  # noqa: E501

        :param name: The name of this UpdateOidcApp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permission_assignment(self):
        """Gets the permission_assignment of this UpdateOidcApp.  # noqa: E501

        A json string defining the access permission assignment for this app  # noqa: E501

        :return: The permission_assignment of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._permission_assignment

    @permission_assignment.setter
    def permission_assignment(self, permission_assignment):
        """Sets the permission_assignment of this UpdateOidcApp.

        A json string defining the access permission assignment for this app  # noqa: E501

        :param permission_assignment: The permission_assignment of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._permission_assignment = permission_assignment

    @property
    def public(self):
        """Gets the public of this UpdateOidcApp.  # noqa: E501

        Set to true if the app is public (cannot keep secrets)  # noqa: E501

        :return: The public of this UpdateOidcApp.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this UpdateOidcApp.

        Set to true if the app is public (cannot keep secrets)  # noqa: E501

        :param public: The public of this UpdateOidcApp.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this UpdateOidcApp.  # noqa: E501

        A comma separated list of allowed redirect uris  # noqa: E501

        :return: The redirect_uris of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this UpdateOidcApp.

        A comma separated list of allowed redirect uris  # noqa: E501

        :param redirect_uris: The redirect_uris of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._redirect_uris = redirect_uris

    @property
    def scopes(self):
        """Gets the scopes of this UpdateOidcApp.  # noqa: E501

        A comma separated list of allowed scopes  # noqa: E501

        :return: The scopes of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this UpdateOidcApp.

        A comma separated list of allowed scopes  # noqa: E501

        :param scopes: The scopes of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._scopes = scopes

    @property
    def token(self):
        """Gets the token of this UpdateOidcApp.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateOidcApp.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateOidcApp.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateOidcApp.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateOidcApp.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateOidcApp.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateOidcApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateOidcApp):
            return True

        return self.to_dict() != other.to_dict()