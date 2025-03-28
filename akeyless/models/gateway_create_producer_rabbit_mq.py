# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GatewayCreateProducerRabbitMQ(BaseModel):
    """
    gatewayCreateProducerRabbitMQ is a command that creates rabbitmq producer [Deprecated: Use dynamic-secret-create-rabbitmq command]
    """ # noqa: E501
    delete_protection: Optional[StrictStr] = Field(default=None, description="Protection from accidental deletion of this object [true/false]")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: StrictStr = Field(description="Dynamic secret name")
    password_length: Optional[StrictStr] = Field(default=None, description="The length of the password to be generated", alias="password-length")
    producer_encryption_key_name: Optional[StrictStr] = Field(default=None, description="Dynamic producer encryption key", alias="producer-encryption-key-name")
    rabbitmq_admin_pwd: Optional[StrictStr] = Field(default=None, description="RabbitMQ Admin password", alias="rabbitmq-admin-pwd")
    rabbitmq_admin_user: Optional[StrictStr] = Field(default=None, description="RabbitMQ Admin User", alias="rabbitmq-admin-user")
    rabbitmq_server_uri: Optional[StrictStr] = Field(default=None, description="Server URI", alias="rabbitmq-server-uri")
    rabbitmq_user_conf_permission: Optional[StrictStr] = Field(default=None, description="User configuration permission", alias="rabbitmq-user-conf-permission")
    rabbitmq_user_read_permission: Optional[StrictStr] = Field(default=None, description="User read permission", alias="rabbitmq-user-read-permission")
    rabbitmq_user_tags: Optional[StrictStr] = Field(default=None, description="User Tags", alias="rabbitmq-user-tags")
    rabbitmq_user_vhost: Optional[StrictStr] = Field(default=None, description="User Virtual Host", alias="rabbitmq-user-vhost")
    rabbitmq_user_write_permission: Optional[StrictStr] = Field(default=None, description="User write permission", alias="rabbitmq-user-write-permission")
    secure_access_enable: Optional[StrictStr] = Field(default=None, description="Enable/Disable secure remote access [true/false]", alias="secure-access-enable")
    secure_access_url: Optional[StrictStr] = Field(default=None, description="Destination URL to inject secrets", alias="secure-access-url")
    secure_access_web: Optional[StrictBool] = Field(default=True, description="Enable Web Secure Remote Access", alias="secure-access-web")
    secure_access_web_browsing: Optional[StrictBool] = Field(default=False, description="Secure browser via Akeyless's Secure Remote Access (SRA)", alias="secure-access-web-browsing")
    secure_access_web_proxy: Optional[StrictBool] = Field(default=False, description="Web-Proxy via Akeyless's Secure Remote Access (SRA)", alias="secure-access-web-proxy")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Add tags attached to this object")
    target_name: Optional[StrictStr] = Field(default=None, description="Target name", alias="target-name")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    user_ttl: Optional[StrictStr] = Field(default='60m', description="User TTL", alias="user-ttl")
    __properties: ClassVar[List[str]] = ["delete_protection", "json", "name", "password-length", "producer-encryption-key-name", "rabbitmq-admin-pwd", "rabbitmq-admin-user", "rabbitmq-server-uri", "rabbitmq-user-conf-permission", "rabbitmq-user-read-permission", "rabbitmq-user-tags", "rabbitmq-user-vhost", "rabbitmq-user-write-permission", "secure-access-enable", "secure-access-url", "secure-access-web", "secure-access-web-browsing", "secure-access-web-proxy", "tags", "target-name", "token", "uid-token", "user-ttl"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GatewayCreateProducerRabbitMQ from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GatewayCreateProducerRabbitMQ from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delete_protection": obj.get("delete_protection"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "password-length": obj.get("password-length"),
            "producer-encryption-key-name": obj.get("producer-encryption-key-name"),
            "rabbitmq-admin-pwd": obj.get("rabbitmq-admin-pwd"),
            "rabbitmq-admin-user": obj.get("rabbitmq-admin-user"),
            "rabbitmq-server-uri": obj.get("rabbitmq-server-uri"),
            "rabbitmq-user-conf-permission": obj.get("rabbitmq-user-conf-permission"),
            "rabbitmq-user-read-permission": obj.get("rabbitmq-user-read-permission"),
            "rabbitmq-user-tags": obj.get("rabbitmq-user-tags"),
            "rabbitmq-user-vhost": obj.get("rabbitmq-user-vhost"),
            "rabbitmq-user-write-permission": obj.get("rabbitmq-user-write-permission"),
            "secure-access-enable": obj.get("secure-access-enable"),
            "secure-access-url": obj.get("secure-access-url"),
            "secure-access-web": obj.get("secure-access-web") if obj.get("secure-access-web") is not None else True,
            "secure-access-web-browsing": obj.get("secure-access-web-browsing") if obj.get("secure-access-web-browsing") is not None else False,
            "secure-access-web-proxy": obj.get("secure-access-web-proxy") if obj.get("secure-access-web-proxy") is not None else False,
            "tags": obj.get("tags"),
            "target-name": obj.get("target-name"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "user-ttl": obj.get("user-ttl") if obj.get("user-ttl") is not None else '60m'
        })
        return _obj


