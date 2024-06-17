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


class HashiVaultTargetDetails(object):
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
        'vault_namespaces': 'str',
        'vault_token': 'str',
        'vault_url': 'str'
    }

    attribute_map = {
        'vault_namespaces': 'vault_namespaces',
        'vault_token': 'vault_token',
        'vault_url': 'vault_url'
    }

    def __init__(self, vault_namespaces=None, vault_token=None, vault_url=None, local_vars_configuration=None):  # noqa: E501
        """HashiVaultTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vault_namespaces = None
        self._vault_token = None
        self._vault_url = None
        self.discriminator = None

        if vault_namespaces is not None:
            self.vault_namespaces = vault_namespaces
        if vault_token is not None:
            self.vault_token = vault_token
        if vault_url is not None:
            self.vault_url = vault_url

    @property
    def vault_namespaces(self):
        """Gets the vault_namespaces of this HashiVaultTargetDetails.  # noqa: E501


        :return: The vault_namespaces of this HashiVaultTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._vault_namespaces

    @vault_namespaces.setter
    def vault_namespaces(self, vault_namespaces):
        """Sets the vault_namespaces of this HashiVaultTargetDetails.


        :param vault_namespaces: The vault_namespaces of this HashiVaultTargetDetails.  # noqa: E501
        :type: str
        """

        self._vault_namespaces = vault_namespaces

    @property
    def vault_token(self):
        """Gets the vault_token of this HashiVaultTargetDetails.  # noqa: E501


        :return: The vault_token of this HashiVaultTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._vault_token

    @vault_token.setter
    def vault_token(self, vault_token):
        """Sets the vault_token of this HashiVaultTargetDetails.


        :param vault_token: The vault_token of this HashiVaultTargetDetails.  # noqa: E501
        :type: str
        """

        self._vault_token = vault_token

    @property
    def vault_url(self):
        """Gets the vault_url of this HashiVaultTargetDetails.  # noqa: E501


        :return: The vault_url of this HashiVaultTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._vault_url

    @vault_url.setter
    def vault_url(self, vault_url):
        """Sets the vault_url of this HashiVaultTargetDetails.


        :param vault_url: The vault_url of this HashiVaultTargetDetails.  # noqa: E501
        :type: str
        """

        self._vault_url = vault_url

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
        if not isinstance(other, HashiVaultTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HashiVaultTargetDetails):
            return True

        return self.to_dict() != other.to_dict()