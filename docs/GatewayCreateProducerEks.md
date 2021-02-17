# GatewayCreateProducerEks

gatewayCreateProducerEks is a command that creates eks producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eks_access_key_id** | **str** | Access Key ID | 
**eks_assume_role** | **str** | IAM assume role | [optional] 
**eks_cluster_cert** | **str** | EKS cluster CA certificate | 
**eks_cluster_endpoint** | **str** | EKS cluster URL endpoint | 
**eks_cluster_name** | **str** | EKS cluster name | 
**eks_region** | **str** | Region | [optional] [default to 'us-east-2']
**eks_secret_access_key** | **str** | Secret Access Key | 
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


