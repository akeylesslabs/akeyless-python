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


class PathRule(object):
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
        'capabilities': 'list[str]',
        'path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'capabilities': 'capabilities',
        'path': 'path',
        'type': 'type'
    }

    def __init__(self, capabilities=None, path=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PathRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capabilities = None
        self._path = None
        self._type = None
        self.discriminator = None

        if capabilities is not None:
            self.capabilities = capabilities
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type

    @property
    def capabilities(self):
        """Gets the capabilities of this PathRule.  # noqa: E501

        The approved/denied capabilities in the path  # noqa: E501

        :return: The capabilities of this PathRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this PathRule.

        The approved/denied capabilities in the path  # noqa: E501

        :param capabilities: The capabilities of this PathRule.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def path(self):
        """Gets the path of this PathRule.  # noqa: E501

        The path the rule refers to  # noqa: E501

        :return: The path of this PathRule.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PathRule.

        The path the rule refers to  # noqa: E501

        :param path: The path of this PathRule.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this PathRule.  # noqa: E501


        :return: The type of this PathRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PathRule.


        :param type: The type of this PathRule.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, PathRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PathRule):
            return True

        return self.to_dict() != other.to_dict()
