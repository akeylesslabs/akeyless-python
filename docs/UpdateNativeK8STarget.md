# UpdateNativeK8STarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_auth_type** | **str** | K8S auth type [token/certificate] | [optional] [default to 'token']
**k8s_client_certificate** | **str** | Content of the k8 client certificate (PEM format) in a Base64 format | [optional] 
**k8s_client_key** | **str** | Content of the k8 client private key (PEM format) in a Base64 format | [optional] 
**k8s_cluster_ca_cert** | **str** | K8S cluster CA certificate | [default to 'dummy_val']
**k8s_cluster_endpoint** | **str** | K8S cluster URL endpoint | [default to 'dummy_val']
**k8s_cluster_token** | **str** | K8S cluster Bearer token | [default to 'dummy_val']
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Deprecated | [optional] 
**use_gw_service_account** | **bool** | Use the GW&#39;s service account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


