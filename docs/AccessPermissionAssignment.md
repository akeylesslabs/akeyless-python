# AccessPermissionAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from akeyless.models.access_permission_assignment import AccessPermissionAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPermissionAssignment from a JSON string
access_permission_assignment_instance = AccessPermissionAssignment.from_json(json)
# print the JSON string representation of the object
print(AccessPermissionAssignment.to_json())

# convert the object into a dict
access_permission_assignment_dict = access_permission_assignment_instance.to_dict()
# create an instance of AccessPermissionAssignment from a dict
access_permission_assignment_from_dict = AccessPermissionAssignment.from_dict(access_permission_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


