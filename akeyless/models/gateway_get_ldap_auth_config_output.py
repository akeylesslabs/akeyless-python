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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GatewayGetLdapAuthConfigOutput(BaseModel):
    """
    GatewayGetLdapAuthConfigOutput
    """ # noqa: E501
    ldap_access_id: Optional[StrictStr] = None
    ldap_anonymous_search: Optional[StrictBool] = None
    ldap_bind_dn: Optional[StrictStr] = None
    ldap_bind_password: Optional[StrictStr] = None
    ldap_cert: Optional[StrictStr] = None
    ldap_enable: Optional[StrictBool] = None
    ldap_group_attr: Optional[StrictStr] = None
    ldap_group_dn: Optional[StrictStr] = None
    ldap_group_filter: Optional[StrictStr] = None
    ldap_private_key: Optional[StrictStr] = None
    ldap_token_expiration: Optional[StrictStr] = None
    ldap_url: Optional[StrictStr] = None
    ldap_user_attr: Optional[StrictStr] = None
    ldap_user_dn: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["ldap_access_id", "ldap_anonymous_search", "ldap_bind_dn", "ldap_bind_password", "ldap_cert", "ldap_enable", "ldap_group_attr", "ldap_group_dn", "ldap_group_filter", "ldap_private_key", "ldap_token_expiration", "ldap_url", "ldap_user_attr", "ldap_user_dn"]

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
        """Create an instance of GatewayGetLdapAuthConfigOutput from a JSON string"""
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
        """Create an instance of GatewayGetLdapAuthConfigOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ldap_access_id": obj.get("ldap_access_id"),
            "ldap_anonymous_search": obj.get("ldap_anonymous_search"),
            "ldap_bind_dn": obj.get("ldap_bind_dn"),
            "ldap_bind_password": obj.get("ldap_bind_password"),
            "ldap_cert": obj.get("ldap_cert"),
            "ldap_enable": obj.get("ldap_enable"),
            "ldap_group_attr": obj.get("ldap_group_attr"),
            "ldap_group_dn": obj.get("ldap_group_dn"),
            "ldap_group_filter": obj.get("ldap_group_filter"),
            "ldap_private_key": obj.get("ldap_private_key"),
            "ldap_token_expiration": obj.get("ldap_token_expiration"),
            "ldap_url": obj.get("ldap_url"),
            "ldap_user_attr": obj.get("ldap_user_attr"),
            "ldap_user_dn": obj.get("ldap_user_dn")
        })
        return _obj


