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


class GitlabTargetDetails(object):
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
        'gitlab_access_token': 'str',
        'gitlab_certificate': 'str',
        'gitlab_url': 'str'
    }

    attribute_map = {
        'gitlab_access_token': 'gitlab_access_token',
        'gitlab_certificate': 'gitlab_certificate',
        'gitlab_url': 'gitlab_url'
    }

    def __init__(self, gitlab_access_token=None, gitlab_certificate=None, gitlab_url=None, local_vars_configuration=None):  # noqa: E501
        """GitlabTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gitlab_access_token = None
        self._gitlab_certificate = None
        self._gitlab_url = None
        self.discriminator = None

        if gitlab_access_token is not None:
            self.gitlab_access_token = gitlab_access_token
        if gitlab_certificate is not None:
            self.gitlab_certificate = gitlab_certificate
        if gitlab_url is not None:
            self.gitlab_url = gitlab_url

    @property
    def gitlab_access_token(self):
        """Gets the gitlab_access_token of this GitlabTargetDetails.  # noqa: E501


        :return: The gitlab_access_token of this GitlabTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gitlab_access_token

    @gitlab_access_token.setter
    def gitlab_access_token(self, gitlab_access_token):
        """Sets the gitlab_access_token of this GitlabTargetDetails.


        :param gitlab_access_token: The gitlab_access_token of this GitlabTargetDetails.  # noqa: E501
        :type: str
        """

        self._gitlab_access_token = gitlab_access_token

    @property
    def gitlab_certificate(self):
        """Gets the gitlab_certificate of this GitlabTargetDetails.  # noqa: E501


        :return: The gitlab_certificate of this GitlabTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gitlab_certificate

    @gitlab_certificate.setter
    def gitlab_certificate(self, gitlab_certificate):
        """Sets the gitlab_certificate of this GitlabTargetDetails.


        :param gitlab_certificate: The gitlab_certificate of this GitlabTargetDetails.  # noqa: E501
        :type: str
        """

        self._gitlab_certificate = gitlab_certificate

    @property
    def gitlab_url(self):
        """Gets the gitlab_url of this GitlabTargetDetails.  # noqa: E501


        :return: The gitlab_url of this GitlabTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gitlab_url

    @gitlab_url.setter
    def gitlab_url(self, gitlab_url):
        """Sets the gitlab_url of this GitlabTargetDetails.


        :param gitlab_url: The gitlab_url of this GitlabTargetDetails.  # noqa: E501
        :type: str
        """

        self._gitlab_url = gitlab_url

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
        if not isinstance(other, GitlabTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GitlabTargetDetails):
            return True

        return self.to_dict() != other.to_dict()