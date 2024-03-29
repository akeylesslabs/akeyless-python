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


class CustomerFragmentConfig(object):
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
        'description': 'str',
        'fragment_type': 'str',
        'id': 'str',
        'key_label': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'fragment_type': 'fragment_type',
        'id': 'id',
        'key_label': 'key_label',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, description=None, fragment_type=None, id=None, key_label=None, name=None, value=None, local_vars_configuration=None):  # noqa: E501
        """CustomerFragmentConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._fragment_type = None
        self._id = None
        self._key_label = None
        self._name = None
        self._value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if fragment_type is not None:
            self.fragment_type = fragment_type
        if id is not None:
            self.id = id
        if key_label is not None:
            self.key_label = key_label
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def description(self):
        """Gets the description of this CustomerFragmentConfig.  # noqa: E501


        :return: The description of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerFragmentConfig.


        :param description: The description of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fragment_type(self):
        """Gets the fragment_type of this CustomerFragmentConfig.  # noqa: E501


        :return: The fragment_type of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._fragment_type

    @fragment_type.setter
    def fragment_type(self, fragment_type):
        """Sets the fragment_type of this CustomerFragmentConfig.


        :param fragment_type: The fragment_type of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._fragment_type = fragment_type

    @property
    def id(self):
        """Gets the id of this CustomerFragmentConfig.  # noqa: E501


        :return: The id of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerFragmentConfig.


        :param id: The id of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key_label(self):
        """Gets the key_label of this CustomerFragmentConfig.  # noqa: E501


        :return: The key_label of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._key_label

    @key_label.setter
    def key_label(self, key_label):
        """Sets the key_label of this CustomerFragmentConfig.


        :param key_label: The key_label of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._key_label = key_label

    @property
    def name(self):
        """Gets the name of this CustomerFragmentConfig.  # noqa: E501


        :return: The name of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerFragmentConfig.


        :param name: The name of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this CustomerFragmentConfig.  # noqa: E501


        :return: The value of this CustomerFragmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomerFragmentConfig.


        :param value: The value of this CustomerFragmentConfig.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, CustomerFragmentConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerFragmentConfig):
            return True

        return self.to_dict() != other.to_dict()
