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


class CreateGlobalSignAtlasTarget(object):
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
        'api_key': 'str',
        'api_secret': 'str',
        'comment': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'mtls_cert_data_base64': 'str',
        'mtls_key_data_base64': 'str',
        'name': 'str',
        'timeout': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'api_key': 'api-key',
        'api_secret': 'api-secret',
        'comment': 'comment',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'mtls_cert_data_base64': 'mtls-cert-data-base64',
        'mtls_key_data_base64': 'mtls-key-data-base64',
        'name': 'name',
        'timeout': 'timeout',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, api_key=None, api_secret=None, comment=None, description=None, json=False, key=None, mtls_cert_data_base64=None, mtls_key_data_base64=None, name=None, timeout='5m', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateGlobalSignAtlasTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key = None
        self._api_secret = None
        self._comment = None
        self._description = None
        self._json = None
        self._key = None
        self._mtls_cert_data_base64 = None
        self._mtls_key_data_base64 = None
        self._name = None
        self._timeout = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.api_key = api_key
        self.api_secret = api_secret
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if mtls_cert_data_base64 is not None:
            self.mtls_cert_data_base64 = mtls_cert_data_base64
        if mtls_key_data_base64 is not None:
            self.mtls_key_data_base64 = mtls_key_data_base64
        self.name = name
        if timeout is not None:
            self.timeout = timeout
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def api_key(self):
        """Gets the api_key of this CreateGlobalSignAtlasTarget.  # noqa: E501

        API Key of the GlobalSign Atlas account  # noqa: E501

        :return: The api_key of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this CreateGlobalSignAtlasTarget.

        API Key of the GlobalSign Atlas account  # noqa: E501

        :param api_key: The api_key of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def api_secret(self):
        """Gets the api_secret of this CreateGlobalSignAtlasTarget.  # noqa: E501

        API Secret of the GlobalSign Atlas account  # noqa: E501

        :return: The api_secret of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this CreateGlobalSignAtlasTarget.

        API Secret of the GlobalSign Atlas account  # noqa: E501

        :param api_secret: The api_secret of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `api_secret`, must not be `None`")  # noqa: E501

        self._api_secret = api_secret

    @property
    def comment(self):
        """Gets the comment of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateGlobalSignAtlasTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGlobalSignAtlasTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateGlobalSignAtlasTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateGlobalSignAtlasTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateGlobalSignAtlasTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def mtls_cert_data_base64(self):
        """Gets the mtls_cert_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Mutual TLS Certificate contents of the GlobalSign Atlas account encoded in base64, either mtls-cert-file-path or mtls-cert-data-base64 must be supplied  # noqa: E501

        :return: The mtls_cert_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._mtls_cert_data_base64

    @mtls_cert_data_base64.setter
    def mtls_cert_data_base64(self, mtls_cert_data_base64):
        """Sets the mtls_cert_data_base64 of this CreateGlobalSignAtlasTarget.

        Mutual TLS Certificate contents of the GlobalSign Atlas account encoded in base64, either mtls-cert-file-path or mtls-cert-data-base64 must be supplied  # noqa: E501

        :param mtls_cert_data_base64: The mtls_cert_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._mtls_cert_data_base64 = mtls_cert_data_base64

    @property
    def mtls_key_data_base64(self):
        """Gets the mtls_key_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Mutual TLS Key contents of the GlobalSign Atlas account encoded in base64, either mtls-key-file-path or mtls-data-base64 must be supplied  # noqa: E501

        :return: The mtls_key_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._mtls_key_data_base64

    @mtls_key_data_base64.setter
    def mtls_key_data_base64(self, mtls_key_data_base64):
        """Sets the mtls_key_data_base64 of this CreateGlobalSignAtlasTarget.

        Mutual TLS Key contents of the GlobalSign Atlas account encoded in base64, either mtls-key-file-path or mtls-data-base64 must be supplied  # noqa: E501

        :param mtls_key_data_base64: The mtls_key_data_base64 of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._mtls_key_data_base64 = mtls_key_data_base64

    @property
    def name(self):
        """Gets the name of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGlobalSignAtlasTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def timeout(self):
        """Gets the timeout of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :return: The timeout of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateGlobalSignAtlasTarget.

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :param timeout: The timeout of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def token(self):
        """Gets the token of this CreateGlobalSignAtlasTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateGlobalSignAtlasTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateGlobalSignAtlasTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateGlobalSignAtlasTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateGlobalSignAtlasTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateGlobalSignAtlasTarget.  # noqa: E501
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
        if not isinstance(other, CreateGlobalSignAtlasTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGlobalSignAtlasTarget):
            return True

        return self.to_dict() != other.to_dict()