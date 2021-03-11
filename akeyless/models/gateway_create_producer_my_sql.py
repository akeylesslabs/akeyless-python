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


class GatewayCreateProducerMySQL(object):
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
        'db_server_certificates': 'str',
        'db_server_name': 'str',
        'gateway_url': 'str',
        'mysql_dbname': 'str',
        'mysql_host': 'str',
        'mysql_password': 'str',
        'mysql_port': 'str',
        'mysql_screation_statements': 'str',
        'mysql_username': 'str',
        'name': 'str',
        'producer_encryption_key_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'db_server_certificates': 'db-server-certificates',
        'db_server_name': 'db-server-name',
        'gateway_url': 'gateway-url',
        'mysql_dbname': 'mysql-dbname',
        'mysql_host': 'mysql-host',
        'mysql_password': 'mysql-password',
        'mysql_port': 'mysql-port',
        'mysql_screation_statements': 'mysql-screation-statements',
        'mysql_username': 'mysql-username',
        'name': 'name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, db_server_certificates=None, db_server_name=None, gateway_url='http://localhost:8000', mysql_dbname=None, mysql_host='127.0.0.1', mysql_password=None, mysql_port='3306', mysql_screation_statements=None, mysql_username=None, name=None, producer_encryption_key_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerMySQL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._db_server_certificates = None
        self._db_server_name = None
        self._gateway_url = None
        self._mysql_dbname = None
        self._mysql_host = None
        self._mysql_password = None
        self._mysql_port = None
        self._mysql_screation_statements = None
        self._mysql_username = None
        self._name = None
        self._producer_encryption_key_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if db_server_certificates is not None:
            self.db_server_certificates = db_server_certificates
        if db_server_name is not None:
            self.db_server_name = db_server_name
        if gateway_url is not None:
            self.gateway_url = gateway_url
        self.mysql_dbname = mysql_dbname
        if mysql_host is not None:
            self.mysql_host = mysql_host
        self.mysql_password = mysql_password
        if mysql_port is not None:
            self.mysql_port = mysql_port
        if mysql_screation_statements is not None:
            self.mysql_screation_statements = mysql_screation_statements
        self.mysql_username = mysql_username
        self.name = name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def db_server_certificates(self):
        """Gets the db_server_certificates of this GatewayCreateProducerMySQL.  # noqa: E501

        (Optional) DB server certificates  # noqa: E501

        :return: The db_server_certificates of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._db_server_certificates

    @db_server_certificates.setter
    def db_server_certificates(self, db_server_certificates):
        """Sets the db_server_certificates of this GatewayCreateProducerMySQL.

        (Optional) DB server certificates  # noqa: E501

        :param db_server_certificates: The db_server_certificates of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._db_server_certificates = db_server_certificates

    @property
    def db_server_name(self):
        """Gets the db_server_name of this GatewayCreateProducerMySQL.  # noqa: E501

        (Optional) Server name for certificate verification  # noqa: E501

        :return: The db_server_name of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._db_server_name

    @db_server_name.setter
    def db_server_name(self, db_server_name):
        """Sets the db_server_name of this GatewayCreateProducerMySQL.

        (Optional) Server name for certificate verification  # noqa: E501

        :param db_server_name: The db_server_name of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._db_server_name = db_server_name

    @property
    def gateway_url(self):
        """Gets the gateway_url of this GatewayCreateProducerMySQL.  # noqa: E501

        Gateway url  # noqa: E501

        :return: The gateway_url of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, gateway_url):
        """Sets the gateway_url of this GatewayCreateProducerMySQL.

        Gateway url  # noqa: E501

        :param gateway_url: The gateway_url of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._gateway_url = gateway_url

    @property
    def mysql_dbname(self):
        """Gets the mysql_dbname of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL DB Name  # noqa: E501

        :return: The mysql_dbname of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_dbname

    @mysql_dbname.setter
    def mysql_dbname(self, mysql_dbname):
        """Sets the mysql_dbname of this GatewayCreateProducerMySQL.

        MySQL DB Name  # noqa: E501

        :param mysql_dbname: The mysql_dbname of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mysql_dbname is None:  # noqa: E501
            raise ValueError("Invalid value for `mysql_dbname`, must not be `None`")  # noqa: E501

        self._mysql_dbname = mysql_dbname

    @property
    def mysql_host(self):
        """Gets the mysql_host of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL Host  # noqa: E501

        :return: The mysql_host of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_host

    @mysql_host.setter
    def mysql_host(self, mysql_host):
        """Sets the mysql_host of this GatewayCreateProducerMySQL.

        MySQL Host  # noqa: E501

        :param mysql_host: The mysql_host of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._mysql_host = mysql_host

    @property
    def mysql_password(self):
        """Gets the mysql_password of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL Password  # noqa: E501

        :return: The mysql_password of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_password

    @mysql_password.setter
    def mysql_password(self, mysql_password):
        """Sets the mysql_password of this GatewayCreateProducerMySQL.

        MySQL Password  # noqa: E501

        :param mysql_password: The mysql_password of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mysql_password is None:  # noqa: E501
            raise ValueError("Invalid value for `mysql_password`, must not be `None`")  # noqa: E501

        self._mysql_password = mysql_password

    @property
    def mysql_port(self):
        """Gets the mysql_port of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL Port  # noqa: E501

        :return: The mysql_port of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_port

    @mysql_port.setter
    def mysql_port(self, mysql_port):
        """Sets the mysql_port of this GatewayCreateProducerMySQL.

        MySQL Port  # noqa: E501

        :param mysql_port: The mysql_port of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._mysql_port = mysql_port

    @property
    def mysql_screation_statements(self):
        """Gets the mysql_screation_statements of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL Creation statements  # noqa: E501

        :return: The mysql_screation_statements of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_screation_statements

    @mysql_screation_statements.setter
    def mysql_screation_statements(self, mysql_screation_statements):
        """Sets the mysql_screation_statements of this GatewayCreateProducerMySQL.

        MySQL Creation statements  # noqa: E501

        :param mysql_screation_statements: The mysql_screation_statements of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._mysql_screation_statements = mysql_screation_statements

    @property
    def mysql_username(self):
        """Gets the mysql_username of this GatewayCreateProducerMySQL.  # noqa: E501

        MySQL Username  # noqa: E501

        :return: The mysql_username of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._mysql_username

    @mysql_username.setter
    def mysql_username(self, mysql_username):
        """Sets the mysql_username of this GatewayCreateProducerMySQL.

        MySQL Username  # noqa: E501

        :param mysql_username: The mysql_username of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mysql_username is None:  # noqa: E501
            raise ValueError("Invalid value for `mysql_username`, must not be `None`")  # noqa: E501

        self._mysql_username = mysql_username

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerMySQL.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerMySQL.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerMySQL.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerMySQL.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerMySQL.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerMySQL.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerMySQL.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerMySQL.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerMySQL.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerMySQL.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerMySQL.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerMySQL.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

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
        if not isinstance(other, GatewayCreateProducerMySQL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerMySQL):
            return True

        return self.to_dict() != other.to_dict()