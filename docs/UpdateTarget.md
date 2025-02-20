# UpdateTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] [default to 'default_comment']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**new_comment** | **str** | Deprecated - use description | [optional] [default to 'default_comment']
**new_name** | **str** | New target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_target import UpdateTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTarget from a JSON string
update_target_instance = UpdateTarget.from_json(json)
# print the JSON string representation of the object
print(UpdateTarget.to_json())

# convert the object into a dict
update_target_dict = update_target_instance.to_dict()
# create an instance of UpdateTarget from a dict
update_target_from_dict = UpdateTarget.from_dict(update_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


