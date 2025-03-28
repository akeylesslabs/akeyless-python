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

class K8SAuth(BaseModel):
    """
    K8SAuth
    """ # noqa: E501
    am_token_expiration: Optional[StrictInt] = Field(default=None, description="AuthMethodTokenExpiration is time in seconds of expiration of the Akeyless Kube Auth Method token")
    auth_method_access_id: Optional[StrictStr] = Field(default=None, description="AuthMethodAccessId of the Kubernetes auth method")
    auth_method_prv_key_pem: Optional[StrictStr] = Field(default=None, description="AuthMethodSigningKey is the private key (in base64 of the PEM format) associated with the public key defined in the Kubernetes auth method, that used to sign the internal token for the Akeyless Kubernetes Auth Method")
    cluster_api_type: Optional[StrictStr] = Field(default=None, description="ClusterApiType defines types of API access to cluster")
    disable_iss_validation: Optional[StrictBool] = Field(default=None, description="DisableISSValidation is optional parameter to disable ISS validation")
    id: Optional[StrictStr] = None
    k8s_auth_type: Optional[StrictStr] = None
    k8s_ca_cert: Optional[StrictStr] = Field(default=None, description="K8SCACert is the CA Cert to use to call into the kubernetes API")
    k8s_client_cert_data: Optional[StrictStr] = Field(default=None, description="K8sClientCertData is the client certificate for k8s client certificate authentication")
    k8s_client_key_data: Optional[StrictStr] = Field(default=None, description="K8sClientKeyData is the client key for k8s client certificate authentication")
    k8s_host: Optional[StrictStr] = Field(default=None, description="K8SHost is the url string for the kubernetes API")
    k8s_issuer: Optional[StrictStr] = Field(default=None, description="K8SIssuer is the claim that specifies who issued the Kubernetes token")
    k8s_pub_keys_pem: Optional[List[StrictStr]] = Field(default=None, description="K8SPublicKeysPEM is the list of public key in PEM format")
    k8s_token_reviewer_jwt: Optional[StrictStr] = Field(default=None, description="K8STokenReviewerJWT is the bearer for clusterApiTypeK8s, used during TokenReview API call")
    name: Optional[StrictStr] = None
    rancher_api_key: Optional[StrictStr] = Field(default=None, description="RancherApiKey the bear token for clusterApiTypeRancher")
    rancher_cluster_id: Optional[StrictStr] = Field(default=None, description="RancherClusterId cluster id as define in rancher (in case of clusterApiTypeRancher)")
    use_local_ca_jwt: Optional[StrictBool] = Field(default=None, description="UseLocalCAJwt is an optional parameter to set defaulting to using the local service account when running in a Kubernetes pod")
    __properties: ClassVar[List[str]] = ["am_token_expiration", "auth_method_access_id", "auth_method_prv_key_pem", "cluster_api_type", "disable_iss_validation", "id", "k8s_auth_type", "k8s_ca_cert", "k8s_client_cert_data", "k8s_client_key_data", "k8s_host", "k8s_issuer", "k8s_pub_keys_pem", "k8s_token_reviewer_jwt", "name", "rancher_api_key", "rancher_cluster_id", "use_local_ca_jwt"]

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
        """Create an instance of K8SAuth from a JSON string"""
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
        """Create an instance of K8SAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "am_token_expiration": obj.get("am_token_expiration"),
            "auth_method_access_id": obj.get("auth_method_access_id"),
            "auth_method_prv_key_pem": obj.get("auth_method_prv_key_pem"),
            "cluster_api_type": obj.get("cluster_api_type"),
            "disable_iss_validation": obj.get("disable_iss_validation"),
            "id": obj.get("id"),
            "k8s_auth_type": obj.get("k8s_auth_type"),
            "k8s_ca_cert": obj.get("k8s_ca_cert"),
            "k8s_client_cert_data": obj.get("k8s_client_cert_data"),
            "k8s_client_key_data": obj.get("k8s_client_key_data"),
            "k8s_host": obj.get("k8s_host"),
            "k8s_issuer": obj.get("k8s_issuer"),
            "k8s_pub_keys_pem": obj.get("k8s_pub_keys_pem"),
            "k8s_token_reviewer_jwt": obj.get("k8s_token_reviewer_jwt"),
            "name": obj.get("name"),
            "rancher_api_key": obj.get("rancher_api_key"),
            "rancher_cluster_id": obj.get("rancher_cluster_id"),
            "use_local_ca_jwt": obj.get("use_local_ca_jwt")
        })
        return _obj


