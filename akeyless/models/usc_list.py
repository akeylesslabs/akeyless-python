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


class UscList(object):
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
        'json': 'bool',
        'object_type': 'str',
        'token': 'str',
        'uid_token': 'str',
        'usc_name': 'str'
    }

    attribute_map = {
        'json': 'json',
        'object_type': 'object-type',
        'token': 'token',
        'uid_token': 'uid-token',
        'usc_name': 'usc-name'
    }

    def __init__(self, json=False, object_type=None, token=None, uid_token=None, usc_name=None, local_vars_configuration=None):  # noqa: E501
        """UscList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._json = None
        self._object_type = None
        self._token = None
        self._uid_token = None
        self._usc_name = None
        self.discriminator = None

        if json is not None:
            self.json = json
        if object_type is not None:
            self.object_type = object_type
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        self.usc_name = usc_name

    @property
    def json(self):
        """Gets the json of this UscList.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UscList.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UscList.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UscList.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def object_type(self):
        """Gets the object_type of this UscList.  # noqa: E501


        :return: The object_type of this UscList.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this UscList.


        :param object_type: The object_type of this UscList.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def token(self):
        """Gets the token of this UscList.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UscList.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UscList.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UscList.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UscList.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UscList.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UscList.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UscList.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def usc_name(self):
        """Gets the usc_name of this UscList.  # noqa: E501

        Name of the Universal Secrets Connector item  # noqa: E501

        :return: The usc_name of this UscList.  # noqa: E501
        :rtype: str
        """
        return self._usc_name

    @usc_name.setter
    def usc_name(self, usc_name):
        """Sets the usc_name of this UscList.

        Name of the Universal Secrets Connector item  # noqa: E501

        :param usc_name: The usc_name of this UscList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and usc_name is None:  # noqa: E501
            raise ValueError("Invalid value for `usc_name`, must not be `None`")  # noqa: E501

        self._usc_name = usc_name

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
        if not isinstance(other, UscList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UscList):
            return True

        return self.to_dict() != other.to_dict()
