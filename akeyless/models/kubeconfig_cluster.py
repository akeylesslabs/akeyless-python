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


class KubeconfigCluster(object):
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
        'certificate_authority': 'str',
        'certificate_authority_data': 'str',
        'server': 'str'
    }

    attribute_map = {
        'certificate_authority': 'certificate-authority',
        'certificate_authority_data': 'certificate-authority-data',
        'server': 'server'
    }

    def __init__(self, certificate_authority=None, certificate_authority_data=None, server=None, local_vars_configuration=None):  # noqa: E501
        """KubeconfigCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate_authority = None
        self._certificate_authority_data = None
        self._server = None
        self.discriminator = None

        if certificate_authority is not None:
            self.certificate_authority = certificate_authority
        if certificate_authority_data is not None:
            self.certificate_authority_data = certificate_authority_data
        if server is not None:
            self.server = server

    @property
    def certificate_authority(self):
        """Gets the certificate_authority of this KubeconfigCluster.  # noqa: E501

        CertificateAuthority is optional and can be omitted if not used.  # noqa: E501

        :return: The certificate_authority of this KubeconfigCluster.  # noqa: E501
        :rtype: str
        """
        return self._certificate_authority

    @certificate_authority.setter
    def certificate_authority(self, certificate_authority):
        """Sets the certificate_authority of this KubeconfigCluster.

        CertificateAuthority is optional and can be omitted if not used.  # noqa: E501

        :param certificate_authority: The certificate_authority of this KubeconfigCluster.  # noqa: E501
        :type: str
        """

        self._certificate_authority = certificate_authority

    @property
    def certificate_authority_data(self):
        """Gets the certificate_authority_data of this KubeconfigCluster.  # noqa: E501


        :return: The certificate_authority_data of this KubeconfigCluster.  # noqa: E501
        :rtype: str
        """
        return self._certificate_authority_data

    @certificate_authority_data.setter
    def certificate_authority_data(self, certificate_authority_data):
        """Sets the certificate_authority_data of this KubeconfigCluster.


        :param certificate_authority_data: The certificate_authority_data of this KubeconfigCluster.  # noqa: E501
        :type: str
        """

        self._certificate_authority_data = certificate_authority_data

    @property
    def server(self):
        """Gets the server of this KubeconfigCluster.  # noqa: E501


        :return: The server of this KubeconfigCluster.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this KubeconfigCluster.


        :param server: The server of this KubeconfigCluster.  # noqa: E501
        :type: str
        """

        self._server = server

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
        if not isinstance(other, KubeconfigCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeconfigCluster):
            return True

        return self.to_dict() != other.to_dict()