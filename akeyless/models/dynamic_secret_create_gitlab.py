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

class DynamicSecretCreateGitlab(BaseModel):
    """
    dynamicSecretCreateGitlab is a command that creates gitlab dynamic secret
    """ # noqa: E501
    delete_protection: Optional[StrictStr] = Field(default=None, description="Protection from accidental deletion of this object [true/false]")
    description: Optional[StrictStr] = Field(default=None, description="Description of the object")
    gitlab_access_token: Optional[StrictStr] = Field(default=None, description="Gitlab access token", alias="gitlab-access-token")
    gitlab_access_type: StrictStr = Field(description="Gitlab access token type [project,group]", alias="gitlab-access-type")
    gitlab_certificate: Optional[StrictStr] = Field(default=None, description="Gitlab tls certificate (base64 encoded)", alias="gitlab-certificate")
    gitlab_role: Optional[StrictStr] = Field(default=None, description="Gitlab role", alias="gitlab-role")
    gitlab_token_scopes: StrictStr = Field(description="Comma-separated list of access token scopes to grant", alias="gitlab-token-scopes")
    gitlab_url: Optional[StrictStr] = Field(default='https://gitlab.com/', description="Gitlab base url", alias="gitlab-url")
    group_name: Optional[StrictStr] = Field(default=None, description="Gitlab group name, required for access-type=group", alias="group-name")
    installation_organization: Optional[StrictStr] = Field(default=None, description="Gitlab project name, required for access-type=project", alias="installation-organization")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: StrictStr = Field(description="Dynamic secret name")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Add tags attached to this object")
    target_name: Optional[StrictStr] = Field(default=None, description="Target name", alias="target-name")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    ttl: Optional[StrictStr] = Field(default=None, description="Access Token TTL")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    __properties: ClassVar[List[str]] = ["delete_protection", "description", "gitlab-access-token", "gitlab-access-type", "gitlab-certificate", "gitlab-role", "gitlab-token-scopes", "gitlab-url", "group-name", "installation-organization", "json", "name", "tags", "target-name", "token", "ttl", "uid-token"]

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
        """Create an instance of DynamicSecretCreateGitlab from a JSON string"""
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
        """Create an instance of DynamicSecretCreateGitlab from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delete_protection": obj.get("delete_protection"),
            "description": obj.get("description"),
            "gitlab-access-token": obj.get("gitlab-access-token"),
            "gitlab-access-type": obj.get("gitlab-access-type"),
            "gitlab-certificate": obj.get("gitlab-certificate"),
            "gitlab-role": obj.get("gitlab-role"),
            "gitlab-token-scopes": obj.get("gitlab-token-scopes"),
            "gitlab-url": obj.get("gitlab-url") if obj.get("gitlab-url") is not None else 'https://gitlab.com/',
            "group-name": obj.get("group-name"),
            "installation-organization": obj.get("installation-organization"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "tags": obj.get("tags"),
            "target-name": obj.get("target-name"),
            "token": obj.get("token"),
            "ttl": obj.get("ttl"),
            "uid-token": obj.get("uid-token")
        })
        return _obj


