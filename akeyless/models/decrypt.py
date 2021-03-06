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


class Decrypt(object):
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
        'ciphertext': 'str',
        'display_id': 'str',
        'encryption_context': 'dict(str, str)',
        'key_name': 'str',
        'password': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'ciphertext': 'ciphertext',
        'display_id': 'display-id',
        'encryption_context': 'encryption-context',
        'key_name': 'key-name',
        'password': 'password',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, ciphertext=None, display_id=None, encryption_context=None, key_name=None, password=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """Decrypt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ciphertext = None
        self._display_id = None
        self._encryption_context = None
        self._key_name = None
        self._password = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        self.ciphertext = ciphertext
        if display_id is not None:
            self.display_id = display_id
        if encryption_context is not None:
            self.encryption_context = encryption_context
        if key_name is not None:
            self.key_name = key_name
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def ciphertext(self):
        """Gets the ciphertext of this Decrypt.  # noqa: E501

        Ciphertext to be decrypted in base64 encoded format  # noqa: E501

        :return: The ciphertext of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, ciphertext):
        """Sets the ciphertext of this Decrypt.

        Ciphertext to be decrypted in base64 encoded format  # noqa: E501

        :param ciphertext: The ciphertext of this Decrypt.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ciphertext is None:  # noqa: E501
            raise ValueError("Invalid value for `ciphertext`, must not be `None`")  # noqa: E501

        self._ciphertext = ciphertext

    @property
    def display_id(self):
        """Gets the display_id of this Decrypt.  # noqa: E501

        The display id of the key to use in the decryption process  # noqa: E501

        :return: The display_id of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this Decrypt.

        The display id of the key to use in the decryption process  # noqa: E501

        :param display_id: The display_id of this Decrypt.  # noqa: E501
        :type: str
        """

        self._display_id = display_id

    @property
    def encryption_context(self):
        """Gets the encryption_context of this Decrypt.  # noqa: E501

        The encryption context. If this was specified in the encrypt command, it must be specified here or the decryption operation will fail  # noqa: E501

        :return: The encryption_context of this Decrypt.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._encryption_context

    @encryption_context.setter
    def encryption_context(self, encryption_context):
        """Sets the encryption_context of this Decrypt.

        The encryption context. If this was specified in the encrypt command, it must be specified here or the decryption operation will fail  # noqa: E501

        :param encryption_context: The encryption_context of this Decrypt.  # noqa: E501
        :type: dict(str, str)
        """

        self._encryption_context = encryption_context

    @property
    def key_name(self):
        """Gets the key_name of this Decrypt.  # noqa: E501

        The name of the key to use in the decryption process  # noqa: E501

        :return: The key_name of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this Decrypt.

        The name of the key to use in the decryption process  # noqa: E501

        :param key_name: The key_name of this Decrypt.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def password(self):
        """Gets the password of this Decrypt.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Decrypt.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this Decrypt.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this Decrypt.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Decrypt.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this Decrypt.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this Decrypt.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this Decrypt.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this Decrypt.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this Decrypt.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this Decrypt.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Decrypt.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this Decrypt.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, Decrypt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Decrypt):
            return True

        return self.to_dict() != other.to_dict()
