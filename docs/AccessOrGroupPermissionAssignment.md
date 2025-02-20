# AccessOrGroupPermissionAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 
**assignment_name** | **str** |  | [optional] 
**assignment_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**sub_claims** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from akeyless.models.access_or_group_permission_assignment import AccessOrGroupPermissionAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AccessOrGroupPermissionAssignment from a JSON string
access_or_group_permission_assignment_instance = AccessOrGroupPermissionAssignment.from_json(json)
# print the JSON string representation of the object
print(AccessOrGroupPermissionAssignment.to_json())

# convert the object into a dict
access_or_group_permission_assignment_dict = access_or_group_permission_assignment_instance.to_dict()
# create an instance of AccessOrGroupPermissionAssignment from a dict
access_or_group_permission_assignment_from_dict = AccessOrGroupPermissionAssignment.from_dict(access_or_group_permission_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


