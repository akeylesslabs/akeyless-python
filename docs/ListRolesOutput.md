# ListRolesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from akeyless.models.list_roles_output import ListRolesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListRolesOutput from a JSON string
list_roles_output_instance = ListRolesOutput.from_json(json)
# print the JSON string representation of the object
print(ListRolesOutput.to_json())

# convert the object into a dict
list_roles_output_dict = list_roles_output_instance.to_dict()
# create an instance of ListRolesOutput from a dict
list_roles_output_from_dict = ListRolesOutput.from_dict(list_roles_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


