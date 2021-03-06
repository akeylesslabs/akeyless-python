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


class GatewayCreateProducerChef(object):
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
        'chef_orgs': 'str',
        'chef_server_key': 'str',
        'chef_server_url': 'str',
        'chef_server_username': 'str',
        'name': 'str',
        'password': 'str',
        'producer_encryption_key_name': 'str',
        'skip_ssl': 'bool',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'chef_orgs': 'chef-orgs',
        'chef_server_key': 'chef-server-key',
        'chef_server_url': 'chef-server-url',
        'chef_server_username': 'chef-server-username',
        'name': 'name',
        'password': 'password',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'skip_ssl': 'skip-ssl',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, chef_orgs=None, chef_server_key=None, chef_server_url=None, chef_server_username=None, name=None, password=None, producer_encryption_key_name=None, skip_ssl=True, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerChef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chef_orgs = None
        self._chef_server_key = None
        self._chef_server_url = None
        self._chef_server_username = None
        self._name = None
        self._password = None
        self._producer_encryption_key_name = None
        self._skip_ssl = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        self.chef_orgs = chef_orgs
        self.chef_server_key = chef_server_key
        self.chef_server_url = chef_server_url
        self.chef_server_username = chef_server_username
        self.name = name
        if password is not None:
            self.password = password
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if skip_ssl is not None:
            self.skip_ssl = skip_ssl
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if username is not None:
            self.username = username

    @property
    def chef_orgs(self):
        """Gets the chef_orgs of this GatewayCreateProducerChef.  # noqa: E501

        Organizations  # noqa: E501

        :return: The chef_orgs of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._chef_orgs

    @chef_orgs.setter
    def chef_orgs(self, chef_orgs):
        """Sets the chef_orgs of this GatewayCreateProducerChef.

        Organizations  # noqa: E501

        :param chef_orgs: The chef_orgs of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chef_orgs is None:  # noqa: E501
            raise ValueError("Invalid value for `chef_orgs`, must not be `None`")  # noqa: E501

        self._chef_orgs = chef_orgs

    @property
    def chef_server_key(self):
        """Gets the chef_server_key of this GatewayCreateProducerChef.  # noqa: E501

        Server key  # noqa: E501

        :return: The chef_server_key of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._chef_server_key

    @chef_server_key.setter
    def chef_server_key(self, chef_server_key):
        """Sets the chef_server_key of this GatewayCreateProducerChef.

        Server key  # noqa: E501

        :param chef_server_key: The chef_server_key of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chef_server_key is None:  # noqa: E501
            raise ValueError("Invalid value for `chef_server_key`, must not be `None`")  # noqa: E501

        self._chef_server_key = chef_server_key

    @property
    def chef_server_url(self):
        """Gets the chef_server_url of this GatewayCreateProducerChef.  # noqa: E501

        Server URL  # noqa: E501

        :return: The chef_server_url of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._chef_server_url

    @chef_server_url.setter
    def chef_server_url(self, chef_server_url):
        """Sets the chef_server_url of this GatewayCreateProducerChef.

        Server URL  # noqa: E501

        :param chef_server_url: The chef_server_url of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chef_server_url is None:  # noqa: E501
            raise ValueError("Invalid value for `chef_server_url`, must not be `None`")  # noqa: E501

        self._chef_server_url = chef_server_url

    @property
    def chef_server_username(self):
        """Gets the chef_server_username of this GatewayCreateProducerChef.  # noqa: E501

        Server username  # noqa: E501

        :return: The chef_server_username of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._chef_server_username

    @chef_server_username.setter
    def chef_server_username(self, chef_server_username):
        """Sets the chef_server_username of this GatewayCreateProducerChef.

        Server username  # noqa: E501

        :param chef_server_username: The chef_server_username of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chef_server_username is None:  # noqa: E501
            raise ValueError("Invalid value for `chef_server_username`, must not be `None`")  # noqa: E501

        self._chef_server_username = chef_server_username

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerChef.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerChef.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerChef.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerChef.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerChef.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerChef.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def skip_ssl(self):
        """Gets the skip_ssl of this GatewayCreateProducerChef.  # noqa: E501

        Skip SSL  # noqa: E501

        :return: The skip_ssl of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: bool
        """
        return self._skip_ssl

    @skip_ssl.setter
    def skip_ssl(self, skip_ssl):
        """Sets the skip_ssl of this GatewayCreateProducerChef.

        Skip SSL  # noqa: E501

        :param skip_ssl: The skip_ssl of this GatewayCreateProducerChef.  # noqa: E501
        :type: bool
        """

        self._skip_ssl = skip_ssl

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerChef.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerChef.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerChef.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerChef.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerChef.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerChef.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerChef.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerChef.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerChef.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerChef.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerChef.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerChef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerChef):
            return True

        return self.to_dict() != other.to_dict()
