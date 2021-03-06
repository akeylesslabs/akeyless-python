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


class GatewayCreateProducerMSSQL(object):
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
        'mssql_create_statements': 'str',
        'mssql_dbname': 'str',
        'mssql_host': 'str',
        'mssql_password': 'str',
        'mssql_port': 'str',
        'mssql_revocation_statements': 'str',
        'mssql_username': 'str',
        'name': 'str',
        'password': 'str',
        'producer_encryption_key_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'mssql_create_statements': 'mssql-create-statements',
        'mssql_dbname': 'mssql-dbname',
        'mssql_host': 'mssql-host',
        'mssql_password': 'mssql-password',
        'mssql_port': 'mssql-port',
        'mssql_revocation_statements': 'mssql-revocation-statements',
        'mssql_username': 'mssql-username',
        'name': 'name',
        'password': 'password',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, mssql_create_statements=None, mssql_dbname=None, mssql_host='127.0.0.1', mssql_password=None, mssql_port='1433', mssql_revocation_statements=None, mssql_username=None, name=None, password=None, producer_encryption_key_name=None, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerMSSQL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mssql_create_statements = None
        self._mssql_dbname = None
        self._mssql_host = None
        self._mssql_password = None
        self._mssql_port = None
        self._mssql_revocation_statements = None
        self._mssql_username = None
        self._name = None
        self._password = None
        self._producer_encryption_key_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        if mssql_create_statements is not None:
            self.mssql_create_statements = mssql_create_statements
        self.mssql_dbname = mssql_dbname
        if mssql_host is not None:
            self.mssql_host = mssql_host
        self.mssql_password = mssql_password
        if mssql_port is not None:
            self.mssql_port = mssql_port
        if mssql_revocation_statements is not None:
            self.mssql_revocation_statements = mssql_revocation_statements
        self.mssql_username = mssql_username
        self.name = name
        if password is not None:
            self.password = password
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if username is not None:
            self.username = username

    @property
    def mssql_create_statements(self):
        """Gets the mssql_create_statements of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Creation statements  # noqa: E501

        :return: The mssql_create_statements of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_create_statements

    @mssql_create_statements.setter
    def mssql_create_statements(self, mssql_create_statements):
        """Sets the mssql_create_statements of this GatewayCreateProducerMSSQL.

        MSSQL Creation statements  # noqa: E501

        :param mssql_create_statements: The mssql_create_statements of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._mssql_create_statements = mssql_create_statements

    @property
    def mssql_dbname(self):
        """Gets the mssql_dbname of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Name  # noqa: E501

        :return: The mssql_dbname of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_dbname

    @mssql_dbname.setter
    def mssql_dbname(self, mssql_dbname):
        """Sets the mssql_dbname of this GatewayCreateProducerMSSQL.

        MSSQL Name  # noqa: E501

        :param mssql_dbname: The mssql_dbname of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mssql_dbname is None:  # noqa: E501
            raise ValueError("Invalid value for `mssql_dbname`, must not be `None`")  # noqa: E501

        self._mssql_dbname = mssql_dbname

    @property
    def mssql_host(self):
        """Gets the mssql_host of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Host  # noqa: E501

        :return: The mssql_host of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_host

    @mssql_host.setter
    def mssql_host(self, mssql_host):
        """Sets the mssql_host of this GatewayCreateProducerMSSQL.

        MSSQL Host  # noqa: E501

        :param mssql_host: The mssql_host of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._mssql_host = mssql_host

    @property
    def mssql_password(self):
        """Gets the mssql_password of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Password  # noqa: E501

        :return: The mssql_password of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_password

    @mssql_password.setter
    def mssql_password(self, mssql_password):
        """Sets the mssql_password of this GatewayCreateProducerMSSQL.

        MSSQL Password  # noqa: E501

        :param mssql_password: The mssql_password of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mssql_password is None:  # noqa: E501
            raise ValueError("Invalid value for `mssql_password`, must not be `None`")  # noqa: E501

        self._mssql_password = mssql_password

    @property
    def mssql_port(self):
        """Gets the mssql_port of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Port  # noqa: E501

        :return: The mssql_port of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_port

    @mssql_port.setter
    def mssql_port(self, mssql_port):
        """Sets the mssql_port of this GatewayCreateProducerMSSQL.

        MSSQL Port  # noqa: E501

        :param mssql_port: The mssql_port of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._mssql_port = mssql_port

    @property
    def mssql_revocation_statements(self):
        """Gets the mssql_revocation_statements of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Revocation statements  # noqa: E501

        :return: The mssql_revocation_statements of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_revocation_statements

    @mssql_revocation_statements.setter
    def mssql_revocation_statements(self, mssql_revocation_statements):
        """Sets the mssql_revocation_statements of this GatewayCreateProducerMSSQL.

        MSSQL Revocation statements  # noqa: E501

        :param mssql_revocation_statements: The mssql_revocation_statements of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._mssql_revocation_statements = mssql_revocation_statements

    @property
    def mssql_username(self):
        """Gets the mssql_username of this GatewayCreateProducerMSSQL.  # noqa: E501

        MSSQL Username  # noqa: E501

        :return: The mssql_username of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._mssql_username

    @mssql_username.setter
    def mssql_username(self, mssql_username):
        """Sets the mssql_username of this GatewayCreateProducerMSSQL.

        MSSQL Username  # noqa: E501

        :param mssql_username: The mssql_username of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mssql_username is None:  # noqa: E501
            raise ValueError("Invalid value for `mssql_username`, must not be `None`")  # noqa: E501

        self._mssql_username = mssql_username

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerMSSQL.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerMSSQL.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerMSSQL.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerMSSQL.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerMSSQL.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerMSSQL.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerMSSQL.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerMSSQL.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerMSSQL.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerMSSQL.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerMSSQL.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerMSSQL.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerMSSQL.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerMSSQL.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerMSSQL.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerMSSQL.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerMSSQL.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerMSSQL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerMSSQL):
            return True

        return self.to_dict() != other.to_dict()
