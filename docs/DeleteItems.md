# DeleteItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **List[str]** | A list of items to delete, To specify multiple items use argument multiple times | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to delete the items from | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_items import DeleteItems

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItems from a JSON string
delete_items_instance = DeleteItems.from_json(json)
# print the JSON string representation of the object
print(DeleteItems.to_json())

# convert the object into a dict
delete_items_dict = delete_items_instance.to_dict()
# create an instance of DeleteItems from a dict
delete_items_from_dict = DeleteItems.from_dict(delete_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


