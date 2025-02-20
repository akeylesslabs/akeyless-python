# DeleteItemsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_items** | **List[str]** |  | [optional] 
**failed_deleted_items** | **Dict[str, str]** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from akeyless.models.delete_items_output import DeleteItemsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemsOutput from a JSON string
delete_items_output_instance = DeleteItemsOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteItemsOutput.to_json())

# convert the object into a dict
delete_items_output_dict = delete_items_output_instance.to_dict()
# create an instance of DeleteItemsOutput from a dict
delete_items_output_from_dict = DeleteItemsOutput.from_dict(delete_items_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


