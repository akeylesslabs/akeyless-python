# GatewayUpdateItem

gatewayUpdateItem is a command that updates classic key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**api_id** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**custom_payload** | **str** |  | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**keep_prev_version** | **str** |  | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Item name | 
**new_metadata** | **str** | New item metadata | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**new_version** | **bool** | Deprecated | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotated_password** | **str** |  | [optional] 
**rotated_username** | **str** |  | [optional] 
**rotation_hour** | **int** | The Rotation Hour | [optional] [default to 0]
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_creds_type** | **str** | The rotation credentials type | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Item type | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


