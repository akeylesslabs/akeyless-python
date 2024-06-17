# CreateRotatedSecret

createRotatedSecret is a command that creates a rotated secret [Deprecated: Use rotated-secret-create commands]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**api_id** | **str** | API ID to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**api_key** | **str** | API key to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**application_id** | **str** | ApplicationId (used in azure) | [optional] 
**authentication_credentials** | **str** | The credentials to connect with use-user-creds/use-target-creds | [optional] [default to 'use-user-creds']
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false] | [optional] 
**aws_region** | **str** | Aws Region (relevant only for aws) | [optional] [default to 'us-east-2']
**custom_payload** | **str** | Secret payload to be sent with rotation request (relevant only for rotator-type&#x3D;custom) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_service_account_email** | **str** | The email of the gcp service account to rotate | [optional] 
**gcp_service_account_key_id** | **str** | The key id of the gcp service account to rotate | [optional] 
**grace_rotation** | **str** | Create a new access key without deleting the old key from AWS for backup (relevant only for AWS) [true/false] | [optional] 
**host_provider** | **str** | Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rotate_after_disconnect** | **str** | Rotate the value of the secret after SRA session ends [true/false] | [optional] [default to 'false']
**rotated_password** | **str** | rotated-username password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotated_username** | **str** | username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it&#39;s own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotation_hour** | **int** | The Hour of the rotation in UTC. Default rotation-hour is 14:00 | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_custom_cmd** | **str** | Custom rotation command (relevant only for ssh target) | [optional] 
**rotator_type** | **str** | Rotator Type | 
**same_password** | **str** | Rotate same password for each host from the Linked Target (relevant only for Linked Target) | [optional] 
**secure_access_allow_external_user** | **bool** | Allow providing external user for a domain users (relevant only for rdp) | [optional] [default to False]
**secure_access_aws_account_id** | **str** | The AWS account id (relevant only for aws) | [optional] 
**secure_access_aws_native_cli** | **bool** | The AWS native cli | [optional] 
**secure_access_bastion_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Bastion | [optional] 
**secure_access_db_name** | **str** | The DB name (relevant only for DB Dynamic-Secret) | [optional] 
**secure_access_db_schema** | **str** | The db schema (relevant only for mssql or postgresql) | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **list[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rdp_domain** | **str** | Required when the Dynamic Secret is used for a domain user (relevant only for RDP Dynamic-Secret) | [optional] 
**secure_access_rdp_user** | **str** | Override the RDP Domain username (relevant only for rdp) | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless Web Access Bastion (relevant only for aws or azure) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless Web Access Bastion (relevant only for aws or azure) | [optional] [default to False]
**ssh_password** | **str** | Deprecated: use RotatedPassword | [optional] 
**ssh_username** | **str** | Deprecated: use RotatedUser | [optional] 
**storage_account_key_name** | **str** | The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account) | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target** | **list[str]** | A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times | [optional] 
**target_name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_attribute** | **str** | LDAP User Attribute, Default value \&quot;cn\&quot; | [optional] [default to 'cn']
**user_dn** | **str** | LDAP User Base DN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


