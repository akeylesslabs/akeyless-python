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


class BastionConfigReplyObj(object):
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
        'cluster_id': 'str',
        'desktop_app': 'SraDesktopAppConf',
        'gator_cluster_id': 'int',
        '_global': 'BastionGlobalConf',
        'ssh_bastion': 'SshBastionConf',
        'web_bastion': 'WebBastionConf'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'desktop_app': 'desktop_app',
        'gator_cluster_id': 'gator_cluster_id',
        '_global': 'global',
        'ssh_bastion': 'ssh_bastion',
        'web_bastion': 'web_bastion'
    }

    def __init__(self, cluster_id=None, desktop_app=None, gator_cluster_id=None, _global=None, ssh_bastion=None, web_bastion=None, local_vars_configuration=None):  # noqa: E501
        """BastionConfigReplyObj - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._desktop_app = None
        self._gator_cluster_id = None
        self.__global = None
        self._ssh_bastion = None
        self._web_bastion = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if desktop_app is not None:
            self.desktop_app = desktop_app
        if gator_cluster_id is not None:
            self.gator_cluster_id = gator_cluster_id
        if _global is not None:
            self._global = _global
        if ssh_bastion is not None:
            self.ssh_bastion = ssh_bastion
        if web_bastion is not None:
            self.web_bastion = web_bastion

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BastionConfigReplyObj.  # noqa: E501


        :return: The cluster_id of this BastionConfigReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BastionConfigReplyObj.


        :param cluster_id: The cluster_id of this BastionConfigReplyObj.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def desktop_app(self):
        """Gets the desktop_app of this BastionConfigReplyObj.  # noqa: E501


        :return: The desktop_app of this BastionConfigReplyObj.  # noqa: E501
        :rtype: SraDesktopAppConf
        """
        return self._desktop_app

    @desktop_app.setter
    def desktop_app(self, desktop_app):
        """Sets the desktop_app of this BastionConfigReplyObj.


        :param desktop_app: The desktop_app of this BastionConfigReplyObj.  # noqa: E501
        :type: SraDesktopAppConf
        """

        self._desktop_app = desktop_app

    @property
    def gator_cluster_id(self):
        """Gets the gator_cluster_id of this BastionConfigReplyObj.  # noqa: E501


        :return: The gator_cluster_id of this BastionConfigReplyObj.  # noqa: E501
        :rtype: int
        """
        return self._gator_cluster_id

    @gator_cluster_id.setter
    def gator_cluster_id(self, gator_cluster_id):
        """Sets the gator_cluster_id of this BastionConfigReplyObj.


        :param gator_cluster_id: The gator_cluster_id of this BastionConfigReplyObj.  # noqa: E501
        :type: int
        """

        self._gator_cluster_id = gator_cluster_id

    @property
    def _global(self):
        """Gets the _global of this BastionConfigReplyObj.  # noqa: E501


        :return: The _global of this BastionConfigReplyObj.  # noqa: E501
        :rtype: BastionGlobalConf
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this BastionConfigReplyObj.


        :param _global: The _global of this BastionConfigReplyObj.  # noqa: E501
        :type: BastionGlobalConf
        """

        self.__global = _global

    @property
    def ssh_bastion(self):
        """Gets the ssh_bastion of this BastionConfigReplyObj.  # noqa: E501


        :return: The ssh_bastion of this BastionConfigReplyObj.  # noqa: E501
        :rtype: SshBastionConf
        """
        return self._ssh_bastion

    @ssh_bastion.setter
    def ssh_bastion(self, ssh_bastion):
        """Sets the ssh_bastion of this BastionConfigReplyObj.


        :param ssh_bastion: The ssh_bastion of this BastionConfigReplyObj.  # noqa: E501
        :type: SshBastionConf
        """

        self._ssh_bastion = ssh_bastion

    @property
    def web_bastion(self):
        """Gets the web_bastion of this BastionConfigReplyObj.  # noqa: E501


        :return: The web_bastion of this BastionConfigReplyObj.  # noqa: E501
        :rtype: WebBastionConf
        """
        return self._web_bastion

    @web_bastion.setter
    def web_bastion(self, web_bastion):
        """Sets the web_bastion of this BastionConfigReplyObj.


        :param web_bastion: The web_bastion of this BastionConfigReplyObj.  # noqa: E501
        :type: WebBastionConf
        """

        self._web_bastion = web_bastion

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
        if not isinstance(other, BastionConfigReplyObj):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BastionConfigReplyObj):
            return True

        return self.to_dict() != other.to_dict()
