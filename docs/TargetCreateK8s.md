# TargetCreateK8s

targetCreateK8s is a command that creates a new k8s target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_auth_type** | **str** | K8S auth type [token/certificate] | [optional] [default to 'token']
**k8s_client_certificate** | **str** | Content of the k8 client certificate (PEM format) in a Base64 format | [optional] 
**k8s_client_key** | **str** | Content of the k8 client private key (PEM format) in a Base64 format | [optional] 
**k8s_cluster_ca_cert** | **str** | K8S cluster CA certificate | [optional] 
**k8s_cluster_endpoint** | **str** | K8S cluster URL endpoint | [optional] 
**k8s_cluster_name** | **str** | K8S cluster name | [optional] 
**k8s_cluster_token** | **str** | K8S cluster Bearer token | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_service_account** | **bool** | Use the GW&#39;s service account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


