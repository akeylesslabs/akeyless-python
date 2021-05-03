# UpdateRotatedSecretSC

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Secret name | 
**new_metadata** | **str** | New item metadata | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**new_version** | **bool** | Whether to create a new version of not | [optional] [default to False]
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 
**ssh_username** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


