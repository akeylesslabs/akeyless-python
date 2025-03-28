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

class GatewayCreateProducerPing(BaseModel):
    """
    gatewayCreateProducerPing is a command that creates ping producer [Deprecated: Use dynamic-secret-create-ping command]
    """ # noqa: E501
    delete_protection: Optional[StrictStr] = Field(default=None, description="Protection from accidental deletion of this object [true/false]")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    name: StrictStr = Field(description="Dynamic secret name")
    ping_administrative_port: Optional[StrictStr] = Field(default='9999', description="Ping Federate administrative port", alias="ping-administrative-port")
    ping_atm_id: Optional[StrictStr] = Field(default=None, description="Set a specific Access Token Management (ATM) instance for the created OAuth Client by providing the ATM Id. If no explicit value is given, the default pingfederate server ATM will be set.", alias="ping-atm-id")
    ping_authorization_port: Optional[StrictStr] = Field(default='9031', description="Ping Federate authorization port", alias="ping-authorization-port")
    ping_cert_subject_dn: Optional[StrictStr] = Field(default=None, description="The subject DN of the client certificate. If no explicit value is given, the producer will create CA certificate and matched client certificate and return it as value. Used in conjunction with ping-issuer-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)", alias="ping-cert-subject-dn")
    ping_client_authentication_type: Optional[StrictStr] = Field(default='CLIENT_SECRET', description="OAuth Client Authentication Type [CLIENT_SECRET, PRIVATE_KEY_JWT, CLIENT_TLS_CERTIFICATE]", alias="ping-client-authentication-type")
    ping_enforce_replay_prevention: Optional[StrictStr] = Field(default='false', description="Determines whether PingFederate requires a unique signed JWT from the client for each action (relevant for PRIVATE_KEY_JWT authentication method) [true/false]", alias="ping-enforce-replay-prevention")
    ping_grant_types: Optional[List[StrictStr]] = Field(default=None, description="List of OAuth client grant types [IMPLICIT, AUTHORIZATION_CODE, CLIENT_CREDENTIALS, TOKEN_EXCHANGE, REFRESH_TOKEN, ASSERTION_GRANTS, PASSWORD, RESOURCE_OWNER_CREDENTIALS]. If no explicit value is given, AUTHORIZATION_CODE will be selected as default.", alias="ping-grant-types")
    ping_issuer_dn: Optional[StrictStr] = Field(default=None, description="Issuer DN of trusted CA certificate that imported into Ping Federate server. You may select \\\"Trust Any\\\" to trust all the existing issuers in Ping Federate server. Used in conjunction with ping-cert-subject-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)", alias="ping-issuer-dn")
    ping_jwks: Optional[StrictStr] = Field(default=None, description="Base64-encoded JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT (Sign Algo: RS256) and return it as value (relevant for PRIVATE_KEY_JWT authentication method)", alias="ping-jwks")
    ping_jwks_url: Optional[StrictStr] = Field(default=None, description="The URL of the JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT and return it as value (relevant for PRIVATE_KEY_JWT authentication method)", alias="ping-jwks-url")
    ping_password: Optional[StrictStr] = Field(default=None, description="Ping Federate privileged user password", alias="ping-password")
    ping_privileged_user: Optional[StrictStr] = Field(default=None, description="Ping Federate privileged user", alias="ping-privileged-user")
    ping_redirect_uris: Optional[List[StrictStr]] = Field(default=None, description="List of URIs to which the OAuth authorization server may redirect the resource owner's user agent after authorization is obtained. At least one redirection URI is required for the AUTHORIZATION_CODE and IMPLICIT grant types.", alias="ping-redirect-uris")
    ping_restricted_scopes: Optional[List[StrictStr]] = Field(default=None, description="Limit the OAuth client to specific scopes list", alias="ping-restricted-scopes")
    ping_signing_algo: Optional[StrictStr] = Field(default=None, description="The signing algorithm that the client must use to sign its request objects [RS256,RS384,RS512,ES256,ES384,ES512,PS256,PS384,PS512] If no explicit value is given, the client can use any of the supported signing algorithms (relevant for PRIVATE_KEY_JWT authentication method)", alias="ping-signing-algo")
    ping_url: Optional[StrictStr] = Field(default=None, description="Ping URL", alias="ping-url")
    producer_encryption_key_name: Optional[StrictStr] = Field(default=None, description="Dynamic producer encryption key", alias="producer-encryption-key-name")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Add tags attached to this object")
    target_name: Optional[StrictStr] = Field(default=None, description="Target name", alias="target-name")
    token: Optional[StrictStr] = Field(default=None, description="Authentication token (see `/auth` and `/configure`)")
    uid_token: Optional[StrictStr] = Field(default=None, description="The universal identity token, Required only for universal_identity authentication", alias="uid-token")
    user_ttl: Optional[StrictStr] = Field(default='60m', description="The time from dynamic secret creation to expiration.", alias="user-ttl")
    __properties: ClassVar[List[str]] = ["delete_protection", "json", "name", "ping-administrative-port", "ping-atm-id", "ping-authorization-port", "ping-cert-subject-dn", "ping-client-authentication-type", "ping-enforce-replay-prevention", "ping-grant-types", "ping-issuer-dn", "ping-jwks", "ping-jwks-url", "ping-password", "ping-privileged-user", "ping-redirect-uris", "ping-restricted-scopes", "ping-signing-algo", "ping-url", "producer-encryption-key-name", "tags", "target-name", "token", "uid-token", "user-ttl"]

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
        """Create an instance of GatewayCreateProducerPing from a JSON string"""
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
        """Create an instance of GatewayCreateProducerPing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delete_protection": obj.get("delete_protection"),
            "json": obj.get("json") if obj.get("json") is not None else False,
            "name": obj.get("name"),
            "ping-administrative-port": obj.get("ping-administrative-port") if obj.get("ping-administrative-port") is not None else '9999',
            "ping-atm-id": obj.get("ping-atm-id"),
            "ping-authorization-port": obj.get("ping-authorization-port") if obj.get("ping-authorization-port") is not None else '9031',
            "ping-cert-subject-dn": obj.get("ping-cert-subject-dn"),
            "ping-client-authentication-type": obj.get("ping-client-authentication-type") if obj.get("ping-client-authentication-type") is not None else 'CLIENT_SECRET',
            "ping-enforce-replay-prevention": obj.get("ping-enforce-replay-prevention") if obj.get("ping-enforce-replay-prevention") is not None else 'false',
            "ping-grant-types": obj.get("ping-grant-types"),
            "ping-issuer-dn": obj.get("ping-issuer-dn"),
            "ping-jwks": obj.get("ping-jwks"),
            "ping-jwks-url": obj.get("ping-jwks-url"),
            "ping-password": obj.get("ping-password"),
            "ping-privileged-user": obj.get("ping-privileged-user"),
            "ping-redirect-uris": obj.get("ping-redirect-uris"),
            "ping-restricted-scopes": obj.get("ping-restricted-scopes"),
            "ping-signing-algo": obj.get("ping-signing-algo"),
            "ping-url": obj.get("ping-url"),
            "producer-encryption-key-name": obj.get("producer-encryption-key-name"),
            "tags": obj.get("tags"),
            "target-name": obj.get("target-name"),
            "token": obj.get("token"),
            "uid-token": obj.get("uid-token"),
            "user-ttl": obj.get("user-ttl") if obj.get("user-ttl") is not None else '60m'
        })
        return _obj


