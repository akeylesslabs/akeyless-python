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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KubernetesAccessRules(BaseModel):
    """
    KubernetesAccessRules
    """ # noqa: E501
    alg: Optional[StrictStr] = None
    audience: Optional[StrictStr] = Field(default=None, description="Audience is an optional Kubernetes jwt claim to verify")
    bound_namespaces: Optional[List[StrictStr]] = Field(default=None, description="A list of namespaces that the authentication is restricted to.")
    bound_pod_names: Optional[List[StrictStr]] = Field(default=None, description="A list of pods names that the authentication is restricted to.")
    bound_service_account_names: Optional[List[StrictStr]] = Field(default=None, description="A list of service account names that the authentication is restricted to.")
    gen_key_pair: Optional[StrictStr] = Field(default=None, description="Generate public/private key (the private key is required for the K8S Auth Config in the Akeyless Gateway)")
    pub_key: Optional[StrictStr] = Field(default=None, description="The public key value of the Kubernetes auth method configuration in the Akeyless Gateway.")
    __properties: ClassVar[List[str]] = ["alg", "audience", "bound_namespaces", "bound_pod_names", "bound_service_account_names", "gen_key_pair", "pub_key"]

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
        """Create an instance of KubernetesAccessRules from a JSON string"""
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
        """Create an instance of KubernetesAccessRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alg": obj.get("alg"),
            "audience": obj.get("audience"),
            "bound_namespaces": obj.get("bound_namespaces"),
            "bound_pod_names": obj.get("bound_pod_names"),
            "bound_service_account_names": obj.get("bound_service_account_names"),
            "gen_key_pair": obj.get("gen_key_pair"),
            "pub_key": obj.get("pub_key")
        })
        return _obj


