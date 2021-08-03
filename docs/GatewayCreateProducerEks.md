# GatewayCreateProducerEks

gatewayCreateProducerEks is a command that creates eks producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eks_access_key_id** | **str** | Access Key ID | [optional] 
**eks_assume_role** | **str** | IAM assume role | [optional] 
**eks_cluster_ca_cert** | **str** | EKS cluster CA certificate | [optional] 
**eks_cluster_endpoint** | **str** | EKS cluster URL endpoint | [optional] 
**eks_cluster_name** | **str** | EKS cluster name | [optional] 
**eks_region** | **str** | Region | [optional] [default to 'us-east-2']
**eks_secret_access_key** | **str** | Secret Access Key | [optional] 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_allow_port_forwading** | **bool** |  | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_cluster_endpoint** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


