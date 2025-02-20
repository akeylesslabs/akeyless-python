# DeleteTarget

deleteTarget is a command that deletes a target. [Deprecated: Use target-delete command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_deletion** | **bool** | Enforce deletion | [optional] [default to False]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Target name | 
**target_version** | **int** | Target version | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_target import DeleteTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTarget from a JSON string
delete_target_instance = DeleteTarget.from_json(json)
# print the JSON string representation of the object
print(DeleteTarget.to_json())

# convert the object into a dict
delete_target_dict = delete_target_instance.to_dict()
# create an instance of DeleteTarget from a dict
delete_target_from_dict = DeleteTarget.from_dict(delete_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


