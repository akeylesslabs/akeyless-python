# CreateUSC

CreateUSC is a command that creates a Universal Secrets Connector
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_kv_name** | **str** | Azure Key Vault name (Relevant only for Azure targets) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the Universal Secrets Connector | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_namespace** | **str** | K8s namespace (Relevant to Kubernetes targets) | [optional] 
**name** | **str** | Universal Secrets Connector name | 
**tags** | **list[str]** | List of the tags attached to this Universal Secrets Connector | [optional] 
**target_to_associate** | **str** | Target Universal Secrets Connector to connect | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


