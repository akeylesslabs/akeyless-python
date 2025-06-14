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


class TmpUserData(object):
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
        'access_id': 'str',
        'creation_date': 'datetime',
        'custom_ttl': 'int',
        'dynamic_secret_type': 'str',
        'encrypted_secret': 'str',
        'host': 'str',
        'id': 'str',
        'sub_claims': 'dict(str, list[str])'
    }

    attribute_map = {
        'access_id': 'access_id',
        'creation_date': 'creation_date',
        'custom_ttl': 'custom_ttl',
        'dynamic_secret_type': 'dynamic_secret_type',
        'encrypted_secret': 'encrypted_secret',
        'host': 'host',
        'id': 'id',
        'sub_claims': 'sub_claims'
    }

    def __init__(self, access_id=None, creation_date=None, custom_ttl=None, dynamic_secret_type=None, encrypted_secret=None, host=None, id=None, sub_claims=None, local_vars_configuration=None):  # noqa: E501
        """TmpUserData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._creation_date = None
        self._custom_ttl = None
        self._dynamic_secret_type = None
        self._encrypted_secret = None
        self._host = None
        self._id = None
        self._sub_claims = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if creation_date is not None:
            self.creation_date = creation_date
        if custom_ttl is not None:
            self.custom_ttl = custom_ttl
        if dynamic_secret_type is not None:
            self.dynamic_secret_type = dynamic_secret_type
        if encrypted_secret is not None:
            self.encrypted_secret = encrypted_secret
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if sub_claims is not None:
            self.sub_claims = sub_claims

    @property
    def access_id(self):
        """Gets the access_id of this TmpUserData.  # noqa: E501


        :return: The access_id of this TmpUserData.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this TmpUserData.


        :param access_id: The access_id of this TmpUserData.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def creation_date(self):
        """Gets the creation_date of this TmpUserData.  # noqa: E501


        :return: The creation_date of this TmpUserData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TmpUserData.


        :param creation_date: The creation_date of this TmpUserData.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def custom_ttl(self):
        """Gets the custom_ttl of this TmpUserData.  # noqa: E501


        :return: The custom_ttl of this TmpUserData.  # noqa: E501
        :rtype: int
        """
        return self._custom_ttl

    @custom_ttl.setter
    def custom_ttl(self, custom_ttl):
        """Sets the custom_ttl of this TmpUserData.


        :param custom_ttl: The custom_ttl of this TmpUserData.  # noqa: E501
        :type: int
        """

        self._custom_ttl = custom_ttl

    @property
    def dynamic_secret_type(self):
        """Gets the dynamic_secret_type of this TmpUserData.  # noqa: E501


        :return: The dynamic_secret_type of this TmpUserData.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_secret_type

    @dynamic_secret_type.setter
    def dynamic_secret_type(self, dynamic_secret_type):
        """Sets the dynamic_secret_type of this TmpUserData.


        :param dynamic_secret_type: The dynamic_secret_type of this TmpUserData.  # noqa: E501
        :type: str
        """

        self._dynamic_secret_type = dynamic_secret_type

    @property
    def encrypted_secret(self):
        """Gets the encrypted_secret of this TmpUserData.  # noqa: E501


        :return: The encrypted_secret of this TmpUserData.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_secret

    @encrypted_secret.setter
    def encrypted_secret(self, encrypted_secret):
        """Sets the encrypted_secret of this TmpUserData.


        :param encrypted_secret: The encrypted_secret of this TmpUserData.  # noqa: E501
        :type: str
        """

        self._encrypted_secret = encrypted_secret

    @property
    def host(self):
        """Gets the host of this TmpUserData.  # noqa: E501


        :return: The host of this TmpUserData.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this TmpUserData.


        :param host: The host of this TmpUserData.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this TmpUserData.  # noqa: E501


        :return: The id of this TmpUserData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TmpUserData.


        :param id: The id of this TmpUserData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sub_claims(self):
        """Gets the sub_claims of this TmpUserData.  # noqa: E501


        :return: The sub_claims of this TmpUserData.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._sub_claims

    @sub_claims.setter
    def sub_claims(self, sub_claims):
        """Sets the sub_claims of this TmpUserData.


        :param sub_claims: The sub_claims of this TmpUserData.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._sub_claims = sub_claims

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
        if not isinstance(other, TmpUserData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TmpUserData):
            return True

        return self.to_dict() != other.to_dict()
