# ListItemsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Item]**](Item.md) |  | [optional] 
**next_page** | **str** |  | [optional] 

## Example

```python
from akeyless.models.list_items_output import ListItemsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemsOutput from a JSON string
list_items_output_instance = ListItemsOutput.from_json(json)
# print the JSON string representation of the object
print(ListItemsOutput.to_json())

# convert the object into a dict
list_items_output_dict = list_items_output_instance.to_dict()
# create an instance of ListItemsOutput from a dict
list_items_output_from_dict = ListItemsOutput.from_dict(list_items_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


