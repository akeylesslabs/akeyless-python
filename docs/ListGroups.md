# ListGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter by auth method name or part of it | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**pagination_token** | **str** | Next page reference | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_groups import ListGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroups from a JSON string
list_groups_instance = ListGroups.from_json(json)
# print the JSON string representation of the object
print(ListGroups.to_json())

# convert the object into a dict
list_groups_dict = list_groups_instance.to_dict()
# create an instance of ListGroups from a dict
list_groups_from_dict = ListGroups.from_dict(list_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


