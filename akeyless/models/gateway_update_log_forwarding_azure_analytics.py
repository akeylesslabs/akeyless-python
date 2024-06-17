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


class GatewayUpdateLogForwardingAzureAnalytics(object):
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
        'enable': 'str',
        'json': 'bool',
        'output_format': 'str',
        'pull_interval': 'str',
        'token': 'str',
        'uid_token': 'str',
        'workspace_id': 'str',
        'workspace_key': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'json': 'json',
        'output_format': 'output-format',
        'pull_interval': 'pull-interval',
        'token': 'token',
        'uid_token': 'uid-token',
        'workspace_id': 'workspace-id',
        'workspace_key': 'workspace-key'
    }

    def __init__(self, enable='true', json=False, output_format='text', pull_interval='10', token=None, uid_token=None, workspace_id=None, workspace_key=None, local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateLogForwardingAzureAnalytics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable = None
        self._json = None
        self._output_format = None
        self._pull_interval = None
        self._token = None
        self._uid_token = None
        self._workspace_id = None
        self._workspace_key = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if json is not None:
            self.json = json
        if output_format is not None:
            self.output_format = output_format
        if pull_interval is not None:
            self.pull_interval = pull_interval
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_key is not None:
            self.workspace_key = workspace_key

    @property
    def enable(self):
        """Gets the enable of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Enable Log Forwarding [true/false]  # noqa: E501

        :return: The enable of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GatewayUpdateLogForwardingAzureAnalytics.

        Enable Log Forwarding [true/false]  # noqa: E501

        :param enable: The enable of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._enable = enable

    @property
    def json(self):
        """Gets the json of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateLogForwardingAzureAnalytics.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def output_format(self):
        """Gets the output_format of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Logs format [text/json]  # noqa: E501

        :return: The output_format of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this GatewayUpdateLogForwardingAzureAnalytics.

        Logs format [text/json]  # noqa: E501

        :param output_format: The output_format of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._output_format = output_format

    @property
    def pull_interval(self):
        """Gets the pull_interval of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Pull interval in seconds  # noqa: E501

        :return: The pull_interval of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._pull_interval

    @pull_interval.setter
    def pull_interval(self, pull_interval):
        """Sets the pull_interval of this GatewayUpdateLogForwardingAzureAnalytics.

        Pull interval in seconds  # noqa: E501

        :param pull_interval: The pull_interval of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._pull_interval = pull_interval

    @property
    def token(self):
        """Gets the token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateLogForwardingAzureAnalytics.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateLogForwardingAzureAnalytics.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def workspace_id(self):
        """Gets the workspace_id of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Azure workspace id  # noqa: E501

        :return: The workspace_id of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this GatewayUpdateLogForwardingAzureAnalytics.

        Azure workspace id  # noqa: E501

        :param workspace_id: The workspace_id of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def workspace_key(self):
        """Gets the workspace_key of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501

        Azure workspace key  # noqa: E501

        :return: The workspace_key of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._workspace_key

    @workspace_key.setter
    def workspace_key(self, workspace_key):
        """Sets the workspace_key of this GatewayUpdateLogForwardingAzureAnalytics.

        Azure workspace key  # noqa: E501

        :param workspace_key: The workspace_key of this GatewayUpdateLogForwardingAzureAnalytics.  # noqa: E501
        :type: str
        """

        self._workspace_key = workspace_key

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
        if not isinstance(other, GatewayUpdateLogForwardingAzureAnalytics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateLogForwardingAzureAnalytics):
            return True

        return self.to_dict() != other.to_dict()