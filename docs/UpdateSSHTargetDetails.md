# UpdateSSHTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The ssh host name | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Deprecated | [optional] 
**port** | **str** | ssh port | [optional] [default to '22']
**private_key** | **str** | ssh private key | [optional] 
**private_key_password** | **str** | The ssh private key password | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**ssh_password** | **str** | ssh pawssword to rotate | [optional] 
**ssh_username** | **str** | ssh username | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_ssh_target_details import UpdateSSHTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSSHTargetDetails from a JSON string
update_ssh_target_details_instance = UpdateSSHTargetDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateSSHTargetDetails.to_json())

# convert the object into a dict
update_ssh_target_details_dict = update_ssh_target_details_instance.to_dict()
# create an instance of UpdateSSHTargetDetails from a dict
update_ssh_target_details_from_dict = UpdateSSHTargetDetails.from_dict(update_ssh_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


