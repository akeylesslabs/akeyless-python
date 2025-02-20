# DeleteRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to delete the auth methods from | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_roles import DeleteRoles

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoles from a JSON string
delete_roles_instance = DeleteRoles.from_json(json)
# print the JSON string representation of the object
print(DeleteRoles.to_json())

# convert the object into a dict
delete_roles_dict = delete_roles_instance.to_dict()
# create an instance of DeleteRoles from a dict
delete_roles_from_dict = DeleteRoles.from_dict(delete_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


