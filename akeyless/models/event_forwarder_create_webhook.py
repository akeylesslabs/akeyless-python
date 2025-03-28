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

class EventForwarderCreateWebhook(BaseModel):
    """
    eventForwarderCreateWebhook is a command that creates webhook event forwarder
    """ # noqa: E501
    auth_methods_event_source_locations: Optional[List[StrictStr]] = Field(default=None, description="Auth Method Event sources", alias="auth-methods-event-source-locations")
    auth_token: Optional[StrictStr] = Field(default=None, description="Base64 encoded Token string for authentication type Token", alias="auth-token")
    auth_type: Optional[StrictStr] = Field(default='user-pass', description="The Webhook authentication type [user-pass, bearer-token, certificate]", alias="auth-type")
    client_cert_data: Optional[StrictStr] = Field(default=None, description="Base64 encoded PEM certificate, relevant for certificate auth-type", alias="client-cert-data")
    description: Optional[StrictStr] = Field(default=None, description="Description of the object")
    event_types: Optional[List[StrictStr]] = Field(default=None, description="List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, next-automatic-rotation, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated, rate-limiting, usage-report, secret-sync]", alias="event-types")
    every: Optional[StrictStr] = Field(default=None, description="Rate of periodic runner repetition in hours")
    gateways_event_source_locations: List[StrictStr] = Field(description="Event sources", alias="gateways-event-source-locations")
    items_event_source_locations: Optional[List[StrictStr]] = Field(default=None, description="Items Event sources", alias="items-event-source-locations")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    key: Optional[StrictStr] = Field(default=None, description="The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used)")
    name: StrictStr = Field(description="EventForwarder name")
    password: Optional[StrictStr] = Field(default=None, description="Password for authentication relevant for user-pass auth-type")
    private_key_data: Optional[StrictStr] = Field(default=None, description="Base64 encoded PEM RSA Private Key, relevant for certificate auth-type", alias="private-key-data")
    runner_type: StrictStr = Field(alias="runner-type")
    server_certificates: Optional[StrictStr] = Field(default=None, description="Base64 encoded PEM certificate of the Webhook", alias="server-certificates")
    targets_event_source_locations: Optional[List[StrictStr]] = Field(default=None, description="Targets Event sources", alias="targets-event-source-locations")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    url: Optional[StrictStr] = Field(default=None, description="Webhook URL")
    username: Optional[StrictStr] = Field(default=None, description="Username for authentication relevant for user-pass auth-type")
    __properties: ClassVar[List[str]] = ["auth-methods-event-source-locations", "auth-token", "auth-type", "client-cert-data", "description", "event-types", "every", "gateways-event-source-locations", "items-event-source-locations", "json", "key", "name", "password", "private-key-data", "runner-type", "server-certificates", "targets-event-source-locations", "token", "uid-token", "url", "username"]

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
        """Create an instance of EventForwarderCreateWebhook from a JSON string"""
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
        """Create an instance of EventForwarderCreateWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth-methods-event-source-locations": obj.get("auth-methods-event-source-locations"),
            "auth-token": obj.get("auth-token"),
            "auth-type": obj.get("auth-type") if obj.get("auth-type") is not None else 'user-pass',
            "client-cert-data": obj.get("client-cert-data"),
            "description": obj.get("description"),
            "event-types": obj.get("event-types"),
            "every": obj.get("every"),
            "gateways-event-source-locations": obj.get("gateways-event-source-locations"),
            "items-event-source-locations": obj.get("items-event-source-locations"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "key": obj.get("key"),
            "name": obj.get("name"),
            "password": obj.get("password"),
            "private-key-data": obj.get("private-key-data"),
            "runner-type": obj.get("runner-type"),
            "server-certificates": obj.get("server-certificates"),
            "targets-event-source-locations": obj.get("targets-event-source-locations"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "url": obj.get("url"),
            "username": obj.get("username")
        })
        return _obj


