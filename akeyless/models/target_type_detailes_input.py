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


class TargetTypeDetailesInput(object):
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
        'admin_name': 'str',
        'admin_pwd': 'str',
        'aws_access_key_id': 'str',
        'aws_region': 'str',
        'aws_secret_access_key': 'str',
        'aws_session_token': 'str',
        'db_host_name': 'str',
        'db_port': 'str',
        'db_pwd': 'str',
        'db_user_name': 'str',
        'host_name': 'str',
        'host_port': 'str',
        'ip': 'list[str]',
        'mongodb_db_name': 'str',
        'mongodb_uri_connection': 'str',
        'port': 'str',
        'rabbitmq_server_password': 'str',
        'rabbitmq_server_uri': 'str',
        'rabbitmq_server_user': 'str',
        'url': 'str'
    }

    attribute_map = {
        'admin_name': 'admin_name',
        'admin_pwd': 'admin_pwd',
        'aws_access_key_id': 'aws_access_key_id',
        'aws_region': 'aws_region',
        'aws_secret_access_key': 'aws_secret_access_key',
        'aws_session_token': 'aws_session_token',
        'db_host_name': 'db_host_name',
        'db_port': 'db_port',
        'db_pwd': 'db_pwd',
        'db_user_name': 'db_user_name',
        'host_name': 'host_name',
        'host_port': 'host_port',
        'ip': 'ip',
        'mongodb_db_name': 'mongodb_db_name',
        'mongodb_uri_connection': 'mongodb_uri_connection',
        'port': 'port',
        'rabbitmq_server_password': 'rabbitmq_server_password',
        'rabbitmq_server_uri': 'rabbitmq_server_uri',
        'rabbitmq_server_user': 'rabbitmq_server_user',
        'url': 'url'
    }

    def __init__(self, admin_name=None, admin_pwd=None, aws_access_key_id=None, aws_region=None, aws_secret_access_key=None, aws_session_token=None, db_host_name=None, db_port=None, db_pwd=None, db_user_name=None, host_name=None, host_port=None, ip=None, mongodb_db_name=None, mongodb_uri_connection=None, port=None, rabbitmq_server_password=None, rabbitmq_server_uri=None, rabbitmq_server_user=None, url=None, local_vars_configuration=None):  # noqa: E501
        """TargetTypeDetailesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_name = None
        self._admin_pwd = None
        self._aws_access_key_id = None
        self._aws_region = None
        self._aws_secret_access_key = None
        self._aws_session_token = None
        self._db_host_name = None
        self._db_port = None
        self._db_pwd = None
        self._db_user_name = None
        self._host_name = None
        self._host_port = None
        self._ip = None
        self._mongodb_db_name = None
        self._mongodb_uri_connection = None
        self._port = None
        self._rabbitmq_server_password = None
        self._rabbitmq_server_uri = None
        self._rabbitmq_server_user = None
        self._url = None
        self.discriminator = None

        if admin_name is not None:
            self.admin_name = admin_name
        if admin_pwd is not None:
            self.admin_pwd = admin_pwd
        if aws_access_key_id is not None:
            self.aws_access_key_id = aws_access_key_id
        if aws_region is not None:
            self.aws_region = aws_region
        if aws_secret_access_key is not None:
            self.aws_secret_access_key = aws_secret_access_key
        if aws_session_token is not None:
            self.aws_session_token = aws_session_token
        if db_host_name is not None:
            self.db_host_name = db_host_name
        if db_port is not None:
            self.db_port = db_port
        if db_pwd is not None:
            self.db_pwd = db_pwd
        if db_user_name is not None:
            self.db_user_name = db_user_name
        if host_name is not None:
            self.host_name = host_name
        if host_port is not None:
            self.host_port = host_port
        if ip is not None:
            self.ip = ip
        if mongodb_db_name is not None:
            self.mongodb_db_name = mongodb_db_name
        if mongodb_uri_connection is not None:
            self.mongodb_uri_connection = mongodb_uri_connection
        if port is not None:
            self.port = port
        if rabbitmq_server_password is not None:
            self.rabbitmq_server_password = rabbitmq_server_password
        if rabbitmq_server_uri is not None:
            self.rabbitmq_server_uri = rabbitmq_server_uri
        if rabbitmq_server_user is not None:
            self.rabbitmq_server_user = rabbitmq_server_user
        if url is not None:
            self.url = url

    @property
    def admin_name(self):
        """Gets the admin_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The admin_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """Sets the admin_name of this TargetTypeDetailesInput.


        :param admin_name: The admin_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._admin_name = admin_name

    @property
    def admin_pwd(self):
        """Gets the admin_pwd of this TargetTypeDetailesInput.  # noqa: E501


        :return: The admin_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._admin_pwd

    @admin_pwd.setter
    def admin_pwd(self, admin_pwd):
        """Sets the admin_pwd of this TargetTypeDetailesInput.


        :param admin_pwd: The admin_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._admin_pwd = admin_pwd

    @property
    def aws_access_key_id(self):
        """Gets the aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_key_id

    @aws_access_key_id.setter
    def aws_access_key_id(self, aws_access_key_id):
        """Sets the aws_access_key_id of this TargetTypeDetailesInput.


        :param aws_access_key_id: The aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_access_key_id = aws_access_key_id

    @property
    def aws_region(self):
        """Gets the aws_region of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_region of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this TargetTypeDetailesInput.


        :param aws_region: The aws_region of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def aws_secret_access_key(self):
        """Gets the aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_secret_access_key

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, aws_secret_access_key):
        """Sets the aws_secret_access_key of this TargetTypeDetailesInput.


        :param aws_secret_access_key: The aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_secret_access_key = aws_secret_access_key

    @property
    def aws_session_token(self):
        """Gets the aws_session_token of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_session_token of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_session_token

    @aws_session_token.setter
    def aws_session_token(self, aws_session_token):
        """Sets the aws_session_token of this TargetTypeDetailesInput.


        :param aws_session_token: The aws_session_token of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_session_token = aws_session_token

    @property
    def db_host_name(self):
        """Gets the db_host_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_host_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_host_name

    @db_host_name.setter
    def db_host_name(self, db_host_name):
        """Sets the db_host_name of this TargetTypeDetailesInput.


        :param db_host_name: The db_host_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_host_name = db_host_name

    @property
    def db_port(self):
        """Gets the db_port of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_port of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this TargetTypeDetailesInput.


        :param db_port: The db_port of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_port = db_port

    @property
    def db_pwd(self):
        """Gets the db_pwd of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_pwd

    @db_pwd.setter
    def db_pwd(self, db_pwd):
        """Sets the db_pwd of this TargetTypeDetailesInput.


        :param db_pwd: The db_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_pwd = db_pwd

    @property
    def db_user_name(self):
        """Gets the db_user_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_user_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this TargetTypeDetailesInput.


        :param db_user_name: The db_user_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_user_name = db_user_name

    @property
    def host_name(self):
        """Gets the host_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The host_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this TargetTypeDetailesInput.


        :param host_name: The host_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def host_port(self):
        """Gets the host_port of this TargetTypeDetailesInput.  # noqa: E501


        :return: The host_port of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """Sets the host_port of this TargetTypeDetailesInput.


        :param host_port: The host_port of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._host_port = host_port

    @property
    def ip(self):
        """Gets the ip of this TargetTypeDetailesInput.  # noqa: E501


        :return: The ip of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TargetTypeDetailesInput.


        :param ip: The ip of this TargetTypeDetailesInput.  # noqa: E501
        :type: list[str]
        """

        self._ip = ip

    @property
    def mongodb_db_name(self):
        """Gets the mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_db_name

    @mongodb_db_name.setter
    def mongodb_db_name(self, mongodb_db_name):
        """Sets the mongodb_db_name of this TargetTypeDetailesInput.


        :param mongodb_db_name: The mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._mongodb_db_name = mongodb_db_name

    @property
    def mongodb_uri_connection(self):
        """Gets the mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501


        :return: The mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_connection

    @mongodb_uri_connection.setter
    def mongodb_uri_connection(self, mongodb_uri_connection):
        """Sets the mongodb_uri_connection of this TargetTypeDetailesInput.


        :param mongodb_uri_connection: The mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_connection = mongodb_uri_connection

    @property
    def port(self):
        """Gets the port of this TargetTypeDetailesInput.  # noqa: E501


        :return: The port of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TargetTypeDetailesInput.


        :param port: The port of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def rabbitmq_server_password(self):
        """Gets the rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_password

    @rabbitmq_server_password.setter
    def rabbitmq_server_password(self, rabbitmq_server_password):
        """Sets the rabbitmq_server_password of this TargetTypeDetailesInput.


        :param rabbitmq_server_password: The rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_password = rabbitmq_server_password

    @property
    def rabbitmq_server_uri(self):
        """Gets the rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_uri

    @rabbitmq_server_uri.setter
    def rabbitmq_server_uri(self, rabbitmq_server_uri):
        """Sets the rabbitmq_server_uri of this TargetTypeDetailesInput.


        :param rabbitmq_server_uri: The rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_uri = rabbitmq_server_uri

    @property
    def rabbitmq_server_user(self):
        """Gets the rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_user

    @rabbitmq_server_user.setter
    def rabbitmq_server_user(self, rabbitmq_server_user):
        """Sets the rabbitmq_server_user of this TargetTypeDetailesInput.


        :param rabbitmq_server_user: The rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_user = rabbitmq_server_user

    @property
    def url(self):
        """Gets the url of this TargetTypeDetailesInput.  # noqa: E501


        :return: The url of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TargetTypeDetailesInput.


        :param url: The url of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, TargetTypeDetailesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetTypeDetailesInput):
            return True

        return self.to_dict() != other.to_dict()