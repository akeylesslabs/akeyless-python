# CreateRotatedSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_id** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Metadata about the secret | [optional] 
**name** | **str** | Secret name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_type** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 
**ssh_username** | **str** |  | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


