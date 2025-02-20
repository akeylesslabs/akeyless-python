# GatewayGetK8SAuthConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**am_token_expiration** | **int** | AuthMethodTokenExpiration is time in seconds of expiration of the Akeyless Kube Auth Method token | [optional] 
**auth_method_access_id** | **str** | AuthMethodAccessId of the Kubernetes auth method | [optional] 
**auth_method_prv_key_pem** | **str** | AuthMethodSigningKey is the private key (in base64 of the PEM format) associated with the public key defined in the Kubernetes auth method, that used to sign the internal token for the Akeyless Kubernetes Auth Method | [optional] 
**cluster_api_type** | **str** | ClusterApiType defines types of API access to cluster | [optional] 
**disable_iss_validation** | **bool** | DisableISSValidation is optional parameter to disable ISS validation | [optional] 
**id** | **str** |  | [optional] 
**k8s_auth_type** | **str** |  | [optional] 
**k8s_ca_cert** | **str** | K8SCACert is the CA Cert to use to call into the kubernetes API | [optional] 
**k8s_client_cert_data** | **str** | K8sClientCertData is the client certificate for k8s client certificate authentication | [optional] 
**k8s_client_key_data** | **str** | K8sClientKeyData is the client key for k8s client certificate authentication | [optional] 
**k8s_host** | **str** | K8SHost is the url string for the kubernetes API | [optional] 
**k8s_issuer** | **str** | K8SIssuer is the claim that specifies who issued the Kubernetes token | [optional] 
**k8s_pub_keys_pem** | **List[str]** | K8SPublicKeysPEM is the list of public key in PEM format | [optional] 
**k8s_token_reviewer_jwt** | **str** | K8STokenReviewerJWT is the bearer for clusterApiTypeK8s, used during TokenReview API call | [optional] 
**name** | **str** |  | [optional] 
**protection_key** | **str** |  | [optional] 
**rancher_api_key** | **str** | RancherApiKey the bear token for clusterApiTypeRancher | [optional] 
**rancher_cluster_id** | **str** | RancherClusterId cluster id as define in rancher (in case of clusterApiTypeRancher) | [optional] 
**use_local_ca_jwt** | **bool** | UseLocalCAJwt is an optional parameter to set defaulting to using the local service account when running in a Kubernetes pod | [optional] 

## Example

```python
from akeyless.models.gateway_get_k8_s_auth_config_output import GatewayGetK8SAuthConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetK8SAuthConfigOutput from a JSON string
gateway_get_k8_s_auth_config_output_instance = GatewayGetK8SAuthConfigOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayGetK8SAuthConfigOutput.to_json())

# convert the object into a dict
gateway_get_k8_s_auth_config_output_dict = gateway_get_k8_s_auth_config_output_instance.to_dict()
# create an instance of GatewayGetK8SAuthConfigOutput from a dict
gateway_get_k8_s_auth_config_output_from_dict = GatewayGetK8SAuthConfigOutput.from_dict(gateway_get_k8_s_auth_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


