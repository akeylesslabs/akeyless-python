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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from akeyless.models.classic_key_status_info import ClassicKeyStatusInfo
from akeyless.models.external_kms_key_id import ExternalKMSKeyId
from typing import Optional, Set
from typing_extensions import Self

class ClassicKeyTargetInfo(BaseModel):
    """
    ClassicKeyTargetInfo
    """ # noqa: E501
    external_kms_id: Optional[ExternalKMSKeyId] = None
    key_purpose: Optional[List[StrictStr]] = None
    key_status: Optional[ClassicKeyStatusInfo] = None
    target_assoc_id: Optional[StrictStr] = None
    target_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["external_kms_id", "key_purpose", "key_status", "target_assoc_id", "target_type"]

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
        """Create an instance of ClassicKeyTargetInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of external_kms_id
        if self.external_kms_id:
            _dict['external_kms_id'] = self.external_kms_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of key_status
        if self.key_status:
            _dict['key_status'] = self.key_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClassicKeyTargetInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_kms_id": ExternalKMSKeyId.from_dict(obj["external_kms_id"]) if obj.get("external_kms_id") is not None else None,
            "key_purpose": obj.get("key_purpose"),
            "key_status": ClassicKeyStatusInfo.from_dict(obj["key_status"]) if obj.get("key_status") is not None else None,
            "target_assoc_id": obj.get("target_assoc_id"),
            "target_type": obj.get("target_type")
        })
        return _obj


