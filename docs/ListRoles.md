# ListRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter by item name or part of it | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**pagination_token** | **str** | Next page reference | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.list_roles import ListRoles

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoles from a JSON string
list_roles_instance = ListRoles.from_json(json)
# print the JSON string representation of the object
print(ListRoles.to_json())

# convert the object into a dict
list_roles_dict = list_roles_instance.to_dict()
# create an instance of ListRoles from a dict
list_roles_from_dict = ListRoles.from_dict(list_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


