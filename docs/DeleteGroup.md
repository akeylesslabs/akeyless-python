# DeleteGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Group name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_group import DeleteGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGroup from a JSON string
delete_group_instance = DeleteGroup.from_json(json)
# print the JSON string representation of the object
print(DeleteGroup.to_json())

# convert the object into a dict
delete_group_dict = delete_group_instance.to_dict()
# create an instance of DeleteGroup from a dict
delete_group_from_dict = DeleteGroup.from_dict(delete_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


