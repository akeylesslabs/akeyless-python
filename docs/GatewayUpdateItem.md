# GatewayUpdateItem

gatewayUpdateItem is a command that updates classic key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **List[str]** | List of the new tags that will be attached to this item | [optional] 
**api_id** | **str** | API ID to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**api_key** | **str** | API key to rotate (relevant only for rotator-type&#x3D;api-key) | [optional] 
**app_id** | **str** | ApplicationId (used in azure) | [optional] 
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false] | [optional] 
**custom_payload** | **str** | Secret payload to be sent with rotation request (relevant only for rotator-type&#x3D;custom) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_metadata']
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_service_account_email** | **str** | The email of the gcp service account to rotate | [optional] 
**gcp_service_account_key_id** | **str** | The key id of the gcp service account to rotate | [optional] 
**grace_rotation** | **str** | Create a new access key without deleting the old key from AWS for backup (relevant only for AWS) [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. (relevant only for --type&#x3D;rotated-secret). If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Item name | 
**new_metadata** | **str** | Deprecated - use description | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**new_version** | **bool** | Deprecated | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rm_tag** | **List[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotated_password** | **str** | rotated-username password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotated_username** | **str** | username to be rotated, if selected \\\&quot;use-self-creds\\\&quot; at rotator-creds-type, this username will try to rotate it&#39;s own password, if \\\&quot;use-target-creds\\\&quot; is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_hour** | **int** | The Rotation Hour | [optional] [default to 0]
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_creds_type** | **str** | The rotation credentials type | [optional] [default to 'use-self-creds']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Item type | 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_item import GatewayUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateItem from a JSON string
gateway_update_item_instance = GatewayUpdateItem.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateItem.to_json())

# convert the object into a dict
gateway_update_item_dict = gateway_update_item_instance.to_dict()
# create an instance of GatewayUpdateItem from a dict
gateway_update_item_from_dict = GatewayUpdateItem.from_dict(gateway_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


