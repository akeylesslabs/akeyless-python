# ListSharedItems

listSharedItems is a command to list all the items been shared

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_shared_items import ListSharedItems

# TODO update the JSON string below
json = "{}"
# create an instance of ListSharedItems from a JSON string
list_shared_items_instance = ListSharedItems.from_json(json)
# print the JSON string representation of the object
print(ListSharedItems.to_json())

# convert the object into a dict
list_shared_items_dict = list_shared_items_instance.to_dict()
# create an instance of ListSharedItems from a dict
list_shared_items_from_dict = ListSharedItems.from_dict(list_shared_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


