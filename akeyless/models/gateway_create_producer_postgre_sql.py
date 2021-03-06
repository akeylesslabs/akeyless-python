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


class GatewayCreateProducerPostgreSQL(object):
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
        'creation_statements': 'str',
        'name': 'str',
        'password': 'str',
        'postgresql_db_name': 'str',
        'postgresql_host': 'str',
        'postgresql_password': 'str',
        'postgresql_port': 'str',
        'postgresql_username': 'str',
        'producer_encryption_key': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'creation_statements': 'creation-statements',
        'name': 'name',
        'password': 'password',
        'postgresql_db_name': 'postgresql-db-name',
        'postgresql_host': 'postgresql-host',
        'postgresql_password': 'postgresql-password',
        'postgresql_port': 'postgresql-port',
        'postgresql_username': 'postgresql-username',
        'producer_encryption_key': 'producer-encryption-key',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, creation_statements=None, name=None, password=None, postgresql_db_name=None, postgresql_host='127.0.0.1', postgresql_password=None, postgresql_port='5432', postgresql_username=None, producer_encryption_key=None, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerPostgreSQL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_statements = None
        self._name = None
        self._password = None
        self._postgresql_db_name = None
        self._postgresql_host = None
        self._postgresql_password = None
        self._postgresql_port = None
        self._postgresql_username = None
        self._producer_encryption_key = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        if creation_statements is not None:
            self.creation_statements = creation_statements
        self.name = name
        if password is not None:
            self.password = password
        self.postgresql_db_name = postgresql_db_name
        if postgresql_host is not None:
            self.postgresql_host = postgresql_host
        self.postgresql_password = postgresql_password
        if postgresql_port is not None:
            self.postgresql_port = postgresql_port
        self.postgresql_username = postgresql_username
        if producer_encryption_key is not None:
            self.producer_encryption_key = producer_encryption_key
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if username is not None:
            self.username = username

    @property
    def creation_statements(self):
        """Gets the creation_statements of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL Creation statements  # noqa: E501

        :return: The creation_statements of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._creation_statements

    @creation_statements.setter
    def creation_statements(self, creation_statements):
        """Sets the creation_statements of this GatewayCreateProducerPostgreSQL.

        PostgreSQL Creation statements  # noqa: E501

        :param creation_statements: The creation_statements of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._creation_statements = creation_statements

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerPostgreSQL.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerPostgreSQL.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def postgresql_db_name(self):
        """Gets the postgresql_db_name of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL DB Name  # noqa: E501

        :return: The postgresql_db_name of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_db_name

    @postgresql_db_name.setter
    def postgresql_db_name(self, postgresql_db_name):
        """Sets the postgresql_db_name of this GatewayCreateProducerPostgreSQL.

        PostgreSQL DB Name  # noqa: E501

        :param postgresql_db_name: The postgresql_db_name of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and postgresql_db_name is None:  # noqa: E501
            raise ValueError("Invalid value for `postgresql_db_name`, must not be `None`")  # noqa: E501

        self._postgresql_db_name = postgresql_db_name

    @property
    def postgresql_host(self):
        """Gets the postgresql_host of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL Host  # noqa: E501

        :return: The postgresql_host of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_host

    @postgresql_host.setter
    def postgresql_host(self, postgresql_host):
        """Sets the postgresql_host of this GatewayCreateProducerPostgreSQL.

        PostgreSQL Host  # noqa: E501

        :param postgresql_host: The postgresql_host of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._postgresql_host = postgresql_host

    @property
    def postgresql_password(self):
        """Gets the postgresql_password of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL Password  # noqa: E501

        :return: The postgresql_password of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_password

    @postgresql_password.setter
    def postgresql_password(self, postgresql_password):
        """Sets the postgresql_password of this GatewayCreateProducerPostgreSQL.

        PostgreSQL Password  # noqa: E501

        :param postgresql_password: The postgresql_password of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and postgresql_password is None:  # noqa: E501
            raise ValueError("Invalid value for `postgresql_password`, must not be `None`")  # noqa: E501

        self._postgresql_password = postgresql_password

    @property
    def postgresql_port(self):
        """Gets the postgresql_port of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL Port  # noqa: E501

        :return: The postgresql_port of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_port

    @postgresql_port.setter
    def postgresql_port(self, postgresql_port):
        """Sets the postgresql_port of this GatewayCreateProducerPostgreSQL.

        PostgreSQL Port  # noqa: E501

        :param postgresql_port: The postgresql_port of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._postgresql_port = postgresql_port

    @property
    def postgresql_username(self):
        """Gets the postgresql_username of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        PostgreSQL Username  # noqa: E501

        :return: The postgresql_username of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_username

    @postgresql_username.setter
    def postgresql_username(self, postgresql_username):
        """Sets the postgresql_username of this GatewayCreateProducerPostgreSQL.

        PostgreSQL Username  # noqa: E501

        :param postgresql_username: The postgresql_username of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and postgresql_username is None:  # noqa: E501
            raise ValueError("Invalid value for `postgresql_username`, must not be `None`")  # noqa: E501

        self._postgresql_username = postgresql_username

    @property
    def producer_encryption_key(self):
        """Gets the producer_encryption_key of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key

    @producer_encryption_key.setter
    def producer_encryption_key(self, producer_encryption_key):
        """Sets the producer_encryption_key of this GatewayCreateProducerPostgreSQL.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key: The producer_encryption_key of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key = producer_encryption_key

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerPostgreSQL.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerPostgreSQL.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerPostgreSQL.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerPostgreSQL.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerPostgreSQL.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerPostgreSQL.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerPostgreSQL.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerPostgreSQL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerPostgreSQL):
            return True

        return self.to_dict() != other.to_dict()
