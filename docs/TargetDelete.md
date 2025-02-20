# TargetDelete

targetDelete is a command that deletes a target

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
from akeyless.models.target_delete import TargetDelete

# TODO update the JSON string below
json = "{}"
# create an instance of TargetDelete from a JSON string
target_delete_instance = TargetDelete.from_json(json)
# print the JSON string representation of the object
print(TargetDelete.to_json())

# convert the object into a dict
target_delete_dict = target_delete_instance.to_dict()
# create an instance of TargetDelete from a dict
target_delete_from_dict = TargetDelete.from_dict(target_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


