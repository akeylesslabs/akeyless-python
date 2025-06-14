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


class GetCertificateValue(object):
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
        'cert_issuer_name': 'str',
        'display_id': 'str',
        'ignore_cache': 'str',
        'issuance_token': 'str',
        'json': 'bool',
        'name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'version': 'int'
    }

    attribute_map = {
        'cert_issuer_name': 'cert-issuer-name',
        'display_id': 'display-id',
        'ignore_cache': 'ignore-cache',
        'issuance_token': 'issuance-token',
        'json': 'json',
        'name': 'name',
        'token': 'token',
        'uid_token': 'uid-token',
        'version': 'version'
    }

    def __init__(self, cert_issuer_name=None, display_id=None, ignore_cache='false', issuance_token=None, json=False, name=None, token=None, uid_token=None, version=None, local_vars_configuration=None):  # noqa: E501
        """GetCertificateValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cert_issuer_name = None
        self._display_id = None
        self._ignore_cache = None
        self._issuance_token = None
        self._json = None
        self._name = None
        self._token = None
        self._uid_token = None
        self._version = None
        self.discriminator = None

        if cert_issuer_name is not None:
            self.cert_issuer_name = cert_issuer_name
        if display_id is not None:
            self.display_id = display_id
        if ignore_cache is not None:
            self.ignore_cache = ignore_cache
        if issuance_token is not None:
            self.issuance_token = issuance_token
        if json is not None:
            self.json = json
        if name is not None:
            self.name = name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if version is not None:
            self.version = version

    @property
    def cert_issuer_name(self):
        """Gets the cert_issuer_name of this GetCertificateValue.  # noqa: E501

        The parent PKI Certificate Issuer's name of the certificate, required when used with display-id and token  # noqa: E501

        :return: The cert_issuer_name of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._cert_issuer_name

    @cert_issuer_name.setter
    def cert_issuer_name(self, cert_issuer_name):
        """Sets the cert_issuer_name of this GetCertificateValue.

        The parent PKI Certificate Issuer's name of the certificate, required when used with display-id and token  # noqa: E501

        :param cert_issuer_name: The cert_issuer_name of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._cert_issuer_name = cert_issuer_name

    @property
    def display_id(self):
        """Gets the display_id of this GetCertificateValue.  # noqa: E501

        Certificate display ID  # noqa: E501

        :return: The display_id of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this GetCertificateValue.

        Certificate display ID  # noqa: E501

        :param display_id: The display_id of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._display_id = display_id

    @property
    def ignore_cache(self):
        """Gets the ignore_cache of this GetCertificateValue.  # noqa: E501

        Retrieve the Secret value without checking the Gateway's cache [true/false]. This flag is only relevant when using the RestAPI  # noqa: E501

        :return: The ignore_cache of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._ignore_cache

    @ignore_cache.setter
    def ignore_cache(self, ignore_cache):
        """Sets the ignore_cache of this GetCertificateValue.

        Retrieve the Secret value without checking the Gateway's cache [true/false]. This flag is only relevant when using the RestAPI  # noqa: E501

        :param ignore_cache: The ignore_cache of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._ignore_cache = ignore_cache

    @property
    def issuance_token(self):
        """Gets the issuance_token of this GetCertificateValue.  # noqa: E501

        Token for getting the issued certificate  # noqa: E501

        :return: The issuance_token of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._issuance_token

    @issuance_token.setter
    def issuance_token(self, issuance_token):
        """Sets the issuance_token of this GetCertificateValue.

        Token for getting the issued certificate  # noqa: E501

        :param issuance_token: The issuance_token of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._issuance_token = issuance_token

    @property
    def json(self):
        """Gets the json of this GetCertificateValue.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GetCertificateValue.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GetCertificateValue.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GetCertificateValue.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GetCertificateValue.  # noqa: E501

        Certificate name  # noqa: E501

        :return: The name of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCertificateValue.

        Certificate name  # noqa: E501

        :param name: The name of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def token(self):
        """Gets the token of this GetCertificateValue.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetCertificateValue.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GetCertificateValue.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GetCertificateValue.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GetCertificateValue.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GetCertificateValue.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def version(self):
        """Gets the version of this GetCertificateValue.  # noqa: E501

        Certificate version  # noqa: E501

        :return: The version of this GetCertificateValue.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetCertificateValue.

        Certificate version  # noqa: E501

        :param version: The version of this GetCertificateValue.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, GetCertificateValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCertificateValue):
            return True

        return self.to_dict() != other.to_dict()
