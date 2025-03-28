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

class Configure(BaseModel):
    """
    Configure
    """ # noqa: E501
    access_id: Optional[StrictStr] = Field(default=None, description="Access ID", alias="access-id")
    access_key: Optional[StrictStr] = Field(default=None, description="Access Key", alias="access-key")
    access_type: Optional[StrictStr] = Field(default='access_key', description="Access Type (access_key/password/azure_ad/saml/oidc/aws_iam/gcp/k8s/cert)", alias="access-type")
    account_id: Optional[StrictStr] = Field(default=None, description="Account id (relevant only for access-type=password where the email address is associated with more than one account)", alias="account-id")
    admin_email: Optional[StrictStr] = Field(default=None, description="Email (relevant only for access-type=password)", alias="admin-email")
    admin_password: Optional[StrictStr] = Field(default=None, description="Password (relevant only for access-type=password)", alias="admin-password")
    azure_ad_object_id: Optional[StrictStr] = Field(default=None, description="Azure Active Directory ObjectId (relevant only for access-type=azure_ad)", alias="azure-ad-object-id")
    cert_data: Optional[StrictStr] = Field(default=None, description="Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type=cert in Curl Context)", alias="cert-data")
    cert_issuer_name: Optional[StrictStr] = Field(default=None, description="Certificate Issuer Name", alias="cert-issuer-name")
    cert_username: Optional[StrictStr] = Field(default=None, description="The username to sign in the SSH certificate (use a comma-separated list for more than one username)", alias="cert-username")
    default_location_prefix: Optional[StrictStr] = Field(default=None, description="Default path prefix for name of items, targets and auth methods", alias="default-location-prefix")
    disable_pafxfast: Optional[StrictStr] = Field(default=None, description="Disable the FAST negotiation in the Kerberos authentication method", alias="disable-pafxfast")
    gateway_spn: Optional[StrictStr] = Field(default=None, description="The service principal name of the gateway as registered in LDAP (i.e., HTTP/gateway)", alias="gateway-spn")
    gcp_audience: Optional[StrictStr] = Field(default='akeyless.io', description="GCP JWT audience", alias="gcp-audience")
    var_json: Optional[StrictBool] = Field(default=False, description="Set output format to JSON", alias="json")
    k8s_auth_config_name: Optional[StrictStr] = Field(default=None, description="The K8S Auth config name (relevant only for access-type=k8s)", alias="k8s-auth-config-name")
    kerberos_token: Optional[StrictStr] = Field(default=None, description="KerberosToken represents a Kerberos token generated for the gateway SPN (Service Principal Name).", alias="kerberos-token")
    kerberos_username: Optional[StrictStr] = Field(default=None, description="TThe username for the entry within the keytab to authenticate via Kerberos", alias="kerberos-username")
    key_data: Optional[StrictStr] = Field(default=None, description="Private key data encoded in base64. Used if file was not provided.(relevant only for access-type=cert in Curl Context)", alias="key-data")
    keytab_data: Optional[StrictStr] = Field(default=None, description="Base64-encoded content of a valid keytab file, containing the service account's entry.", alias="keytab-data")
    krb5_conf_data: Optional[StrictStr] = Field(default=None, description="Base64-encoded content of a valid krb5.conf file, specifying the settings and parameters required for Kerberos authentication.", alias="krb5-conf-data")
    legacy_signing_alg_name: Optional[StrictBool] = Field(default=None, description="Set this option to output legacy ('ssh-rsa-cert-v01@openssh.com') signing algorithm name in the certificate.", alias="legacy-signing-alg-name")
    oci_auth_type: Optional[StrictStr] = Field(default='apikey', description="The type of the OCI configuration to use [instance/apikey/resource] (relevant only for access-type=oci)", alias="oci-auth-type")
    oci_group_ocid: Optional[List[StrictStr]] = Field(default=None, description="A list of Oracle Cloud IDs groups (relevant only for access-type=oci)", alias="oci-group-ocid")
    __properties: ClassVar[List[str]] = ["access-id", "access-key", "access-type", "account-id", "admin-email", "admin-password", "azure-ad-object-id", "cert-data", "cert-issuer-name", "cert-username", "default-location-prefix", "disable-pafxfast", "gateway-spn", "gcp-audience", "json", "k8s-auth-config-name", "kerberos-token", "kerberos-username", "key-data", "keytab-data", "krb5-conf-data", "legacy-signing-alg-name", "oci-auth-type", "oci-group-ocid"]

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
        """Create an instance of Configure from a JSON string"""
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
        """Create an instance of Configure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access-id": obj.get("access-id"),
            "access-key": obj.get("access-key"),
            "access-type": obj.get("access-type") if obj.get("access-type") is not None else 'access_key',
            "account-id": obj.get("account-id"),
            "admin-email": obj.get("admin-email"),
            "admin-password": obj.get("admin-password"),
            "azure-ad-object-id": obj.get("azure-ad-object-id"),
            "cert-data": obj.get("cert-data"),
            "cert-issuer-name": obj.get("cert-issuer-name"),
            "cert-username": obj.get("cert-username"),
            "default-location-prefix": obj.get("default-location-prefix"),
            "disable-pafxfast": obj.get("disable-pafxfast"),
            "gateway-spn": obj.get("gateway-spn"),
            "gcp-audience": obj.get("gcp-audience") if obj.get("gcp-audience") is not None else 'akeyless.io',
            "json": obj.get("json") if obj.get("json") is not None else False,
            "k8s-auth-config-name": obj.get("k8s-auth-config-name"),
            "kerberos-token": obj.get("kerberos-token"),
            "kerberos-username": obj.get("kerberos-username"),
            "key-data": obj.get("key-data"),
            "keytab-data": obj.get("keytab-data"),
            "krb5-conf-data": obj.get("krb5-conf-data"),
            "legacy-signing-alg-name": obj.get("legacy-signing-alg-name"),
            "oci-auth-type": obj.get("oci-auth-type") if obj.get("oci-auth-type") is not None else 'apikey',
            "oci-group-ocid": obj.get("oci-group-ocid")
        })
        return _obj


