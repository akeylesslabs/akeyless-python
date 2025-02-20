# ListItemsInPathOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | **List[str]** |  | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 
**next_page** | **str** |  | [optional] 

## Example

```python
from akeyless.models.list_items_in_path_output import ListItemsInPathOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemsInPathOutput from a JSON string
list_items_in_path_output_instance = ListItemsInPathOutput.from_json(json)
# print the JSON string representation of the object
print(ListItemsInPathOutput.to_json())

# convert the object into a dict
list_items_in_path_output_dict = list_items_in_path_output_instance.to_dict()
# create an instance of ListItemsInPathOutput from a dict
list_items_in_path_output_from_dict = ListItemsInPathOutput.from_dict(list_items_in_path_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


