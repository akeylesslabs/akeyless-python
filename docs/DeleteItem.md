# DeleteItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**delete_immediately** | **bool** | When delete-in-days&#x3D;-1, must be set | [optional] [default to False]
**delete_in_days** | **int** | The number of days to wait before deleting the item (relevant for keys only) | [optional] [default to 7]
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Item name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The specific version you want to delete - 0&#x3D;last version, -1&#x3D;entire item with all versions (default) | [optional] [default to -1]

## Example

```python
from akeyless.models.delete_item import DeleteItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItem from a JSON string
delete_item_instance = DeleteItem.from_json(json)
# print the JSON string representation of the object
print(DeleteItem.to_json())

# convert the object into a dict
delete_item_dict = delete_item_instance.to_dict()
# create an instance of DeleteItem from a dict
delete_item_from_dict = DeleteItem.from_dict(delete_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


