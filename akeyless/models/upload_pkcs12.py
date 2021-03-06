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


class UploadPKCS12(object):
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
        'customer_frg_id': 'str',
        '_in': 'str',
        'metadata': 'str',
        'name': 'str',
        'passphrase': 'str',
        'password': 'str',
        'split_level': 'int',
        'tag': 'list[str]',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'customer_frg_id': 'customer-frg-id',
        '_in': 'in',
        'metadata': 'metadata',
        'name': 'name',
        'passphrase': 'passphrase',
        'password': 'password',
        'split_level': 'split-level',
        'tag': 'tag',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, customer_frg_id=None, _in=None, metadata=None, name=None, passphrase=None, password=None, split_level=2, tag=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UploadPKCS12 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_frg_id = None
        self.__in = None
        self._metadata = None
        self._name = None
        self._passphrase = None
        self._password = None
        self._split_level = None
        self._tag = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if customer_frg_id is not None:
            self.customer_frg_id = customer_frg_id
        self._in = _in
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.passphrase = passphrase
        if password is not None:
            self.password = password
        if split_level is not None:
            self.split_level = split_level
        if tag is not None:
            self.tag = tag
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def customer_frg_id(self):
        """Gets the customer_frg_id of this UploadPKCS12.  # noqa: E501

        The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :return: The customer_frg_id of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._customer_frg_id

    @customer_frg_id.setter
    def customer_frg_id(self, customer_frg_id):
        """Sets the customer_frg_id of this UploadPKCS12.

        The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :param customer_frg_id: The customer_frg_id of this UploadPKCS12.  # noqa: E501
        :type: str
        """

        self._customer_frg_id = customer_frg_id

    @property
    def _in(self):
        """Gets the _in of this UploadPKCS12.  # noqa: E501

        PKCS#12 input file (private key and certificate only)  # noqa: E501

        :return: The _in of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this UploadPKCS12.

        PKCS#12 input file (private key and certificate only)  # noqa: E501

        :param _in: The _in of this UploadPKCS12.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and _in is None:  # noqa: E501
            raise ValueError("Invalid value for `_in`, must not be `None`")  # noqa: E501

        self.__in = _in

    @property
    def metadata(self):
        """Gets the metadata of this UploadPKCS12.  # noqa: E501

        A metadata about the key  # noqa: E501

        :return: The metadata of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UploadPKCS12.

        A metadata about the key  # noqa: E501

        :param metadata: The metadata of this UploadPKCS12.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this UploadPKCS12.  # noqa: E501

        Name of key to be created  # noqa: E501

        :return: The name of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadPKCS12.

        Name of key to be created  # noqa: E501

        :param name: The name of this UploadPKCS12.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def passphrase(self):
        """Gets the passphrase of this UploadPKCS12.  # noqa: E501

        Passphrase to unlock the pkcs#12 bundle  # noqa: E501

        :return: The passphrase of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this UploadPKCS12.

        Passphrase to unlock the pkcs#12 bundle  # noqa: E501

        :param passphrase: The passphrase of this UploadPKCS12.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and passphrase is None:  # noqa: E501
            raise ValueError("Invalid value for `passphrase`, must not be `None`")  # noqa: E501

        self._passphrase = passphrase

    @property
    def password(self):
        """Gets the password of this UploadPKCS12.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UploadPKCS12.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this UploadPKCS12.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def split_level(self):
        """Gets the split_level of this UploadPKCS12.  # noqa: E501

        The number of fragments that the item will be split into  # noqa: E501

        :return: The split_level of this UploadPKCS12.  # noqa: E501
        :rtype: int
        """
        return self._split_level

    @split_level.setter
    def split_level(self, split_level):
        """Sets the split_level of this UploadPKCS12.

        The number of fragments that the item will be split into  # noqa: E501

        :param split_level: The split_level of this UploadPKCS12.  # noqa: E501
        :type: int
        """

        self._split_level = split_level

    @property
    def tag(self):
        """Gets the tag of this UploadPKCS12.  # noqa: E501

        List of the tags attached to this key  # noqa: E501

        :return: The tag of this UploadPKCS12.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this UploadPKCS12.

        List of the tags attached to this key  # noqa: E501

        :param tag: The tag of this UploadPKCS12.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def token(self):
        """Gets the token of this UploadPKCS12.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UploadPKCS12.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UploadPKCS12.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UploadPKCS12.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UploadPKCS12.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UploadPKCS12.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this UploadPKCS12.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this UploadPKCS12.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UploadPKCS12.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this UploadPKCS12.  # noqa: E501
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
        if not isinstance(other, UploadPKCS12):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadPKCS12):
            return True

        return self.to_dict() != other.to_dict()
