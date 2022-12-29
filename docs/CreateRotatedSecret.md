# CreateRotatedSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_id** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**application_id** | **str** | ApplicationId (used in azure) | [optional] 
**authentication_credentials** | **str** |  | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**aws_region** | **str** | Region (used in aws) | [optional] [default to 'us-east-2']
**custom_payload** | **str** |  | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Metadata about the secret | [optional] 
**name** | **str** | Secret name | 
**rotated_password** | **str** |  | [optional] 
**rotated_username** | **str** |  | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_custom_cmd** | **str** |  | [optional] 
**rotator_type** | **str** | Rotator Type | 
**secure_access_allow_external_user** | **bool** | Secure Access Allow Providing External User (used in ssh) | [optional] [default to False]
**secure_access_aws_account_id** | **str** | Secure Access Account Id (used in aws) | [optional] 
**secure_access_aws_native_cli** | **bool** | Secure Access Aws Native Cli (used in aws) | [optional] 
**secure_access_bastion_issuer** | **str** | Secure Access Bastion Issuer | [optional] 
**secure_access_db_name** | **str** | Secure Access DB Name (used in data bases) | [optional] 
**secure_access_db_schema** | **str** | Secure Access Schema (used in mssql, postgresql) | [optional] 
**secure_access_enable** | **str** | Secure Access Enabled | [optional] 
**secure_access_host** | **list[str]** | Secure Access Host | [optional] 
**secure_access_rdp_domain** | **str** | Secure Access Domain (used in ssh) | [optional] 
**secure_access_rdp_user** | **str** | Secure Access Override User (used in ssh) | [optional] 
**secure_access_web** | **bool** | Secure Access Web | [optional] [default to False]
**secure_access_web_browsing** | **bool** | Secure Access Isolated (used in aws, azure) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Secure Access Web Proxy (used in aws, azure) | [optional] [default to False]
**ssh_password** | **str** | Deprecated: use RotatedPassword | [optional] 
**ssh_username** | **str** | Deprecated: use RotatedUser | [optional] 
**storage_account_key_name** | **str** | The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account) | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | LDAP User Attribute, Default value \&quot;cn\&quot; | [optional] 
**user_dn** | **str** | LDAP User Base DN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


