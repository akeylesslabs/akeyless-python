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


class TargetUpdateEks(object):
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
        'description': 'str',
        'eks_access_key_id': 'str',
        'eks_cluster_ca_cert': 'str',
        'eks_cluster_endpoint': 'str',
        'eks_cluster_name': 'str',
        'eks_region': 'str',
        'eks_secret_access_key': 'str',
        'json': 'bool',
        'keep_prev_version': 'str',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'new_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'use_gw_cloud_identity': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'eks_access_key_id': 'eks-access-key-id',
        'eks_cluster_ca_cert': 'eks-cluster-ca-cert',
        'eks_cluster_endpoint': 'eks-cluster-endpoint',
        'eks_cluster_name': 'eks-cluster-name',
        'eks_region': 'eks-region',
        'eks_secret_access_key': 'eks-secret-access-key',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'new_name': 'new-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'use_gw_cloud_identity': 'use-gw-cloud-identity'
    }

    def __init__(self, description=None, eks_access_key_id=None, eks_cluster_ca_cert=None, eks_cluster_endpoint=None, eks_cluster_name=None, eks_region='us-east-2', eks_secret_access_key=None, json=False, keep_prev_version=None, key=None, max_versions=None, name=None, new_name=None, token=None, uid_token=None, use_gw_cloud_identity=None, local_vars_configuration=None):  # noqa: E501
        """TargetUpdateEks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._eks_access_key_id = None
        self._eks_cluster_ca_cert = None
        self._eks_cluster_endpoint = None
        self._eks_cluster_name = None
        self._eks_region = None
        self._eks_secret_access_key = None
        self._json = None
        self._keep_prev_version = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._new_name = None
        self._token = None
        self._uid_token = None
        self._use_gw_cloud_identity = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.eks_access_key_id = eks_access_key_id
        self.eks_cluster_ca_cert = eks_cluster_ca_cert
        self.eks_cluster_endpoint = eks_cluster_endpoint
        self.eks_cluster_name = eks_cluster_name
        if eks_region is not None:
            self.eks_region = eks_region
        self.eks_secret_access_key = eks_secret_access_key
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if use_gw_cloud_identity is not None:
            self.use_gw_cloud_identity = use_gw_cloud_identity

    @property
    def description(self):
        """Gets the description of this TargetUpdateEks.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TargetUpdateEks.

        Description of the object  # noqa: E501

        :param description: The description of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eks_access_key_id(self):
        """Gets the eks_access_key_id of this TargetUpdateEks.  # noqa: E501

        Access Key ID  # noqa: E501

        :return: The eks_access_key_id of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_access_key_id

    @eks_access_key_id.setter
    def eks_access_key_id(self, eks_access_key_id):
        """Sets the eks_access_key_id of this TargetUpdateEks.

        Access Key ID  # noqa: E501

        :param eks_access_key_id: The eks_access_key_id of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_access_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_access_key_id`, must not be `None`")  # noqa: E501

        self._eks_access_key_id = eks_access_key_id

    @property
    def eks_cluster_ca_cert(self):
        """Gets the eks_cluster_ca_cert of this TargetUpdateEks.  # noqa: E501

        EKS cluster CA certificate  # noqa: E501

        :return: The eks_cluster_ca_cert of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_ca_cert

    @eks_cluster_ca_cert.setter
    def eks_cluster_ca_cert(self, eks_cluster_ca_cert):
        """Sets the eks_cluster_ca_cert of this TargetUpdateEks.

        EKS cluster CA certificate  # noqa: E501

        :param eks_cluster_ca_cert: The eks_cluster_ca_cert of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_ca_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_ca_cert`, must not be `None`")  # noqa: E501

        self._eks_cluster_ca_cert = eks_cluster_ca_cert

    @property
    def eks_cluster_endpoint(self):
        """Gets the eks_cluster_endpoint of this TargetUpdateEks.  # noqa: E501

        EKS cluster URL endpoint  # noqa: E501

        :return: The eks_cluster_endpoint of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_endpoint

    @eks_cluster_endpoint.setter
    def eks_cluster_endpoint(self, eks_cluster_endpoint):
        """Sets the eks_cluster_endpoint of this TargetUpdateEks.

        EKS cluster URL endpoint  # noqa: E501

        :param eks_cluster_endpoint: The eks_cluster_endpoint of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_endpoint`, must not be `None`")  # noqa: E501

        self._eks_cluster_endpoint = eks_cluster_endpoint

    @property
    def eks_cluster_name(self):
        """Gets the eks_cluster_name of this TargetUpdateEks.  # noqa: E501

        EKS cluster name  # noqa: E501

        :return: The eks_cluster_name of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_name

    @eks_cluster_name.setter
    def eks_cluster_name(self, eks_cluster_name):
        """Sets the eks_cluster_name of this TargetUpdateEks.

        EKS cluster name  # noqa: E501

        :param eks_cluster_name: The eks_cluster_name of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_name is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_name`, must not be `None`")  # noqa: E501

        self._eks_cluster_name = eks_cluster_name

    @property
    def eks_region(self):
        """Gets the eks_region of this TargetUpdateEks.  # noqa: E501

        Region  # noqa: E501

        :return: The eks_region of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_region

    @eks_region.setter
    def eks_region(self, eks_region):
        """Sets the eks_region of this TargetUpdateEks.

        Region  # noqa: E501

        :param eks_region: The eks_region of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._eks_region = eks_region

    @property
    def eks_secret_access_key(self):
        """Gets the eks_secret_access_key of this TargetUpdateEks.  # noqa: E501

        Secret Access Key  # noqa: E501

        :return: The eks_secret_access_key of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_secret_access_key

    @eks_secret_access_key.setter
    def eks_secret_access_key(self, eks_secret_access_key):
        """Sets the eks_secret_access_key of this TargetUpdateEks.

        Secret Access Key  # noqa: E501

        :param eks_secret_access_key: The eks_secret_access_key of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_secret_access_key`, must not be `None`")  # noqa: E501

        self._eks_secret_access_key = eks_secret_access_key

    @property
    def json(self):
        """Gets the json of this TargetUpdateEks.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this TargetUpdateEks.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this TargetUpdateEks.

        Set output format to JSON  # noqa: E501

        :param json: The json of this TargetUpdateEks.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this TargetUpdateEks.  # noqa: E501

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :return: The keep_prev_version of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this TargetUpdateEks.

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :param keep_prev_version: The keep_prev_version of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this TargetUpdateEks.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TargetUpdateEks.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this TargetUpdateEks.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this TargetUpdateEks.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this TargetUpdateEks.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetUpdateEks.

        Target name  # noqa: E501

        :param name: The name of this TargetUpdateEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this TargetUpdateEks.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this TargetUpdateEks.

        New target name  # noqa: E501

        :param new_name: The new_name of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def token(self):
        """Gets the token of this TargetUpdateEks.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TargetUpdateEks.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this TargetUpdateEks.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this TargetUpdateEks.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this TargetUpdateEks.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this TargetUpdateEks.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_gw_cloud_identity(self):
        """Gets the use_gw_cloud_identity of this TargetUpdateEks.  # noqa: E501


        :return: The use_gw_cloud_identity of this TargetUpdateEks.  # noqa: E501
        :rtype: bool
        """
        return self._use_gw_cloud_identity

    @use_gw_cloud_identity.setter
    def use_gw_cloud_identity(self, use_gw_cloud_identity):
        """Sets the use_gw_cloud_identity of this TargetUpdateEks.


        :param use_gw_cloud_identity: The use_gw_cloud_identity of this TargetUpdateEks.  # noqa: E501
        :type: bool
        """

        self._use_gw_cloud_identity = use_gw_cloud_identity

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
        if not isinstance(other, TargetUpdateEks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetUpdateEks):
            return True

        return self.to_dict() != other.to_dict()