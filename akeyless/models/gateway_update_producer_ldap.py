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


class GatewayUpdateProducerLdap(object):
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
        'provider_type': 'str',
        'bind_dn': 'str',
        'bind_dn_password': 'str',
        'delete_protection': 'str',
        'external_username': 'str',
        'fixed_user_claim_keyname': 'str',
        'group_dn': 'str',
        'host_provider': 'str',
        'json': 'bool',
        'ldap_ca_cert': 'str',
        'ldap_url': 'str',
        'name': 'str',
        'new_name': 'str',
        'password_length': 'str',
        'producer_encryption_key_name': 'str',
        'secure_access_bastion_issuer': 'str',
        'secure_access_certificate_issuer': 'str',
        'secure_access_delay': 'int',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_rd_gateway_server': 'str',
        'secure_access_rdp_domain': 'str',
        'tags': 'list[str]',
        'target': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'token_expiration': 'str',
        'uid_token': 'str',
        'user_attribute': 'str',
        'user_dn': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'provider_type': 'ProviderType',
        'bind_dn': 'bind-dn',
        'bind_dn_password': 'bind-dn-password',
        'delete_protection': 'delete_protection',
        'external_username': 'external-username',
        'fixed_user_claim_keyname': 'fixed-user-claim-keyname',
        'group_dn': 'group-dn',
        'host_provider': 'host-provider',
        'json': 'json',
        'ldap_ca_cert': 'ldap-ca-cert',
        'ldap_url': 'ldap-url',
        'name': 'name',
        'new_name': 'new-name',
        'password_length': 'password-length',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_certificate_issuer': 'secure-access-certificate-issuer',
        'secure_access_delay': 'secure-access-delay',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_rd_gateway_server': 'secure-access-rd-gateway-server',
        'secure_access_rdp_domain': 'secure-access-rdp-domain',
        'tags': 'tags',
        'target': 'target',
        'target_name': 'target-name',
        'token': 'token',
        'token_expiration': 'token-expiration',
        'uid_token': 'uid-token',
        'user_attribute': 'user-attribute',
        'user_dn': 'user-dn',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, provider_type=None, bind_dn=None, bind_dn_password=None, delete_protection=None, external_username='false', fixed_user_claim_keyname='ext_username', group_dn=None, host_provider=None, json=False, ldap_ca_cert=None, ldap_url=None, name=None, new_name=None, password_length=None, producer_encryption_key_name=None, secure_access_bastion_issuer=None, secure_access_certificate_issuer=None, secure_access_delay=None, secure_access_enable=None, secure_access_host=None, secure_access_rd_gateway_server=None, secure_access_rdp_domain=None, tags=None, target=None, target_name=None, token=None, token_expiration=None, uid_token=None, user_attribute=None, user_dn=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerLdap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider_type = None
        self._bind_dn = None
        self._bind_dn_password = None
        self._delete_protection = None
        self._external_username = None
        self._fixed_user_claim_keyname = None
        self._group_dn = None
        self._host_provider = None
        self._json = None
        self._ldap_ca_cert = None
        self._ldap_url = None
        self._name = None
        self._new_name = None
        self._password_length = None
        self._producer_encryption_key_name = None
        self._secure_access_bastion_issuer = None
        self._secure_access_certificate_issuer = None
        self._secure_access_delay = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_rd_gateway_server = None
        self._secure_access_rdp_domain = None
        self._tags = None
        self._target = None
        self._target_name = None
        self._token = None
        self._token_expiration = None
        self._uid_token = None
        self._user_attribute = None
        self._user_dn = None
        self._user_ttl = None
        self.discriminator = None

        if provider_type is not None:
            self.provider_type = provider_type
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_dn_password is not None:
            self.bind_dn_password = bind_dn_password
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if external_username is not None:
            self.external_username = external_username
        if fixed_user_claim_keyname is not None:
            self.fixed_user_claim_keyname = fixed_user_claim_keyname
        if group_dn is not None:
            self.group_dn = group_dn
        if host_provider is not None:
            self.host_provider = host_provider
        if json is not None:
            self.json = json
        if ldap_ca_cert is not None:
            self.ldap_ca_cert = ldap_ca_cert
        if ldap_url is not None:
            self.ldap_url = ldap_url
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password_length is not None:
            self.password_length = password_length
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_certificate_issuer is not None:
            self.secure_access_certificate_issuer = secure_access_certificate_issuer
        if secure_access_delay is not None:
            self.secure_access_delay = secure_access_delay
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if secure_access_rd_gateway_server is not None:
            self.secure_access_rd_gateway_server = secure_access_rd_gateway_server
        if secure_access_rdp_domain is not None:
            self.secure_access_rdp_domain = secure_access_rdp_domain
        if tags is not None:
            self.tags = tags
        if target is not None:
            self.target = target
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if token_expiration is not None:
            self.token_expiration = token_expiration
        if uid_token is not None:
            self.uid_token = uid_token
        if user_attribute is not None:
            self.user_attribute = user_attribute
        if user_dn is not None:
            self.user_dn = user_dn
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def provider_type(self):
        """Gets the provider_type of this GatewayUpdateProducerLdap.  # noqa: E501


        :return: The provider_type of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this GatewayUpdateProducerLdap.


        :param provider_type: The provider_type of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def bind_dn(self):
        """Gets the bind_dn of this GatewayUpdateProducerLdap.  # noqa: E501

        Bind DN  # noqa: E501

        :return: The bind_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this GatewayUpdateProducerLdap.

        Bind DN  # noqa: E501

        :param bind_dn: The bind_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_dn_password(self):
        """Gets the bind_dn_password of this GatewayUpdateProducerLdap.  # noqa: E501

        Bind DN Password  # noqa: E501

        :return: The bind_dn_password of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn_password

    @bind_dn_password.setter
    def bind_dn_password(self, bind_dn_password):
        """Sets the bind_dn_password of this GatewayUpdateProducerLdap.

        Bind DN Password  # noqa: E501

        :param bind_dn_password: The bind_dn_password of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._bind_dn_password = bind_dn_password

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayUpdateProducerLdap.  # noqa: E501

        Protection from accidental deletion of this object [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayUpdateProducerLdap.

        Protection from accidental deletion of this object [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def external_username(self):
        """Gets the external_username of this GatewayUpdateProducerLdap.  # noqa: E501

        Externally provided username [true/false]  # noqa: E501

        :return: The external_username of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._external_username

    @external_username.setter
    def external_username(self, external_username):
        """Sets the external_username of this GatewayUpdateProducerLdap.

        Externally provided username [true/false]  # noqa: E501

        :param external_username: The external_username of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._external_username = external_username

    @property
    def fixed_user_claim_keyname(self):
        """Gets the fixed_user_claim_keyname of this GatewayUpdateProducerLdap.  # noqa: E501

        For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for external-username=true)  # noqa: E501

        :return: The fixed_user_claim_keyname of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._fixed_user_claim_keyname

    @fixed_user_claim_keyname.setter
    def fixed_user_claim_keyname(self, fixed_user_claim_keyname):
        """Sets the fixed_user_claim_keyname of this GatewayUpdateProducerLdap.

        For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for external-username=true)  # noqa: E501

        :param fixed_user_claim_keyname: The fixed_user_claim_keyname of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._fixed_user_claim_keyname = fixed_user_claim_keyname

    @property
    def group_dn(self):
        """Gets the group_dn of this GatewayUpdateProducerLdap.  # noqa: E501

        Group DN which the temporary user should be added  # noqa: E501

        :return: The group_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._group_dn

    @group_dn.setter
    def group_dn(self, group_dn):
        """Sets the group_dn of this GatewayUpdateProducerLdap.

        Group DN which the temporary user should be added  # noqa: E501

        :param group_dn: The group_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._group_dn = group_dn

    @property
    def host_provider(self):
        """Gets the host_provider of this GatewayUpdateProducerLdap.  # noqa: E501

        Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret  # noqa: E501

        :return: The host_provider of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._host_provider

    @host_provider.setter
    def host_provider(self, host_provider):
        """Sets the host_provider of this GatewayUpdateProducerLdap.

        Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret  # noqa: E501

        :param host_provider: The host_provider of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._host_provider = host_provider

    @property
    def json(self):
        """Gets the json of this GatewayUpdateProducerLdap.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateProducerLdap.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def ldap_ca_cert(self):
        """Gets the ldap_ca_cert of this GatewayUpdateProducerLdap.  # noqa: E501

        CA Certificate File Content  # noqa: E501

        :return: The ldap_ca_cert of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._ldap_ca_cert

    @ldap_ca_cert.setter
    def ldap_ca_cert(self, ldap_ca_cert):
        """Sets the ldap_ca_cert of this GatewayUpdateProducerLdap.

        CA Certificate File Content  # noqa: E501

        :param ldap_ca_cert: The ldap_ca_cert of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._ldap_ca_cert = ldap_ca_cert

    @property
    def ldap_url(self):
        """Gets the ldap_url of this GatewayUpdateProducerLdap.  # noqa: E501

        LDAP Server URL  # noqa: E501

        :return: The ldap_url of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """Sets the ldap_url of this GatewayUpdateProducerLdap.

        LDAP Server URL  # noqa: E501

        :param ldap_url: The ldap_url of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._ldap_url = ldap_url

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerLdap.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerLdap.

        Dynamic secret name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerLdap.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerLdap.

        Dynamic secret name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password_length(self):
        """Gets the password_length of this GatewayUpdateProducerLdap.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this GatewayUpdateProducerLdap.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerLdap.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerLdap.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this GatewayUpdateProducerLdap.  # noqa: E501

        Deprecated. use secure-access-certificate-issuer  # noqa: E501

        :return: The secure_access_bastion_issuer of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this GatewayUpdateProducerLdap.

        Deprecated. use secure-access-certificate-issuer  # noqa: E501

        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_certificate_issuer(self):
        """Gets the secure_access_certificate_issuer of this GatewayUpdateProducerLdap.  # noqa: E501

        Path to the SSH Certificate Issuer for your Akeyless Secure Access  # noqa: E501

        :return: The secure_access_certificate_issuer of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_certificate_issuer

    @secure_access_certificate_issuer.setter
    def secure_access_certificate_issuer(self, secure_access_certificate_issuer):
        """Sets the secure_access_certificate_issuer of this GatewayUpdateProducerLdap.

        Path to the SSH Certificate Issuer for your Akeyless Secure Access  # noqa: E501

        :param secure_access_certificate_issuer: The secure_access_certificate_issuer of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._secure_access_certificate_issuer = secure_access_certificate_issuer

    @property
    def secure_access_delay(self):
        """Gets the secure_access_delay of this GatewayUpdateProducerLdap.  # noqa: E501

        The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds  # noqa: E501

        :return: The secure_access_delay of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: int
        """
        return self._secure_access_delay

    @secure_access_delay.setter
    def secure_access_delay(self, secure_access_delay):
        """Sets the secure_access_delay of this GatewayUpdateProducerLdap.

        The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds  # noqa: E501

        :param secure_access_delay: The secure_access_delay of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: int
        """

        self._secure_access_delay = secure_access_delay

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayUpdateProducerLdap.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayUpdateProducerLdap.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this GatewayUpdateProducerLdap.  # noqa: E501

        Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)  # noqa: E501

        :return: The secure_access_host of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this GatewayUpdateProducerLdap.

        Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)  # noqa: E501

        :param secure_access_host: The secure_access_host of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_rd_gateway_server(self):
        """Gets the secure_access_rd_gateway_server of this GatewayUpdateProducerLdap.  # noqa: E501

        RD Gateway server  # noqa: E501

        :return: The secure_access_rd_gateway_server of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_rd_gateway_server

    @secure_access_rd_gateway_server.setter
    def secure_access_rd_gateway_server(self, secure_access_rd_gateway_server):
        """Sets the secure_access_rd_gateway_server of this GatewayUpdateProducerLdap.

        RD Gateway server  # noqa: E501

        :param secure_access_rd_gateway_server: The secure_access_rd_gateway_server of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._secure_access_rd_gateway_server = secure_access_rd_gateway_server

    @property
    def secure_access_rdp_domain(self):
        """Gets the secure_access_rdp_domain of this GatewayUpdateProducerLdap.  # noqa: E501

        Required when the Dynamic Secret is used for a domain user  # noqa: E501

        :return: The secure_access_rdp_domain of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_rdp_domain

    @secure_access_rdp_domain.setter
    def secure_access_rdp_domain(self, secure_access_rdp_domain):
        """Sets the secure_access_rdp_domain of this GatewayUpdateProducerLdap.

        Required when the Dynamic Secret is used for a domain user  # noqa: E501

        :param secure_access_rdp_domain: The secure_access_rdp_domain of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._secure_access_rdp_domain = secure_access_rdp_domain

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerLdap.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerLdap.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target(self):
        """Gets the target of this GatewayUpdateProducerLdap.  # noqa: E501

        A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times  # noqa: E501

        :return: The target of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: list[str]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this GatewayUpdateProducerLdap.

        A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times  # noqa: E501

        :param target: The target of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: list[str]
        """

        self._target = target

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerLdap.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerLdap.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerLdap.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerLdap.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def token_expiration(self):
        """Gets the token_expiration of this GatewayUpdateProducerLdap.  # noqa: E501

        Token expiration  # noqa: E501

        :return: The token_expiration of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._token_expiration

    @token_expiration.setter
    def token_expiration(self, token_expiration):
        """Sets the token_expiration of this GatewayUpdateProducerLdap.

        Token expiration  # noqa: E501

        :param token_expiration: The token_expiration of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._token_expiration = token_expiration

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerLdap.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerLdap.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_attribute(self):
        """Gets the user_attribute of this GatewayUpdateProducerLdap.  # noqa: E501

        User Attribute  # noqa: E501

        :return: The user_attribute of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute

    @user_attribute.setter
    def user_attribute(self, user_attribute):
        """Sets the user_attribute of this GatewayUpdateProducerLdap.

        User Attribute  # noqa: E501

        :param user_attribute: The user_attribute of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._user_attribute = user_attribute

    @property
    def user_dn(self):
        """Gets the user_dn of this GatewayUpdateProducerLdap.  # noqa: E501

        User DN  # noqa: E501

        :return: The user_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn):
        """Sets the user_dn of this GatewayUpdateProducerLdap.

        User DN  # noqa: E501

        :param user_dn: The user_dn of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._user_dn = user_dn

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerLdap.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerLdap.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerLdap.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerLdap.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

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
        if not isinstance(other, GatewayUpdateProducerLdap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerLdap):
            return True

        return self.to_dict() != other.to_dict()
