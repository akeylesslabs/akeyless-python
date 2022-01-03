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


class SignPKICertWithClassicKey(object):
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
        'common_name': 'str',
        'country': 'str',
        'display_id': 'str',
        'dns_names': 'str',
        'key_usage': 'str',
        'locality': 'str',
        'organizational_units': 'str',
        'organizations': 'str',
        'password': 'str',
        'postal_code': 'str',
        'province': 'str',
        'public_key_pem_data': 'str',
        'signing_method': 'str',
        'street_address': 'str',
        'token': 'str',
        'ttl': 'int',
        'uid_token': 'str',
        'uri_sans': 'str',
        'username': 'str',
        'version': 'int'
    }

    attribute_map = {
        'common_name': 'common-name',
        'country': 'country',
        'display_id': 'display-id',
        'dns_names': 'dns-names',
        'key_usage': 'key-usage',
        'locality': 'locality',
        'organizational_units': 'organizational-units',
        'organizations': 'organizations',
        'password': 'password',
        'postal_code': 'postal-code',
        'province': 'province',
        'public_key_pem_data': 'public-key-pem-data',
        'signing_method': 'signing-method',
        'street_address': 'street-address',
        'token': 'token',
        'ttl': 'ttl',
        'uid_token': 'uid-token',
        'uri_sans': 'uri-sans',
        'username': 'username',
        'version': 'version'
    }

    def __init__(self, common_name=None, country=None, display_id=None, dns_names=None, key_usage='DigitalSignature,KeyAgreement,KeyEncipherment', locality=None, organizational_units=None, organizations=None, password=None, postal_code=None, province=None, public_key_pem_data=None, signing_method=None, street_address=None, token=None, ttl=None, uid_token=None, uri_sans=None, username=None, version=None, local_vars_configuration=None):  # noqa: E501
        """SignPKICertWithClassicKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._common_name = None
        self._country = None
        self._display_id = None
        self._dns_names = None
        self._key_usage = None
        self._locality = None
        self._organizational_units = None
        self._organizations = None
        self._password = None
        self._postal_code = None
        self._province = None
        self._public_key_pem_data = None
        self._signing_method = None
        self._street_address = None
        self._token = None
        self._ttl = None
        self._uid_token = None
        self._uri_sans = None
        self._username = None
        self._version = None
        self.discriminator = None

        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        self.display_id = display_id
        if dns_names is not None:
            self.dns_names = dns_names
        if key_usage is not None:
            self.key_usage = key_usage
        if locality is not None:
            self.locality = locality
        if organizational_units is not None:
            self.organizational_units = organizational_units
        if organizations is not None:
            self.organizations = organizations
        if password is not None:
            self.password = password
        if postal_code is not None:
            self.postal_code = postal_code
        if province is not None:
            self.province = province
        if public_key_pem_data is not None:
            self.public_key_pem_data = public_key_pem_data
        self.signing_method = signing_method
        if street_address is not None:
            self.street_address = street_address
        if token is not None:
            self.token = token
        self.ttl = ttl
        if uid_token is not None:
            self.uid_token = uid_token
        if uri_sans is not None:
            self.uri_sans = uri_sans
        if username is not None:
            self.username = username
        self.version = version

    @property
    def common_name(self):
        """Gets the common_name of this SignPKICertWithClassicKey.  # noqa: E501

        The common name to be included in the PKI certificate  # noqa: E501

        :return: The common_name of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this SignPKICertWithClassicKey.

        The common name to be included in the PKI certificate  # noqa: E501

        :param common_name: The common_name of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def country(self):
        """Gets the country of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of the country that will be set in the issued certificate  # noqa: E501

        :return: The country of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SignPKICertWithClassicKey.

        A comma-separated list of the country that will be set in the issued certificate  # noqa: E501

        :param country: The country of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def display_id(self):
        """Gets the display_id of this SignPKICertWithClassicKey.  # noqa: E501

        The name of the key to use in the sign PKI Cert process  # noqa: E501

        :return: The display_id of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this SignPKICertWithClassicKey.

        The name of the key to use in the sign PKI Cert process  # noqa: E501

        :param display_id: The display_id of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and display_id is None:  # noqa: E501
            raise ValueError("Invalid value for `display_id`, must not be `None`")  # noqa: E501

        self._display_id = display_id

    @property
    def dns_names(self):
        """Gets the dns_names of this SignPKICertWithClassicKey.  # noqa: E501

        DNS Names to be included in the PKI certificate (in a comma-delimited list)  # noqa: E501

        :return: The dns_names of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        """Sets the dns_names of this SignPKICertWithClassicKey.

        DNS Names to be included in the PKI certificate (in a comma-delimited list)  # noqa: E501

        :param dns_names: The dns_names of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._dns_names = dns_names

    @property
    def key_usage(self):
        """Gets the key_usage of this SignPKICertWithClassicKey.  # noqa: E501

        key-usage  # noqa: E501

        :return: The key_usage of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this SignPKICertWithClassicKey.

        key-usage  # noqa: E501

        :param key_usage: The key_usage of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._key_usage = key_usage

    @property
    def locality(self):
        """Gets the locality of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of the locality that will be set in the issued certificate  # noqa: E501

        :return: The locality of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this SignPKICertWithClassicKey.

        A comma-separated list of the locality that will be set in the issued certificate  # noqa: E501

        :param locality: The locality of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def organizational_units(self):
        """Gets the organizational_units of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of organizational units (OU) that will be set in the issued certificate  # noqa: E501

        :return: The organizational_units of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._organizational_units

    @organizational_units.setter
    def organizational_units(self, organizational_units):
        """Sets the organizational_units of this SignPKICertWithClassicKey.

        A comma-separated list of organizational units (OU) that will be set in the issued certificate  # noqa: E501

        :param organizational_units: The organizational_units of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._organizational_units = organizational_units

    @property
    def organizations(self):
        """Gets the organizations of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of organizations (O) that will be set in the issued certificate  # noqa: E501

        :return: The organizations of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this SignPKICertWithClassicKey.

        A comma-separated list of organizations (O) that will be set in the issued certificate  # noqa: E501

        :param organizations: The organizations of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._organizations = organizations

    @property
    def password(self):
        """Gets the password of this SignPKICertWithClassicKey.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignPKICertWithClassicKey.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def postal_code(self):
        """Gets the postal_code of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of the postal code that will be set in the issued certificate  # noqa: E501

        :return: The postal_code of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SignPKICertWithClassicKey.

        A comma-separated list of the postal code that will be set in the issued certificate  # noqa: E501

        :param postal_code: The postal_code of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def province(self):
        """Gets the province of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of the province that will be set in the issued certificate  # noqa: E501

        :return: The province of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this SignPKICertWithClassicKey.

        A comma-separated list of the province that will be set in the issued certificate  # noqa: E501

        :param province: The province of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def public_key_pem_data(self):
        """Gets the public_key_pem_data of this SignPKICertWithClassicKey.  # noqa: E501

        PublicKey using for signing in a PEM format.  # noqa: E501

        :return: The public_key_pem_data of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key_pem_data

    @public_key_pem_data.setter
    def public_key_pem_data(self, public_key_pem_data):
        """Sets the public_key_pem_data of this SignPKICertWithClassicKey.

        PublicKey using for signing in a PEM format.  # noqa: E501

        :param public_key_pem_data: The public_key_pem_data of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._public_key_pem_data = public_key_pem_data

    @property
    def signing_method(self):
        """Gets the signing_method of this SignPKICertWithClassicKey.  # noqa: E501

        SigningMethod  # noqa: E501

        :return: The signing_method of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._signing_method

    @signing_method.setter
    def signing_method(self, signing_method):
        """Sets the signing_method of this SignPKICertWithClassicKey.

        SigningMethod  # noqa: E501

        :param signing_method: The signing_method of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signing_method is None:  # noqa: E501
            raise ValueError("Invalid value for `signing_method`, must not be `None`")  # noqa: E501

        self._signing_method = signing_method

    @property
    def street_address(self):
        """Gets the street_address of this SignPKICertWithClassicKey.  # noqa: E501

        A comma-separated list of the street address that will be set in the issued certificate  # noqa: E501

        :return: The street_address of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this SignPKICertWithClassicKey.

        A comma-separated list of the street address that will be set in the issued certificate  # noqa: E501

        :param street_address: The street_address of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def token(self):
        """Gets the token of this SignPKICertWithClassicKey.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SignPKICertWithClassicKey.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def ttl(self):
        """Gets the ttl of this SignPKICertWithClassicKey.  # noqa: E501

        he requested Time To Live for the certificate, in seconds  # noqa: E501

        :return: The ttl of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this SignPKICertWithClassicKey.

        he requested Time To Live for the certificate, in seconds  # noqa: E501

        :param ttl: The ttl of this SignPKICertWithClassicKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ttl is None:  # noqa: E501
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def uid_token(self):
        """Gets the uid_token of this SignPKICertWithClassicKey.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this SignPKICertWithClassicKey.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def uri_sans(self):
        """Gets the uri_sans of this SignPKICertWithClassicKey.  # noqa: E501

        The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list)  # noqa: E501

        :return: The uri_sans of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._uri_sans

    @uri_sans.setter
    def uri_sans(self, uri_sans):
        """Sets the uri_sans of this SignPKICertWithClassicKey.

        The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list)  # noqa: E501

        :param uri_sans: The uri_sans of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._uri_sans = uri_sans

    @property
    def username(self):
        """Gets the username of this SignPKICertWithClassicKey.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SignPKICertWithClassicKey.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this SignPKICertWithClassicKey.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def version(self):
        """Gets the version of this SignPKICertWithClassicKey.  # noqa: E501

        classic key version  # noqa: E501

        :return: The version of this SignPKICertWithClassicKey.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SignPKICertWithClassicKey.

        classic key version  # noqa: E501

        :param version: The version of this SignPKICertWithClassicKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, SignPKICertWithClassicKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignPKICertWithClassicKey):
            return True

        return self.to_dict() != other.to_dict()