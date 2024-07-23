# RotatedSecretCreateAzure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_id** | **str** | API ID to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**api_key** | **str** | API key to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**application_id** | **str** | Id of the azure app that hold the serect to be rotated (relevant only for rotator-type&#x3D;api-key &amp; authentication-credentials&#x3D;use-target-creds) | [optional] 
**authentication_credentials** | **str** | The credentials to connect with use-user-creds/use-target-creds | [optional] [default to 'use-user-creds']
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false] | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Rotated secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rotate_after_disconnect** | **str** | Rotate the value of the secret after SRA session ends [true/false] | [optional] [default to 'false']
**rotation_hour** | **int** | The Hour of the rotation in UTC | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_type** | **str** | The rotator type. options: [target/password/api-key/azure-storage-account] | 
**secure_access_disable_concurrent_connections** | **bool** | Enable this flag to prevent simultaneous use of the same secret | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless Web Access Bastion | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless Web Access Bastion | [optional] [default to False]
**storage_account_key_name** | **str** | The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account) | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | The user principal name to rotate his password (relevant only for rotator-type&#x3D;password) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


