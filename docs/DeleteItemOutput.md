# DeleteItemOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_date** | **datetime** |  | [optional] 
**item_id** | **int** |  | [optional] 
**item_name** | **str** |  | [optional] 
**version_deleted** | **int** |  | [optional] 

## Example

```python
from akeyless.models.delete_item_output import DeleteItemOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemOutput from a JSON string
delete_item_output_instance = DeleteItemOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteItemOutput.to_json())

# convert the object into a dict
delete_item_output_dict = delete_item_output_instance.to_dict()
# create an instance of DeleteItemOutput from a dict
delete_item_output_from_dict = DeleteItemOutput.from_dict(delete_item_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


