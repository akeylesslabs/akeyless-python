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

class CreatePingTarget(BaseModel):
    """
    createPingTarget is a command that creates a new target. [Deprecated: Use target-create-ping command]
    """ # noqa: E501
    administrative_port: Optional[StrictStr] = Field(default='9999', description="Ping Federate administrative port", alias="administrative-port")
    authorization_port: Optional[StrictStr] = Field(default='9031', description="Ping Federate authorization port", alias="authorization-port")
    comment: Optional[StrictStr] = Field(default=None, description="Deprecated - use description")
    description: Optional[StrictStr] = Field(default=None, description="Description of the object")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    key: Optional[StrictStr] = Field(default=None, description="The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)")
    max_versions: Optional[StrictStr] = Field(default=None, description="Set the maximum number of versions, limited by the account settings defaults.", alias="max-versions")
    name: StrictStr = Field(description="Target name")
    password: Optional[StrictStr] = Field(default=None, description="Ping Federate privileged user password")
    ping_url: Optional[StrictStr] = Field(default=None, description="Ping URL", alias="ping-url")
    privileged_user: Optional[StrictStr] = Field(default=None, description="Ping Federate privileged user", alias="privileged-user")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    __properties: ClassVar[List[str]] = ["administrative-port", "authorization-port", "comment", "description", "json", "key", "max-versions", "name", "password", "ping-url", "privileged-user", "token", "uid-token"]

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
        """Create an instance of CreatePingTarget from a JSON string"""
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
        """Create an instance of CreatePingTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "administrative-port": obj.get("administrative-port") if obj.get("administrative-port") is not None else '9999',
            "authorization-port": obj.get("authorization-port") if obj.get("authorization-port") is not None else '9031',
            "comment": obj.get("comment"),
            "description": obj.get("description"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "key": obj.get("key"),
            "max-versions": obj.get("max-versions"),
            "name": obj.get("name"),
            "password": obj.get("password"),
            "ping-url": obj.get("ping-url"),
            "privileged-user": obj.get("privileged-user"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token")
        })
        return _obj


