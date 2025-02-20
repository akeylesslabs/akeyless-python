# ListItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**advanced_filter** | **str** | Filter by item name/username/website or part of it | [optional] 
**auto_pagination** | **str** | Retrieve all items using pagination, when disabled retrieving only first 1000 items | [optional] [default to 'enabled']
**filter** | **str** | Filter by item name or part of it | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**minimal_view** | **bool** | Show only basic information of the items | [optional] 
**modified_after** | **int** | List only secrets modified after specified date (in unix time) | [optional] 
**pagination_token** | **str** | Next page reference | [optional] 
**path** | **str** | Path to folder | [optional] 
**sra_only** | **bool** | Filter by items with SRA functionality enabled | [optional] [default to False]
**sub_types** | **List[str]** |  | [optional] 
**tag** | **str** | Filter by item tag | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **List[str]** | The item types list of the requested items. In case it is empty, all types of items will be returned. options: [key, static-secret, dynamic-secret, classic-key] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_items import ListItems

# TODO update the JSON string below
json = "{}"
# create an instance of ListItems from a JSON string
list_items_instance = ListItems.from_json(json)
# print the JSON string representation of the object
print(ListItems.to_json())

# convert the object into a dict
list_items_dict = list_items_instance.to_dict()
# create an instance of ListItems from a dict
list_items_from_dict = ListItems.from_dict(list_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


