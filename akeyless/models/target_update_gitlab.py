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

class TargetUpdateGitlab(BaseModel):
    """
    TargetUpdateGitlab
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the object")
    gitlab_access_token: Optional[StrictStr] = Field(default=None, description="Gitlab access token", alias="gitlab-access-token")
    gitlab_certificate: Optional[StrictStr] = Field(default=None, description="Gitlab tls certificate (base64 encoded)", alias="gitlab-certificate")
    gitlab_url: Optional[StrictStr] = Field(default='https://gitlab.com/', description="Gitlab base url", alias="gitlab-url")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    keep_prev_version: Optional[StrictStr] = Field(default=None, description="Whether to keep previous version [true/false]. If not set, use default according to account settings", alias="keep-prev-version")
    key: Optional[StrictStr] = Field(default=None, description="The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)")
    max_versions: Optional[StrictStr] = Field(default=None, description="Set the maximum number of versions, limited by the account settings defaults.", alias="max-versions")
    name: StrictStr = Field(description="Target name")
    new_name: Optional[StrictStr] = Field(default=None, description="New target name", alias="new-name")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    __properties: ClassVar[List[str]] = ["description", "gitlab-access-token", "gitlab-certificate", "gitlab-url", "json", "keep-prev-version", "key", "max-versions", "name", "new-name", "token", "uid-token"]

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
        """Create an instance of TargetUpdateGitlab from a JSON string"""
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
        """Create an instance of TargetUpdateGitlab from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "gitlab-access-token": obj.get("gitlab-access-token"),
            "gitlab-certificate": obj.get("gitlab-certificate"),
            "gitlab-url": obj.get("gitlab-url") if obj.get("gitlab-url") is not None else 'https://gitlab.com/',
            "json": obj.get("json") if obj.get("json") is not None else False,
            "keep-prev-version": obj.get("keep-prev-version"),
            "key": obj.get("key"),
            "max-versions": obj.get("max-versions"),
            "name": obj.get("name"),
            "new-name": obj.get("new-name"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token")
        })
        return _obj


