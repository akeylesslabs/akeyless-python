# TargetCreateSsh

targetCreateSsh is a command that creates a new ssh target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**host** | **str** | SSH host name | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**port** | **str** | SSH port | [optional] [default to '22']
**private_key** | **str** | SSH private key | [optional] 
**private_key_password** | **str** | SSH private key password | [optional] 
**ssh_password** | **str** | SSH password to rotate | [optional] 
**ssh_username** | **str** | SSH username | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_create_ssh import TargetCreateSsh

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateSsh from a JSON string
target_create_ssh_instance = TargetCreateSsh.from_json(json)
# print the JSON string representation of the object
print(TargetCreateSsh.to_json())

# convert the object into a dict
target_create_ssh_dict = target_create_ssh_instance.to_dict()
# create an instance of TargetCreateSsh from a dict
target_create_ssh_from_dict = TargetCreateSsh.from_dict(target_create_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


