# UpdateGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**group_alias** | **str** | A short group alias | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Group name | 
**new_name** | **str** | Group new name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_assignment** | **str** | A json string defining the access permission assignment for this client | [optional] 

## Example

```python
from akeyless.models.update_group import UpdateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroup from a JSON string
update_group_instance = UpdateGroup.from_json(json)
# print the JSON string representation of the object
print(UpdateGroup.to_json())

# convert the object into a dict
update_group_dict = update_group_instance.to_dict()
# create an instance of UpdateGroup from a dict
update_group_from_dict = UpdateGroup.from_dict(update_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


