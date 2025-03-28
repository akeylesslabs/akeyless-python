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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetCertificateValue(BaseModel):
    """
    GetCertificateValue
    """ # noqa: E501
    cert_issuer_name: Optional[StrictStr] = Field(default=None, description="The parent PKI Certificate Issuer's name of the certificate, required when used with display-id and token", alias="cert-issuer-name")
    display_id: Optional[StrictStr] = Field(default=None, description="Certificate display ID", alias="display-id")
    ignore_cache: Optional[StrictStr] = Field(default='false', description="Retrieve the Secret value without checking the Gateway's cache [true/false]. This flag is only relevant when using the RestAPI", alias="ignore-cache")
    issuance_token: Optional[StrictStr] = Field(default=None, description="Token for getting the issued certificate", alias="issuance-token")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: Optional[StrictStr] = Field(default=None, description="Certificate name")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    version: Optional[StrictInt] = Field(default=None, description="Certificate version")
    __properties: ClassVar[List[str]] = ["cert-issuer-name", "display-id", "ignore-cache", "issuance-token", "json", "name", "token", "uid-token", "version"]

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
        """Create an instance of GetCertificateValue from a JSON string"""
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
        """Create an instance of GetCertificateValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cert-issuer-name": obj.get("cert-issuer-name"),
            "display-id": obj.get("display-id"),
            "ignore-cache": obj.get("ignore-cache") if obj.get("ignore-cache") is not None else 'false',
            "issuance-token": obj.get("issuance-token"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "version": obj.get("version")
        })
        return _obj


