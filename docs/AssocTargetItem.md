# AssocTargetItem

assocTargetItem is a command that creates an association between target and item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_path** | **str** | A path on the target to store the certificate pem file (relevant only for certificate provisioning) | [optional] 
**chain_path** | **str** | A path on the target to store the full chain pem file (relevant only for certificate provisioning) | [optional] 
**disable_previous_key_version** | **bool** | Automatically disable previous key version (required for azure targets) | [optional] [default to False]
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_operations** | **list[str]** | A list of allowed operations for the key (required for azure targets) | [optional] 
**keyring_name** | **str** | Keyring name of the GCP KMS (required for gcp targets) | [optional] 
**kms_algorithm** | **str** | Algorithm of the key in GCP KMS (required for gcp targets) | [optional] 
**location_id** | **str** | Location id of the GCP KMS (required for gcp targets) | [optional] 
**multi_region** | **str** | Set to &#39;true&#39; to create a multi-region managed key. (Relevant only for Classic Key AWS targets) | [optional] [default to 'false']
**name** | **str** | The item to associate | 
**post_provision_command** | **str** | A custom command to run on the remote target after successful provisioning (relevant only for certificate provisioning) | [optional] 
**private_key_path** | **str** | A path on the target to store the private key (relevant only for certificate provisioning) | [optional] 
**project_id** | **str** | Project id of the GCP KMS (required for gcp targets) | [optional] 
**protection_level** | **str** | Protection level of the key [software/hardware] (relevant for gcp targets) | [optional] [default to 'software']
**purpose** | **str** | Purpose of the key in GCP KMS (required for gcp targets) | [optional] 
**regions** | **list[str]** | The list of regions to create a copy of the key in (relevant for aws targets) | [optional] 
**sra_association** | **bool** | Is the target to associate is for sra, relevant only for linked target association for ldap rotated secret | [optional] [default to False]
**target_name** | **str** | The target to associate | 
**tenant_secret_type** | **str** | The tenant secret type [Data/SearchIndex/Analytics] (required for salesforce targets) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**vault_name** | **str** | Name of the vault used (required for azure targets) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


