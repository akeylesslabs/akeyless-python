# UpdateRotatedSecret

updateRotatedSecret is a command that updates rotated secret. [Deprecated: Use gateway-update-item command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**api_id** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Secret name | 
**new_metadata** | **str** | New item metadata | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**new_version** | **bool** | Whether to create a new version of not | [optional] [default to False]
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotated_password** | **str** |  | [optional] 
**rotated_username** | **str** |  | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_custom_cmd** | **str** |  | [optional] 
**ssh_password** | **str** | Deprecated: use RotatedPassword | [optional] 
**ssh_username** | **str** | Deprecated: use RotatedUser | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


