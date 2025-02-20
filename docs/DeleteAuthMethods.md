# DeleteAuthMethods

deleteAuthMethods is a command that deletes multiple auth methods from a given path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | Path to delete the auth methods from | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_auth_methods import DeleteAuthMethods

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAuthMethods from a JSON string
delete_auth_methods_instance = DeleteAuthMethods.from_json(json)
# print the JSON string representation of the object
print(DeleteAuthMethods.to_json())

# convert the object into a dict
delete_auth_methods_dict = delete_auth_methods_instance.to_dict()
# create an instance of DeleteAuthMethods from a dict
delete_auth_methods_from_dict = DeleteAuthMethods.from_dict(delete_auth_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


