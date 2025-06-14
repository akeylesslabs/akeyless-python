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


class GatewayGetDefaultsOutput(object):
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
        'certificate_access_id': 'str',
        'default_protection_key_id': 'str',
        'hvp_route_version': 'int',
        'notify_on_status_change': 'bool',
        'oidc_access_id': 'str',
        'saml_access_id': 'str'
    }

    attribute_map = {
        'certificate_access_id': 'certificate_access_id',
        'default_protection_key_id': 'default_protection_key_id',
        'hvp_route_version': 'hvp_route_version',
        'notify_on_status_change': 'notify_on_status_change',
        'oidc_access_id': 'oidc_access_id',
        'saml_access_id': 'saml_access_id'
    }

    def __init__(self, certificate_access_id=None, default_protection_key_id=None, hvp_route_version=None, notify_on_status_change=None, oidc_access_id=None, saml_access_id=None, local_vars_configuration=None):  # noqa: E501
        """GatewayGetDefaultsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate_access_id = None
        self._default_protection_key_id = None
        self._hvp_route_version = None
        self._notify_on_status_change = None
        self._oidc_access_id = None
        self._saml_access_id = None
        self.discriminator = None

        if certificate_access_id is not None:
            self.certificate_access_id = certificate_access_id
        if default_protection_key_id is not None:
            self.default_protection_key_id = default_protection_key_id
        if hvp_route_version is not None:
            self.hvp_route_version = hvp_route_version
        if notify_on_status_change is not None:
            self.notify_on_status_change = notify_on_status_change
        if oidc_access_id is not None:
            self.oidc_access_id = oidc_access_id
        if saml_access_id is not None:
            self.saml_access_id = saml_access_id

    @property
    def certificate_access_id(self):
        """Gets the certificate_access_id of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The certificate_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_access_id

    @certificate_access_id.setter
    def certificate_access_id(self, certificate_access_id):
        """Sets the certificate_access_id of this GatewayGetDefaultsOutput.


        :param certificate_access_id: The certificate_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: str
        """

        self._certificate_access_id = certificate_access_id

    @property
    def default_protection_key_id(self):
        """Gets the default_protection_key_id of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The default_protection_key_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._default_protection_key_id

    @default_protection_key_id.setter
    def default_protection_key_id(self, default_protection_key_id):
        """Sets the default_protection_key_id of this GatewayGetDefaultsOutput.


        :param default_protection_key_id: The default_protection_key_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: str
        """

        self._default_protection_key_id = default_protection_key_id

    @property
    def hvp_route_version(self):
        """Gets the hvp_route_version of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The hvp_route_version of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: int
        """
        return self._hvp_route_version

    @hvp_route_version.setter
    def hvp_route_version(self, hvp_route_version):
        """Sets the hvp_route_version of this GatewayGetDefaultsOutput.


        :param hvp_route_version: The hvp_route_version of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: int
        """

        self._hvp_route_version = hvp_route_version

    @property
    def notify_on_status_change(self):
        """Gets the notify_on_status_change of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The notify_on_status_change of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._notify_on_status_change

    @notify_on_status_change.setter
    def notify_on_status_change(self, notify_on_status_change):
        """Sets the notify_on_status_change of this GatewayGetDefaultsOutput.


        :param notify_on_status_change: The notify_on_status_change of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: bool
        """

        self._notify_on_status_change = notify_on_status_change

    @property
    def oidc_access_id(self):
        """Gets the oidc_access_id of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The oidc_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._oidc_access_id

    @oidc_access_id.setter
    def oidc_access_id(self, oidc_access_id):
        """Sets the oidc_access_id of this GatewayGetDefaultsOutput.


        :param oidc_access_id: The oidc_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: str
        """

        self._oidc_access_id = oidc_access_id

    @property
    def saml_access_id(self):
        """Gets the saml_access_id of this GatewayGetDefaultsOutput.  # noqa: E501


        :return: The saml_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._saml_access_id

    @saml_access_id.setter
    def saml_access_id(self, saml_access_id):
        """Sets the saml_access_id of this GatewayGetDefaultsOutput.


        :param saml_access_id: The saml_access_id of this GatewayGetDefaultsOutput.  # noqa: E501
        :type: str
        """

        self._saml_access_id = saml_access_id

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
        if not isinstance(other, GatewayGetDefaultsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayGetDefaultsOutput):
            return True

        return self.to_dict() != other.to_dict()
