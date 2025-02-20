# DeleteAuthMethod

deleteAuthMethod is a command that deletes the auth method. [Deprecated: Use auth-method-delete command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_auth_method import DeleteAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAuthMethod from a JSON string
delete_auth_method_instance = DeleteAuthMethod.from_json(json)
# print the JSON string representation of the object
print(DeleteAuthMethod.to_json())

# convert the object into a dict
delete_auth_method_dict = delete_auth_method_instance.to_dict()
# create an instance of DeleteAuthMethod from a dict
delete_auth_method_from_dict = DeleteAuthMethod.from_dict(delete_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


