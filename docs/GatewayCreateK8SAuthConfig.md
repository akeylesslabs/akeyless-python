# GatewayCreateK8SAuthConfig

gatewayCreateK8SAuth is a command that creates k8s auth config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | The access ID of the Kubernetes auth method | 
**cluster_api_type** | **str** | Cluster access type. options: [native_k8s, rancher] | [optional] [default to 'native_k8s']
**config_encryption_key_name** | **str** | Config encryption key | [optional] 
**disable_issuer_validation** | **str** | Disable issuer validation | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**k8s_ca_cert** | **str** | The CA Certificate (base64 encoded) to use to call into the kubernetes API server | [optional] 
**k8s_host** | **str** | The URL of the kubernetes API server | 
**k8s_issuer** | **str** | The Kubernetes JWT issuer name. If not set, kubernetes/serviceaccount will use as an issuer. | [optional] 
**name** | **str** | K8S Auth config name | 
**rancher_api_key** | **str** | The api key used to access the TokenReview API to validate other JWTs (relevant for \&quot;rancher\&quot; only) | [optional] 
**rancher_cluster_id** | **str** | The cluster id as define in rancher (relevant for \&quot;rancher\&quot; only) | [optional] 
**signing_key** | **str** | The private key (base64 encoded) associated with the public key defined in the Kubernetes auth | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**token_exp** | **int** | Time in seconds of expiration of the Akeyless Kube Auth Method token | [optional] [default to 300]
**token_reviewer_jwt** | **str** | A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs (relevant for \&quot;native_k8s\&quot; only). If not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API. | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


