# GatewayUpdateK8SAuthConfig

gatewayUpdateK8SAuth is a command that updates k8s auth config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access ID of the Kubernetes auth method | 
**config_encryption_key_name** | **str** | Config encryption key | [optional] 
**k8s_ca_cert** | **str** | The CA Cert (in PEM format) to use to call into the kubernetes API server | [optional] 
**k8s_host** | **str** | The URL of the kubernetes API server | 
**k8s_issuer** | **str** | The Kubernetes JWT issuer name. If not set, kubernetes/serviceaccount will use as an issuer. | [optional] 
**name** | **str** | K8S Auth config name | 
**new_name** | **str** | K8S Auth config new name | 
**signing_key** | **str** | The private key (in base64 encoded of the PEM format) associated with the public key defined in the Kubernetes auth | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_exp** | **int** | Time in seconds of expiration of the Akeyless Kube Auth Method token | [optional] 
**token_reviewer_jwt** | **str** | A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs. If not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API. | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


