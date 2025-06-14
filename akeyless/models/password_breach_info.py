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


class PasswordBreachInfo(object):
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
        'breach_check_date': 'datetime',
        'breach_count': 'int',
        'breach_suggestions': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'breach_check_date': 'breach_check_date',
        'breach_count': 'breach_count',
        'breach_suggestions': 'breach_suggestions',
        'status': 'status'
    }

    def __init__(self, breach_check_date=None, breach_count=None, breach_suggestions=None, status=None, local_vars_configuration=None):  # noqa: E501
        """PasswordBreachInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._breach_check_date = None
        self._breach_count = None
        self._breach_suggestions = None
        self._status = None
        self.discriminator = None

        if breach_check_date is not None:
            self.breach_check_date = breach_check_date
        if breach_count is not None:
            self.breach_count = breach_count
        if breach_suggestions is not None:
            self.breach_suggestions = breach_suggestions
        if status is not None:
            self.status = status

    @property
    def breach_check_date(self):
        """Gets the breach_check_date of this PasswordBreachInfo.  # noqa: E501


        :return: The breach_check_date of this PasswordBreachInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._breach_check_date

    @breach_check_date.setter
    def breach_check_date(self, breach_check_date):
        """Sets the breach_check_date of this PasswordBreachInfo.


        :param breach_check_date: The breach_check_date of this PasswordBreachInfo.  # noqa: E501
        :type: datetime
        """

        self._breach_check_date = breach_check_date

    @property
    def breach_count(self):
        """Gets the breach_count of this PasswordBreachInfo.  # noqa: E501


        :return: The breach_count of this PasswordBreachInfo.  # noqa: E501
        :rtype: int
        """
        return self._breach_count

    @breach_count.setter
    def breach_count(self, breach_count):
        """Sets the breach_count of this PasswordBreachInfo.


        :param breach_count: The breach_count of this PasswordBreachInfo.  # noqa: E501
        :type: int
        """

        self._breach_count = breach_count

    @property
    def breach_suggestions(self):
        """Gets the breach_suggestions of this PasswordBreachInfo.  # noqa: E501


        :return: The breach_suggestions of this PasswordBreachInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._breach_suggestions

    @breach_suggestions.setter
    def breach_suggestions(self, breach_suggestions):
        """Sets the breach_suggestions of this PasswordBreachInfo.


        :param breach_suggestions: The breach_suggestions of this PasswordBreachInfo.  # noqa: E501
        :type: list[str]
        """

        self._breach_suggestions = breach_suggestions

    @property
    def status(self):
        """Gets the status of this PasswordBreachInfo.  # noqa: E501


        :return: The status of this PasswordBreachInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PasswordBreachInfo.


        :param status: The status of this PasswordBreachInfo.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, PasswordBreachInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordBreachInfo):
            return True

        return self.to_dict() != other.to_dict()
