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


class PasswordExpirationInfo(object):
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
        'days_before_expire': 'int',
        'days_before_notification': 'int',
        'days_until_expire': 'int',
        'enable': 'bool'
    }

    attribute_map = {
        'days_before_expire': 'days_before_expire',
        'days_before_notification': 'days_before_notification',
        'days_until_expire': 'days_until_expire',
        'enable': 'enable'
    }

    def __init__(self, days_before_expire=None, days_before_notification=None, days_until_expire=None, enable=None, local_vars_configuration=None):  # noqa: E501
        """PasswordExpirationInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._days_before_expire = None
        self._days_before_notification = None
        self._days_until_expire = None
        self._enable = None
        self.discriminator = None

        if days_before_expire is not None:
            self.days_before_expire = days_before_expire
        if days_before_notification is not None:
            self.days_before_notification = days_before_notification
        if days_until_expire is not None:
            self.days_until_expire = days_until_expire
        if enable is not None:
            self.enable = enable

    @property
    def days_before_expire(self):
        """Gets the days_before_expire of this PasswordExpirationInfo.  # noqa: E501


        :return: The days_before_expire of this PasswordExpirationInfo.  # noqa: E501
        :rtype: int
        """
        return self._days_before_expire

    @days_before_expire.setter
    def days_before_expire(self, days_before_expire):
        """Sets the days_before_expire of this PasswordExpirationInfo.


        :param days_before_expire: The days_before_expire of this PasswordExpirationInfo.  # noqa: E501
        :type: int
        """

        self._days_before_expire = days_before_expire

    @property
    def days_before_notification(self):
        """Gets the days_before_notification of this PasswordExpirationInfo.  # noqa: E501


        :return: The days_before_notification of this PasswordExpirationInfo.  # noqa: E501
        :rtype: int
        """
        return self._days_before_notification

    @days_before_notification.setter
    def days_before_notification(self, days_before_notification):
        """Sets the days_before_notification of this PasswordExpirationInfo.


        :param days_before_notification: The days_before_notification of this PasswordExpirationInfo.  # noqa: E501
        :type: int
        """

        self._days_before_notification = days_before_notification

    @property
    def days_until_expire(self):
        """Gets the days_until_expire of this PasswordExpirationInfo.  # noqa: E501

        r/o calculated parameter  # noqa: E501

        :return: The days_until_expire of this PasswordExpirationInfo.  # noqa: E501
        :rtype: int
        """
        return self._days_until_expire

    @days_until_expire.setter
    def days_until_expire(self, days_until_expire):
        """Sets the days_until_expire of this PasswordExpirationInfo.

        r/o calculated parameter  # noqa: E501

        :param days_until_expire: The days_until_expire of this PasswordExpirationInfo.  # noqa: E501
        :type: int
        """

        self._days_until_expire = days_until_expire

    @property
    def enable(self):
        """Gets the enable of this PasswordExpirationInfo.  # noqa: E501


        :return: The enable of this PasswordExpirationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PasswordExpirationInfo.


        :param enable: The enable of this PasswordExpirationInfo.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if not isinstance(other, PasswordExpirationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordExpirationInfo):
            return True

        return self.to_dict() != other.to_dict()