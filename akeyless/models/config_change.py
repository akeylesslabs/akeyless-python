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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from akeyless.models.config_hash import ConfigHash
from akeyless.models.last_config_change import LastConfigChange
from akeyless.models.last_status_info import LastStatusInfo
from akeyless.models.required_activity import RequiredActivity
from typing import Optional, Set
from typing_extensions import Self

class ConfigChange(BaseModel):
    """
    ConfigChange
    """ # noqa: E501
    config_hash: Optional[ConfigHash] = None
    last_change: Optional[LastConfigChange] = None
    last_status: Optional[LastStatusInfo] = None
    required_activity: Optional[RequiredActivity] = None
    update_stamp: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["config_hash", "last_change", "last_status", "required_activity", "update_stamp"]

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
        """Create an instance of ConfigChange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config_hash
        if self.config_hash:
            _dict['config_hash'] = self.config_hash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_change
        if self.last_change:
            _dict['last_change'] = self.last_change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_status
        if self.last_status:
            _dict['last_status'] = self.last_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of required_activity
        if self.required_activity:
            _dict['required_activity'] = self.required_activity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigChange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config_hash": ConfigHash.from_dict(obj["config_hash"]) if obj.get("config_hash") is not None else None,
            "last_change": LastConfigChange.from_dict(obj["last_change"]) if obj.get("last_change") is not None else None,
            "last_status": LastStatusInfo.from_dict(obj["last_status"]) if obj.get("last_status") is not None else None,
            "required_activity": RequiredActivity.from_dict(obj["required_activity"]) if obj.get("required_activity") is not None else None,
            "update_stamp": obj.get("update_stamp")
        })
        return _obj


