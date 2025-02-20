# UpdateDBTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_type** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**mongo_db_name** | **str** |  | [optional] 
**mongo_uri** | **str** |  | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Deprecated | [optional] 
**port** | **str** |  | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**pwd** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.update_db_target_details import UpdateDBTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDBTargetDetails from a JSON string
update_db_target_details_instance = UpdateDBTargetDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateDBTargetDetails.to_json())

# convert the object into a dict
update_db_target_details_dict = update_db_target_details_instance.to_dict()
# create an instance of UpdateDBTargetDetails from a dict
update_db_target_details_from_dict = UpdateDBTargetDetails.from_dict(update_db_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


