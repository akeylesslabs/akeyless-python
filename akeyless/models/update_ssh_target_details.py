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

class UpdateSSHTargetDetails(BaseModel):
    """
    UpdateSSHTargetDetails
    """ # noqa: E501
    host: Optional[StrictStr] = Field(default=None, description="The ssh host name")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    keep_prev_version: Optional[StrictStr] = Field(default=None, description="Whether to keep previous version [true/false]. If not set, use default according to account settings", alias="keep-prev-version")
    name: StrictStr = Field(description="Target name")
    new_version: Optional[StrictBool] = Field(default=None, description="Deprecated", alias="new-version")
    port: Optional[StrictStr] = Field(default='22', description="ssh port")
    private_key: Optional[StrictStr] = Field(default=None, description="ssh private key", alias="private-key")
    private_key_password: Optional[StrictStr] = Field(default=None, description="The ssh private key password", alias="private-key-password")
    protection_key: Optional[StrictStr] = Field(default=None, description="The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)")
    ssh_password: Optional[StrictStr] = Field(default=None, description="ssh pawssword to rotate", alias="ssh-password")
    ssh_username: Optional[StrictStr] = Field(default=None, description="ssh username", alias="ssh-username")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    __properties: ClassVar[List[str]] = ["host", "json", "keep-prev-version", "name", "new-version", "port", "private-key", "private-key-password", "protection_key", "ssh-password", "ssh-username", "token", "uid-token"]

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
        """Create an instance of UpdateSSHTargetDetails from a JSON string"""
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
        """Create an instance of UpdateSSHTargetDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "keep-prev-version": obj.get("keep-prev-version"),
            "name": obj.get("name"),
            "new-version": obj.get("new-version"),
            "port": obj.get("port") if obj.get("port") is not None else '22',
            "private-key": obj.get("private-key"),
            "private-key-password": obj.get("private-key-password"),
            "protection_key": obj.get("protection_key"),
            "ssh-password": obj.get("ssh-password"),
            "ssh-username": obj.get("ssh-username"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token")
        })
        return _obj


