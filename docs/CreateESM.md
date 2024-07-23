# CreateESM

CreateESM is a command that creates an External Secrets Manager. [Deprecated: Use command create-usc]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_kv_name** | **str** | Azure Key Vault name (Relevant only for Azure targets) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the External Secrets Manager | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_namespace** | **str** | K8s namespace (Relevant to Kubernetes targets) | [optional] 
**name** | **str** | External Secrets Manager name | 
**tags** | **list[str]** | List of the tags attached to this External Secrets Manager | [optional] 
**target_to_associate** | **str** | Target External Secrets Manager to connect | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


