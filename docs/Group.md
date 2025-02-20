# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**group_alias** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**is_subclaims_with_operator** | **bool** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**user_assignments** | [**List[AccessPermissionAssignment]**](AccessPermissionAssignment.md) |  | [optional] 

## Example

```python
from akeyless.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


