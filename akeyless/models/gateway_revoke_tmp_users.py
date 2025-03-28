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

class GatewayRevokeTmpUsers(BaseModel):
    """
    gatewayRevokeTmpUsers is a command that revoke producer tmp user [Deprecated: Use dynamic-secret-tmp-creds-delete command]
    """ # noqa: E501
    host: Optional[StrictStr] = Field(default=None, description="Host")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: StrictStr = Field(description="Dynamic secret name")
    revoke_all: Optional[StrictBool] = Field(default=None, description="Revoke All Temp Creds", alias="revoke-all")
    soft_delete: Optional[StrictBool] = Field(default=None, description="Soft Delete", alias="soft-delete")
    tmp_creds_id: Optional[StrictStr] = Field(default=None, description="Tmp Creds ID", alias="tmp-creds-id")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    __properties: ClassVar[List[str]] = ["host", "json", "name", "revoke-all", "soft-delete", "tmp-creds-id", "token", "uid-token"]

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
        """Create an instance of GatewayRevokeTmpUsers from a JSON string"""
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
        """Create an instance of GatewayRevokeTmpUsers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "revoke-all": obj.get("revoke-all"),
            "soft-delete": obj.get("soft-delete"),
            "tmp-creds-id": obj.get("tmp-creds-id"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token")
        })
        return _obj


