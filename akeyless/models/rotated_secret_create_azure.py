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


class RotatedSecretCreateAzure(object):
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
        'api_id': 'str',
        'api_key': 'str',
        'application_id': 'str',
        'authentication_credentials': 'str',
        'auto_rotate': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'password_length': 'str',
        'rotate_after_disconnect': 'str',
        'rotation_hour': 'int',
        'rotation_interval': 'str',
        'rotator_type': 'str',
        'secure_access_enable': 'str',
        'secure_access_url': 'str',
        'secure_access_web': 'bool',
        'secure_access_web_browsing': 'bool',
        'secure_access_web_proxy': 'bool',
        'storage_account_key_name': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'api_id': 'api-id',
        'api_key': 'api-key',
        'application_id': 'application-id',
        'authentication_credentials': 'authentication-credentials',
        'auto_rotate': 'auto-rotate',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'password_length': 'password-length',
        'rotate_after_disconnect': 'rotate-after-disconnect',
        'rotation_hour': 'rotation-hour',
        'rotation_interval': 'rotation-interval',
        'rotator_type': 'rotator-type',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_url': 'secure-access-url',
        'secure_access_web': 'secure-access-web',
        'secure_access_web_browsing': 'secure-access-web-browsing',
        'secure_access_web_proxy': 'secure-access-web-proxy',
        'storage_account_key_name': 'storage-account-key-name',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, api_id=None, api_key=None, application_id=None, authentication_credentials='use-user-creds', auto_rotate=None, delete_protection=None, description=None, json=False, key=None, max_versions=None, name=None, password_length=None, rotate_after_disconnect='false', rotation_hour=None, rotation_interval=None, rotator_type=None, secure_access_enable=None, secure_access_url=None, secure_access_web=False, secure_access_web_browsing=False, secure_access_web_proxy=False, storage_account_key_name=None, tags=None, target_name=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """RotatedSecretCreateAzure - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_id = None
        self._api_key = None
        self._application_id = None
        self._authentication_credentials = None
        self._auto_rotate = None
        self._delete_protection = None
        self._description = None
        self._json = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._password_length = None
        self._rotate_after_disconnect = None
        self._rotation_hour = None
        self._rotation_interval = None
        self._rotator_type = None
        self._secure_access_enable = None
        self._secure_access_url = None
        self._secure_access_web = None
        self._secure_access_web_browsing = None
        self._secure_access_web_proxy = None
        self._storage_account_key_name = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_key is not None:
            self.api_key = api_key
        if application_id is not None:
            self.application_id = application_id
        if authentication_credentials is not None:
            self.authentication_credentials = authentication_credentials
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if password_length is not None:
            self.password_length = password_length
        if rotate_after_disconnect is not None:
            self.rotate_after_disconnect = rotate_after_disconnect
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        self.rotator_type = rotator_type
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_url is not None:
            self.secure_access_url = secure_access_url
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
        if secure_access_web_browsing is not None:
            self.secure_access_web_browsing = secure_access_web_browsing
        if secure_access_web_proxy is not None:
            self.secure_access_web_proxy = secure_access_web_proxy
        if storage_account_key_name is not None:
            self.storage_account_key_name = storage_account_key_name
        if tags is not None:
            self.tags = tags
        self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def api_id(self):
        """Gets the api_id of this RotatedSecretCreateAzure.  # noqa: E501

        API ID to rotate (relevant only for rotator-type=api-key)  # noqa: E501

        :return: The api_id of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this RotatedSecretCreateAzure.

        API ID to rotate (relevant only for rotator-type=api-key)  # noqa: E501

        :param api_id: The api_id of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._api_id = api_id

    @property
    def api_key(self):
        """Gets the api_key of this RotatedSecretCreateAzure.  # noqa: E501

        API key to rotate (relevant only for rotator-type=api-key)  # noqa: E501

        :return: The api_key of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this RotatedSecretCreateAzure.

        API key to rotate (relevant only for rotator-type=api-key)  # noqa: E501

        :param api_key: The api_key of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def application_id(self):
        """Gets the application_id of this RotatedSecretCreateAzure.  # noqa: E501

        Id of the azure app that hold the serect to be rotated (relevant only for rotator-type=api-key & authentication-credentials=use-target-creds)  # noqa: E501

        :return: The application_id of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this RotatedSecretCreateAzure.

        Id of the azure app that hold the serect to be rotated (relevant only for rotator-type=api-key & authentication-credentials=use-target-creds)  # noqa: E501

        :param application_id: The application_id of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def authentication_credentials(self):
        """Gets the authentication_credentials of this RotatedSecretCreateAzure.  # noqa: E501

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :return: The authentication_credentials of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._authentication_credentials

    @authentication_credentials.setter
    def authentication_credentials(self, authentication_credentials):
        """Sets the authentication_credentials of this RotatedSecretCreateAzure.

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :param authentication_credentials: The authentication_credentials of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._authentication_credentials = authentication_credentials

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this RotatedSecretCreateAzure.  # noqa: E501

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :return: The auto_rotate of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this RotatedSecretCreateAzure.

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :param auto_rotate: The auto_rotate of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._auto_rotate = auto_rotate

    @property
    def delete_protection(self):
        """Gets the delete_protection of this RotatedSecretCreateAzure.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this RotatedSecretCreateAzure.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this RotatedSecretCreateAzure.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RotatedSecretCreateAzure.

        Description of the object  # noqa: E501

        :param description: The description of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this RotatedSecretCreateAzure.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this RotatedSecretCreateAzure.

        Set output format to JSON  # noqa: E501

        :param json: The json of this RotatedSecretCreateAzure.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this RotatedSecretCreateAzure.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RotatedSecretCreateAzure.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this RotatedSecretCreateAzure.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this RotatedSecretCreateAzure.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this RotatedSecretCreateAzure.  # noqa: E501

        Rotated secret name  # noqa: E501

        :return: The name of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RotatedSecretCreateAzure.

        Rotated secret name  # noqa: E501

        :param name: The name of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password_length(self):
        """Gets the password_length of this RotatedSecretCreateAzure.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this RotatedSecretCreateAzure.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def rotate_after_disconnect(self):
        """Gets the rotate_after_disconnect of this RotatedSecretCreateAzure.  # noqa: E501

        Rotate the value of the secret after SRA session ends [true/false]  # noqa: E501

        :return: The rotate_after_disconnect of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._rotate_after_disconnect

    @rotate_after_disconnect.setter
    def rotate_after_disconnect(self, rotate_after_disconnect):
        """Sets the rotate_after_disconnect of this RotatedSecretCreateAzure.

        Rotate the value of the secret after SRA session ends [true/false]  # noqa: E501

        :param rotate_after_disconnect: The rotate_after_disconnect of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._rotate_after_disconnect = rotate_after_disconnect

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this RotatedSecretCreateAzure.  # noqa: E501

        The Hour of the rotation in UTC  # noqa: E501

        :return: The rotation_hour of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this RotatedSecretCreateAzure.

        The Hour of the rotation in UTC  # noqa: E501

        :param rotation_hour: The rotation_hour of this RotatedSecretCreateAzure.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this RotatedSecretCreateAzure.  # noqa: E501

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :return: The rotation_interval of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this RotatedSecretCreateAzure.

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :param rotation_interval: The rotation_interval of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._rotation_interval = rotation_interval

    @property
    def rotator_type(self):
        """Gets the rotator_type of this RotatedSecretCreateAzure.  # noqa: E501

        The rotator type. options: [target/password/api-key/azure-storage-account]  # noqa: E501

        :return: The rotator_type of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._rotator_type

    @rotator_type.setter
    def rotator_type(self, rotator_type):
        """Sets the rotator_type of this RotatedSecretCreateAzure.

        The rotator type. options: [target/password/api-key/azure-storage-account]  # noqa: E501

        :param rotator_type: The rotator_type of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rotator_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rotator_type`, must not be `None`")  # noqa: E501

        self._rotator_type = rotator_type

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this RotatedSecretCreateAzure.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this RotatedSecretCreateAzure.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_url(self):
        """Gets the secure_access_url of this RotatedSecretCreateAzure.  # noqa: E501

        Destination URL to inject secrets  # noqa: E501

        :return: The secure_access_url of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_url

    @secure_access_url.setter
    def secure_access_url(self, secure_access_url):
        """Sets the secure_access_url of this RotatedSecretCreateAzure.

        Destination URL to inject secrets  # noqa: E501

        :param secure_access_url: The secure_access_url of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._secure_access_url = secure_access_url

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this RotatedSecretCreateAzure.  # noqa: E501

        Enable Web Secure Remote Access  # noqa: E501

        :return: The secure_access_web of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this RotatedSecretCreateAzure.

        Enable Web Secure Remote Access  # noqa: E501

        :param secure_access_web: The secure_access_web of this RotatedSecretCreateAzure.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def secure_access_web_browsing(self):
        """Gets the secure_access_web_browsing of this RotatedSecretCreateAzure.  # noqa: E501

        Secure browser via Akeyless Web Access Bastion  # noqa: E501

        :return: The secure_access_web_browsing of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_browsing

    @secure_access_web_browsing.setter
    def secure_access_web_browsing(self, secure_access_web_browsing):
        """Sets the secure_access_web_browsing of this RotatedSecretCreateAzure.

        Secure browser via Akeyless Web Access Bastion  # noqa: E501

        :param secure_access_web_browsing: The secure_access_web_browsing of this RotatedSecretCreateAzure.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_browsing = secure_access_web_browsing

    @property
    def secure_access_web_proxy(self):
        """Gets the secure_access_web_proxy of this RotatedSecretCreateAzure.  # noqa: E501

        Web-Proxy via Akeyless Web Access Bastion  # noqa: E501

        :return: The secure_access_web_proxy of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_proxy

    @secure_access_web_proxy.setter
    def secure_access_web_proxy(self, secure_access_web_proxy):
        """Sets the secure_access_web_proxy of this RotatedSecretCreateAzure.

        Web-Proxy via Akeyless Web Access Bastion  # noqa: E501

        :param secure_access_web_proxy: The secure_access_web_proxy of this RotatedSecretCreateAzure.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_proxy = secure_access_web_proxy

    @property
    def storage_account_key_name(self):
        """Gets the storage_account_key_name of this RotatedSecretCreateAzure.  # noqa: E501

        The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account)  # noqa: E501

        :return: The storage_account_key_name of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._storage_account_key_name

    @storage_account_key_name.setter
    def storage_account_key_name(self, storage_account_key_name):
        """Sets the storage_account_key_name of this RotatedSecretCreateAzure.

        The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account)  # noqa: E501

        :param storage_account_key_name: The storage_account_key_name of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._storage_account_key_name = storage_account_key_name

    @property
    def tags(self):
        """Gets the tags of this RotatedSecretCreateAzure.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RotatedSecretCreateAzure.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this RotatedSecretCreateAzure.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this RotatedSecretCreateAzure.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this RotatedSecretCreateAzure.

        Target name  # noqa: E501

        :param target_name: The target_name of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_name is None:  # noqa: E501
            raise ValueError("Invalid value for `target_name`, must not be `None`")  # noqa: E501

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this RotatedSecretCreateAzure.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RotatedSecretCreateAzure.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this RotatedSecretCreateAzure.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this RotatedSecretCreateAzure.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this RotatedSecretCreateAzure.  # noqa: E501

        The user principal name to rotate his password (relevant only for rotator-type=password)  # noqa: E501

        :return: The username of this RotatedSecretCreateAzure.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RotatedSecretCreateAzure.

        The user principal name to rotate his password (relevant only for rotator-type=password)  # noqa: E501

        :param username: The username of this RotatedSecretCreateAzure.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, RotatedSecretCreateAzure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RotatedSecretCreateAzure):
            return True

        return self.to_dict() != other.to_dict()