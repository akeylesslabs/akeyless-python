# GatewayPartialUpdateK8SAuthConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_default_identity_bool** | **bool** |  | [optional] 
**access_id** | **str** | The access ID of the Kubernetes auth method | [optional] 
**disable_issuer_validation** | **str** | Disable issuer validation [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_auth_type** | **str** | K8S auth type [token/certificate]. (relevant for \&quot;native_k8s\&quot; only) | [optional] [default to 'token']
**k8s_ca_cert** | **str** | The CA Certificate (base64 encoded) to use to call into the kubernetes API server | [optional] 
**k8s_client_certificate** | **str** | Content of the k8 client certificate (PEM format) in a Base64 format (relevant for \&quot;native_k8s\&quot; only) | [optional] 
**k8s_client_key** | **str** | Content of the k8 client private key (PEM format) in a Base64 format (relevant for \&quot;native_k8s\&quot; only) | [optional] 
**k8s_host** | **str** | The URL of the kubernetes API server | [optional] 
**k8s_issuer** | **str** | The Kubernetes JWT issuer name. K8SIssuer is the claim that specifies who issued the Kubernetes token | [optional] 
**name** | **str** | K8S Auth config name | [optional] 
**new_name** | **str** | K8S Auth config new name | [optional] 
**rancher_api_key** | **str** | The api key used to access the TokenReview API to validate other JWTs (relevant for \&quot;rancher\&quot; only) | [optional] 
**rancher_cluster_id** | **str** | The cluster id as define in rancher (relevant for \&quot;rancher\&quot; only) | [optional] 
**signing_key** | **str** | The private key (base64 encoded) associated with the public key defined in the Kubernetes auth | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_exp** | **int** | Time in seconds of expiration of the Akeyless Kube Auth Method token | [optional] 
**token_reviewer_jwt** | **str** | A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs (relevant for \&quot;native_k8s\&quot; only). If not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API. | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_service_account** | **str** | Use the GW&#39;s service account | [optional] 

## Example

```python
from akeyless.models.gateway_partial_update_k8_s_auth_config import GatewayPartialUpdateK8SAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPartialUpdateK8SAuthConfig from a JSON string
gateway_partial_update_k8_s_auth_config_instance = GatewayPartialUpdateK8SAuthConfig.from_json(json)
# print the JSON string representation of the object
print(GatewayPartialUpdateK8SAuthConfig.to_json())

# convert the object into a dict
gateway_partial_update_k8_s_auth_config_dict = gateway_partial_update_k8_s_auth_config_instance.to_dict()
# create an instance of GatewayPartialUpdateK8SAuthConfig from a dict
gateway_partial_update_k8_s_auth_config_from_dict = GatewayPartialUpdateK8SAuthConfig.from_dict(gateway_partial_update_k8_s_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


