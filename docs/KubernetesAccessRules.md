# KubernetesAccessRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**audience** | **str** | Audience is an optional Kubernetes jwt claim to verify | [optional] 
**bound_namespaces** | **list[str]** | A list of namespaces that the authentication is restricted to. | [optional] 
**bound_pod_names** | **list[str]** | A list of pods names that the authentication is restricted to. | [optional] 
**bound_service_account_names** | **list[str]** | A list of service account names that the authentication is restricted to. | [optional] 
**gen_key_pair** | **str** | Generate public/private key (the private key is required for the K8S Auth Config in the Akeyless Gateway) | [optional] 
**pub_key** | **str** | The public key value of the Kubernetes auth method configuration in the Akeyless Gateway. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


