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
from akeyless.models.gateway_name_info import GatewayNameInfo
from akeyless.models.sra_session_entry_out import SraSessionEntryOut
from typing import Optional, Set
from typing_extensions import Self

class ListSraSessionsOutput(BaseModel):
    """
    ListSraSessionsOutput
    """ # noqa: E501
    allowed_gateways: Optional[List[GatewayNameInfo]] = None
    next_page: Optional[StrictStr] = None
    sessions: Optional[List[SraSessionEntryOut]] = None
    __properties: ClassVar[List[str]] = ["allowed_gateways", "next_page", "sessions"]

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
        """Create an instance of ListSraSessionsOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_gateways (list)
        _items = []
        if self.allowed_gateways:
            for _item_allowed_gateways in self.allowed_gateways:
                if _item_allowed_gateways:
                    _items.append(_item_allowed_gateways.to_dict())
            _dict['allowed_gateways'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sessions (list)
        _items = []
        if self.sessions:
            for _item_sessions in self.sessions:
                if _item_sessions:
                    _items.append(_item_sessions.to_dict())
            _dict['sessions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListSraSessionsOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_gateways": [GatewayNameInfo.from_dict(_item) for _item in obj["allowed_gateways"]] if obj.get("allowed_gateways") is not None else None,
            "next_page": obj.get("next_page"),
            "sessions": [SraSessionEntryOut.from_dict(_item) for _item in obj["sessions"]] if obj.get("sessions") is not None else None
        })
        return _obj


