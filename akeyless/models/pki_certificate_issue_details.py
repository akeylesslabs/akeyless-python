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
from akeyless.models.certificate_expiration_event import CertificateExpirationEvent
from typing import Optional, Set
from typing_extensions import Self

class PKICertificateIssueDetails(BaseModel):
    """
    PKICertificateIssueDetails
    """ # noqa: E501
    acme_enabled: Optional[StrictBool] = None
    allow_any_name: Optional[StrictBool] = None
    allow_copy_ext_from_csr: Optional[StrictBool] = None
    allow_subdomains: Optional[StrictBool] = None
    allowed_domains_list: Optional[List[StrictStr]] = None
    allowed_extra_extensions: Optional[Dict[str, List[StrictStr]]] = None
    allowed_ip_sans: Optional[List[StrictStr]] = None
    allowed_uri_sans: Optional[List[StrictStr]] = None
    auto_renew_certificate: Optional[StrictBool] = None
    basic_constraints_valid_for_non_ca: Optional[StrictBool] = None
    certificate_authority_mode: Optional[StrictStr] = None
    client_flag: Optional[StrictBool] = None
    code_signing_flag: Optional[StrictBool] = None
    country: Optional[List[StrictStr]] = None
    create_private_crl: Optional[StrictBool] = None
    create_public_crl: Optional[StrictBool] = None
    destination_path: Optional[StrictStr] = Field(default=None, description="DestinationPath is the destination to save generated certificates")
    enforce_hostnames: Optional[StrictBool] = None
    expiration_events: Optional[List[CertificateExpirationEvent]] = Field(default=None, description="ExpirationNotification holds a list of expiration notices that should be sent in case a certificate is about to expire, this value is being propagated to the Certificate resources that are created")
    gw_cluster_id: Optional[StrictInt] = None
    gw_cluster_url: Optional[StrictStr] = Field(default=None, description="GWClusterURL is required when CAMode is \"public\" and it defines the cluster URL the PKI should be issued from. The GW cluster must have permissions to read associated target's details")
    is_ca: Optional[StrictBool] = None
    key_bits: Optional[StrictInt] = None
    key_type: Optional[StrictStr] = None
    key_usage_list: Optional[List[StrictStr]] = None
    locality: Optional[List[StrictStr]] = None
    max_path_len: Optional[StrictInt] = None
    non_critical_key_usage: Optional[StrictBool] = None
    not_before_duration: Optional[StrictInt] = Field(default=None, description="A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.")
    organization_list: Optional[List[StrictStr]] = None
    organization_unit_list: Optional[List[StrictStr]] = None
    pki_issuer_type: Optional[StrictStr] = None
    postal_code: Optional[List[StrictStr]] = None
    protect_generated_certificates: Optional[StrictBool] = Field(default=None, description="ProtectGeneratedCertificates dictates whether the created certificates should be protected from deletion")
    province: Optional[List[StrictStr]] = None
    renew_before_expiration_in_days: Optional[StrictInt] = None
    require_cn: Optional[StrictBool] = None
    server_flag: Optional[StrictBool] = None
    street_address: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["acme_enabled", "allow_any_name", "allow_copy_ext_from_csr", "allow_subdomains", "allowed_domains_list", "allowed_extra_extensions", "allowed_ip_sans", "allowed_uri_sans", "auto_renew_certificate", "basic_constraints_valid_for_non_ca", "certificate_authority_mode", "client_flag", "code_signing_flag", "country", "create_private_crl", "create_public_crl", "destination_path", "enforce_hostnames", "expiration_events", "gw_cluster_id", "gw_cluster_url", "is_ca", "key_bits", "key_type", "key_usage_list", "locality", "max_path_len", "non_critical_key_usage", "not_before_duration", "organization_list", "organization_unit_list", "pki_issuer_type", "postal_code", "protect_generated_certificates", "province", "renew_before_expiration_in_days", "require_cn", "server_flag", "street_address"]

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
        """Create an instance of PKICertificateIssueDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in expiration_events (list)
        _items = []
        if self.expiration_events:
            for _item_expiration_events in self.expiration_events:
                if _item_expiration_events:
                    _items.append(_item_expiration_events.to_dict())
            _dict['expiration_events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PKICertificateIssueDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acme_enabled": obj.get("acme_enabled"),
            "allow_any_name": obj.get("allow_any_name"),
            "allow_copy_ext_from_csr": obj.get("allow_copy_ext_from_csr"),
            "allow_subdomains": obj.get("allow_subdomains"),
            "allowed_domains_list": obj.get("allowed_domains_list"),
            "allowed_extra_extensions": obj.get("allowed_extra_extensions"),
            "allowed_ip_sans": obj.get("allowed_ip_sans"),
            "allowed_uri_sans": obj.get("allowed_uri_sans"),
            "auto_renew_certificate": obj.get("auto_renew_certificate"),
            "basic_constraints_valid_for_non_ca": obj.get("basic_constraints_valid_for_non_ca"),
            "certificate_authority_mode": obj.get("certificate_authority_mode"),
            "client_flag": obj.get("client_flag"),
            "code_signing_flag": obj.get("code_signing_flag"),
            "country": obj.get("country"),
            "create_private_crl": obj.get("create_private_crl"),
            "create_public_crl": obj.get("create_public_crl"),
            "destination_path": obj.get("destination_path"),
            "enforce_hostnames": obj.get("enforce_hostnames"),
            "expiration_events": [CertificateExpirationEvent.from_dict(_item) for _item in obj["expiration_events"]] if obj.get("expiration_events") is not None else None,
            "gw_cluster_id": obj.get("gw_cluster_id"),
            "gw_cluster_url": obj.get("gw_cluster_url"),
            "is_ca": obj.get("is_ca"),
            "key_bits": obj.get("key_bits"),
            "key_type": obj.get("key_type"),
            "key_usage_list": obj.get("key_usage_list"),
            "locality": obj.get("locality"),
            "max_path_len": obj.get("max_path_len"),
            "non_critical_key_usage": obj.get("non_critical_key_usage"),
            "not_before_duration": obj.get("not_before_duration"),
            "organization_list": obj.get("organization_list"),
            "organization_unit_list": obj.get("organization_unit_list"),
            "pki_issuer_type": obj.get("pki_issuer_type"),
            "postal_code": obj.get("postal_code"),
            "protect_generated_certificates": obj.get("protect_generated_certificates"),
            "province": obj.get("province"),
            "renew_before_expiration_in_days": obj.get("renew_before_expiration_in_days"),
            "require_cn": obj.get("require_cn"),
            "server_flag": obj.get("server_flag"),
            "street_address": obj.get("street_address")
        })
        return _obj


