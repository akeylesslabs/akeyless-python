# DeleteTargets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_deletion** | **bool** | Enforce deletion | [optional] [default to False]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to delete the targets from | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_targets import DeleteTargets

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTargets from a JSON string
delete_targets_instance = DeleteTargets.from_json(json)
# print the JSON string representation of the object
print(DeleteTargets.to_json())

# convert the object into a dict
delete_targets_dict = delete_targets_instance.to_dict()
# create an instance of DeleteTargets from a dict
delete_targets_from_dict = DeleteTargets.from_dict(delete_targets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


