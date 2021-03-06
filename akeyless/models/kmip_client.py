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


class KMIPClient(object):
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
        'environment': 'str',
        'id': 'str',
        'name': 'str',
        'rules': 'list[PathRule]'
    }

    attribute_map = {
        'environment': 'environment',
        'id': 'id',
        'name': 'name',
        'rules': 'rules'
    }

    def __init__(self, environment=None, id=None, name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """KMIPClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._environment = None
        self._id = None
        self._name = None
        self._rules = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules

    @property
    def environment(self):
        """Gets the environment of this KMIPClient.  # noqa: E501


        :return: The environment of this KMIPClient.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this KMIPClient.


        :param environment: The environment of this KMIPClient.  # noqa: E501
        :type: str
        """

        self._environment = environment

    @property
    def id(self):
        """Gets the id of this KMIPClient.  # noqa: E501


        :return: The id of this KMIPClient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KMIPClient.


        :param id: The id of this KMIPClient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this KMIPClient.  # noqa: E501


        :return: The name of this KMIPClient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KMIPClient.


        :param name: The name of this KMIPClient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this KMIPClient.  # noqa: E501


        :return: The rules of this KMIPClient.  # noqa: E501
        :rtype: list[PathRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this KMIPClient.


        :param rules: The rules of this KMIPClient.  # noqa: E501
        :type: list[PathRule]
        """

        self._rules = rules

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
        if not isinstance(other, KMIPClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KMIPClient):
            return True

        return self.to_dict() != other.to_dict()
