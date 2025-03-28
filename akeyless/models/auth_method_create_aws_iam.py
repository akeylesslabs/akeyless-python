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

class AuthMethodCreateAwsIam(BaseModel):
    """
    authMethodCreateAwsIam is a command that creates a new Auth Method that will be able to authenticate using AWS IAM credentials.
    """ # noqa: E501
    access_expires: Optional[StrictInt] = Field(default=0, description="Access expiration date in Unix timestamp (select 0 for access without expiry date)", alias="access-expires")
    audit_logs_claims: Optional[List[StrictStr]] = Field(default=None, description="Subclaims to include in audit logs, e.g \"--audit-logs-claims email --audit-logs-claims username\"", alias="audit-logs-claims")
    bound_arn: Optional[List[StrictStr]] = Field(default=None, description="A list of full arns that the access is restricted to", alias="bound-arn")
    bound_aws_account_id: List[StrictStr] = Field(description="A list of AWS account-IDs that the access is restricted to", alias="bound-aws-account-id")
    bound_ips: Optional[List[StrictStr]] = Field(default=None, description="A CIDR whitelist with the IPs that the access is restricted to", alias="bound-ips")
    bound_resource_id: Optional[List[StrictStr]] = Field(default=None, description="A list of full resource ids that the access is restricted to", alias="bound-resource-id")
    bound_role_id: Optional[List[StrictStr]] = Field(default=None, description="A list of full role ids that the access is restricted to", alias="bound-role-id")
    bound_role_name: Optional[List[StrictStr]] = Field(default=None, description="A list of full role-name that the access is restricted to", alias="bound-role-name")
    bound_user_id: Optional[List[StrictStr]] = Field(default=None, description="A list of full user ids that the access is restricted to", alias="bound-user-id")
    bound_user_name: Optional[List[StrictStr]] = Field(default=None, description="A list of full user-name that the access is restricted to", alias="bound-user-name")
    delete_protection: Optional[StrictStr] = Field(default=None, description="Protection from accidental deletion of this object [true/false]")
    description: Optional[StrictStr] = Field(default=None, description="Auth Method description")
    expiration_event_in: Optional[List[StrictStr]] = Field(default=None, description="How many days before the expiration of the auth method would you like to be notified.", alias="expiration-event-in")
    force_sub_claims: Optional[StrictBool] = Field(default=None, description="if true: enforce role-association must include sub claims", alias="force-sub-claims")
    gw_bound_ips: Optional[List[StrictStr]] = Field(default=None, description="A CIDR whitelist with the GW IPs that the access is restricted to", alias="gw-bound-ips")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    jwt_ttl: Optional[StrictInt] = Field(default=0, description="Jwt TTL", alias="jwt-ttl")
    name: StrictStr = Field(description="Auth Method name")
    product_type: Optional[List[StrictStr]] = Field(default=None, description="Choose the relevant product type for the auth method [sm, sra, pm, dp, ca]", alias="product-type")
    sts_url: Optional[StrictStr] = Field(default='https://sts.amazonaws.com', description="sts URL", alias="sts-url")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    unique_identifier: Optional[StrictStr] = Field(default=None, description="A unique identifier (ID) value which is a \"sub claim\" name that contains details uniquely identifying that resource. This \"sub claim\" is used to distinguish between different identities.", alias="unique-identifier")
    __properties: ClassVar[List[str]] = ["access-expires", "audit-logs-claims", "bound-arn", "bound-aws-account-id", "bound-ips", "bound-resource-id", "bound-role-id", "bound-role-name", "bound-user-id", "bound-user-name", "delete_protection", "description", "expiration-event-in", "force-sub-claims", "gw-bound-ips", "json", "jwt-ttl", "name", "product-type", "sts-url", "token", "uid-token", "unique-identifier"]

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
        """Create an instance of AuthMethodCreateAwsIam from a JSON string"""
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
        """Create an instance of AuthMethodCreateAwsIam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access-expires": obj.get("access-expires") if obj.get("access-expires") is not None else 0,
            "audit-logs-claims": obj.get("audit-logs-claims"),
            "bound-arn": obj.get("bound-arn"),
            "bound-aws-account-id": obj.get("bound-aws-account-id"),
            "bound-ips": obj.get("bound-ips"),
            "bound-resource-id": obj.get("bound-resource-id"),
            "bound-role-id": obj.get("bound-role-id"),
            "bound-role-name": obj.get("bound-role-name"),
            "bound-user-id": obj.get("bound-user-id"),
            "bound-user-name": obj.get("bound-user-name"),
            "delete_protection": obj.get("delete_protection"),
            "description": obj.get("description"),
            "expiration-event-in": obj.get("expiration-event-in"),
            "force-sub-claims": obj.get("force-sub-claims"),
            "gw-bound-ips": obj.get("gw-bound-ips"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "jwt-ttl": obj.get("jwt-ttl") if obj.get("jwt-ttl") is not None else 0,
            "name": obj.get("name"),
            "product-type": obj.get("product-type"),
            "sts-url": obj.get("sts-url") if obj.get("sts-url") is not None else 'https://sts.amazonaws.com',
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "unique-identifier": obj.get("unique-identifier")
        })
        return _obj


