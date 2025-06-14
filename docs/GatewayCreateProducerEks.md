# GatewayCreateProducerEks

gatewayCreateProducerEks is a command that creates eks producer [Deprecated: Use dynamic-secret-create-eks command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**eks_access_key_id** | **str** | Access Key ID | [optional] 
**eks_assume_role** | **str** | IAM assume role | [optional] 
**eks_cluster_ca_cert** | **str** | EKS cluster CA certificate | [optional] 
**eks_cluster_endpoint** | **str** | EKS cluster URL endpoint | [optional] 
**eks_cluster_name** | **str** | EKS cluster name | [optional] 
**eks_region** | **str** | Region | [optional] [default to 'us-east-2']
**eks_secret_access_key** | **str** | Secret Access Key | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_allow_port_forwading** | **bool** | Enable Port forwarding while using CLI access | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_cluster_endpoint** | **str** | The K8s cluster endpoint URL | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '15m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


