# AssocTargetItem

assocTargetItem is a command that creates an association between target and item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json** | **bool** | Set output format to JSON | [optional] 
**key_operations** | **list[str]** | A list of allowed operations for the key (required for azure targets) | [optional] 
**keyring_name** | **str** | Keyring name of the GCP KMS (required for gcp targets) | [optional] 
**kms_algorithm** | **str** | Algorithm of the key in GCP KMS (required for gcp targets) | [optional] 
**location_id** | **str** | Location id of the GCP KMS (required for gcp targets) | [optional] 
**name** | **str** | The item to associate | 
**project_id** | **str** | Project id of the GCP KMS (required for gcp targets) | [optional] 
**purpose** | **str** | Purpose of the key in GCP KMS (required for gcp targets) | [optional] 
**target_name** | **str** | The target to associate | 
**tenant_secret_type** | **str** | The tenant secret type [Data/SearchIndex/Analytics] (required for salesforce targets) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**vault_name** | **str** | Name of the vault used (required for azure targets) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


