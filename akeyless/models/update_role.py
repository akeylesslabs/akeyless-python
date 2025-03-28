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

class UpdateRole(BaseModel):
    """
    UpdateRole
    """ # noqa: E501
    analytics_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.", alias="analytics-access")
    audit_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view audit logs. Currently only 'none', 'own' and 'all' values are supported, allowing associated auth methods to view audit logs produced by the same auth methods.", alias="audit-access")
    delete_protection: Optional[StrictStr] = Field(default=None, description="Protection from accidental deletion of this object [true/false]")
    description: Optional[StrictStr] = Field(default='default_comment', description="Description of the object")
    event_center_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view Event Center. Currently only 'none', 'own' and 'all' values are supported", alias="event-center-access")
    event_forwarder_access: Optional[StrictStr] = Field(default=None, description="Allow this role to manage Event Forwarders. Currently only 'none' and 'all' values are supported.", alias="event-forwarder-access")
    gw_analytics_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view gw analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.", alias="gw-analytics-access")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: StrictStr = Field(description="Role name")
    new_comment: Optional[StrictStr] = Field(default='default_comment', description="Deprecated - use description", alias="new-comment")
    new_name: Optional[StrictStr] = Field(default=None, description="New Role name", alias="new-name")
    sra_reports_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view SRA Clusters. Currently only 'none', 'own', 'all' values are supported.", alias="sra-reports-access")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    usage_reports_access: Optional[StrictStr] = Field(default=None, description="Allow this role to view Usage Report. Currently only 'none' and 'all' values are supported.", alias="usage-reports-access")
    __properties: ClassVar[List[str]] = ["analytics-access", "audit-access", "delete_protection", "description", "event-center-access", "event-forwarder-access", "gw-analytics-access", "json", "name", "new-comment", "new-name", "sra-reports-access", "token", "uid-token", "usage-reports-access"]

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
        """Create an instance of UpdateRole from a JSON string"""
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
        """Create an instance of UpdateRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analytics-access": obj.get("analytics-access"),
            "audit-access": obj.get("audit-access"),
            "delete_protection": obj.get("delete_protection"),
            "description": obj.get("description") if obj.get("description") is not None else 'default_comment',
            "event-center-access": obj.get("event-center-access"),
            "event-forwarder-access": obj.get("event-forwarder-access"),
            "gw-analytics-access": obj.get("gw-analytics-access"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "new-comment": obj.get("new-comment") if obj.get("new-comment") is not None else 'default_comment',
            "new-name": obj.get("new-name"),
            "sra-reports-access": obj.get("sra-reports-access"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "usage-reports-access": obj.get("usage-reports-access")
        })
        return _obj


