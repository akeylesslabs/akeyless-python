# RotatedSecretUpdateSnowflake


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **List[str]** | List of the new tags that will be attached to this item | [optional] 
**authentication_credentials** | **str** | The credentials to connect with use-user-creds/use-target-creds | [optional] [default to 'use-user-creds']
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false] | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_metadata']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Rotated secret name | 
**new_name** | **str** | New item name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rm_tag** | **List[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotated_password** | **str** | rotated-username password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotated_username** | **str** | username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it&#39;s own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_hour** | **int** | The Hour of the rotation in UTC | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotated_secret_update_snowflake import RotatedSecretUpdateSnowflake

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretUpdateSnowflake from a JSON string
rotated_secret_update_snowflake_instance = RotatedSecretUpdateSnowflake.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretUpdateSnowflake.to_json())

# convert the object into a dict
rotated_secret_update_snowflake_dict = rotated_secret_update_snowflake_instance.to_dict()
# create an instance of RotatedSecretUpdateSnowflake from a dict
rotated_secret_update_snowflake_from_dict = RotatedSecretUpdateSnowflake.from_dict(rotated_secret_update_snowflake_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


