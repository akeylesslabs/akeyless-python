# RotatedSecretCreateRedshift


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_credentials** | **str** | The credentials to connect with use-user-creds/use-target-creds | [optional] [default to 'use-user-creds']
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false] | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Rotated secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**rotate_after_disconnect** | **str** | Rotate the value of the secret after SRA session ends [true/false] | [optional] [default to 'false']
**rotated_password** | **str** | rotated-username password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotated_username** | **str** | username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it&#39;s own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type&#x3D;password) | [optional] 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_hour** | **int** | The Hour of the rotation in UTC | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (1-365) | [optional] 
**rotator_type** | **str** | The rotator type. options: [target/password] | 
**secure_access_db_name** | **str** | The DB name (relevant only for DB Dynamic-Secret) | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotated_secret_create_redshift import RotatedSecretCreateRedshift

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretCreateRedshift from a JSON string
rotated_secret_create_redshift_instance = RotatedSecretCreateRedshift.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretCreateRedshift.to_json())

# convert the object into a dict
rotated_secret_create_redshift_dict = rotated_secret_create_redshift_instance.to_dict()
# create an instance of RotatedSecretCreateRedshift from a dict
rotated_secret_create_redshift_from_dict = RotatedSecretCreateRedshift.from_dict(rotated_secret_create_redshift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


