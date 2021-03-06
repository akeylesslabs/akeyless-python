# GatewayCreateProducerNativeK8S

gatewayCreateProducerNativeK8S is a command that creates k8s producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_cluster_ca_cert** | **str** | K8S cluster CA certificate | 
**k8s_cluster_endpoint** | **str** | K8S cluster URL endpoint | 
**k8s_cluster_token** | **str** | K8S cluster Bearer token | 
**k8s_namespace** | **str** | K8S namespace | [optional] 
**k8s_service_account** | **str** | K8S service account | 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


