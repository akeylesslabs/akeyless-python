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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from akeyless.models.rules import Rules
from typing import Optional, Set
from typing_extensions import Self

class AuthMethodRoleAssociation(BaseModel):
    """
    AuthMethodRoleAssociation includes details of an association between an auth method and a role.
    """ # noqa: E501
    allowed_ops: Optional[List[StrictStr]] = None
    assoc_id: Optional[StrictStr] = None
    auth_method_sub_claims: Optional[Dict[str, List[StrictStr]]] = None
    is_sub_claims_case_sensitive: Optional[StrictBool] = None
    is_subclaims_with_operator: Optional[StrictBool] = None
    role_id: Optional[StrictInt] = None
    role_name: Optional[StrictStr] = None
    rules: Optional[Rules] = None
    __properties: ClassVar[List[str]] = ["allowed_ops", "assoc_id", "auth_method_sub_claims", "is_sub_claims_case_sensitive", "is_subclaims_with_operator", "role_id", "role_name", "rules"]

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
        """Create an instance of AuthMethodRoleAssociation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rules
        if self.rules:
            _dict['rules'] = self.rules.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthMethodRoleAssociation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_ops": obj.get("allowed_ops"),
            "assoc_id": obj.get("assoc_id"),
            "auth_method_sub_claims": obj.get("auth_method_sub_claims"),
            "is_sub_claims_case_sensitive": obj.get("is_sub_claims_case_sensitive"),
            "is_subclaims_with_operator": obj.get("is_subclaims_with_operator"),
            "role_id": obj.get("role_id"),
            "role_name": obj.get("role_name"),
            "rules": Rules.from_dict(obj["rules"]) if obj.get("rules") is not None else None
        })
        return _obj


