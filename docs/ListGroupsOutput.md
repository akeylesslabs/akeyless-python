# ListGroupsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) |  | [optional] 
**next_page** | **str** |  | [optional] 

## Example

```python
from akeyless.models.list_groups_output import ListGroupsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroupsOutput from a JSON string
list_groups_output_instance = ListGroupsOutput.from_json(json)
# print the JSON string representation of the object
print(ListGroupsOutput.to_json())

# convert the object into a dict
list_groups_output_dict = list_groups_output_instance.to_dict()
# create an instance of ListGroupsOutput from a dict
list_groups_output_from_dict = ListGroupsOutput.from_dict(list_groups_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


