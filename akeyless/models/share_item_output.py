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
from akeyless.models.response_stop_share_item import ResponseStopShareItem
from akeyless.models.sharing_item_full_info import SharingItemFullInfo
from typing import Optional, Set
from typing_extensions import Self

class ShareItemOutput(BaseModel):
    """
    ShareItemOutput
    """ # noqa: E501
    email_error: Optional[Dict[str, StrictStr]] = None
    items_error: Optional[List[ResponseStopShareItem]] = None
    s_token: Optional[StrictStr] = None
    shared_users: Optional[List[StrictStr]] = None
    shared_users_full_info: Optional[List[SharingItemFullInfo]] = None
    sharing_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["email_error", "items_error", "s_token", "shared_users", "shared_users_full_info", "sharing_url"]

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
        """Create an instance of ShareItemOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items_error (list)
        _items = []
        if self.items_error:
            for _item_items_error in self.items_error:
                if _item_items_error:
                    _items.append(_item_items_error.to_dict())
            _dict['items_error'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shared_users_full_info (list)
        _items = []
        if self.shared_users_full_info:
            for _item_shared_users_full_info in self.shared_users_full_info:
                if _item_shared_users_full_info:
                    _items.append(_item_shared_users_full_info.to_dict())
            _dict['shared_users_full_info'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShareItemOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email_error": obj.get("email_error"),
            "items_error": [ResponseStopShareItem.from_dict(_item) for _item in obj["items_error"]] if obj.get("items_error") is not None else None,
            "s_token": obj.get("s_token"),
            "shared_users": obj.get("shared_users"),
            "shared_users_full_info": [SharingItemFullInfo.from_dict(_item) for _item in obj["shared_users_full_info"]] if obj.get("shared_users_full_info") is not None else None,
            "sharing_url": obj.get("sharing_url")
        })
        return _obj


