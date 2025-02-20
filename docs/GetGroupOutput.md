# GetGroupOutput


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
from akeyless.models.get_group_output import GetGroupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupOutput from a JSON string
get_group_output_instance = GetGroupOutput.from_json(json)
# print the JSON string representation of the object
print(GetGroupOutput.to_json())

# convert the object into a dict
get_group_output_dict = get_group_output_instance.to_dict()
# create an instance of GetGroupOutput from a dict
get_group_output_from_dict = GetGroupOutput.from_dict(get_group_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


