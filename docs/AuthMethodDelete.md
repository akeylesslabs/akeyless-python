# AuthMethodDelete

authMethodDelete is a command that deletes auth method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.auth_method_delete import AuthMethodDelete

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodDelete from a JSON string
auth_method_delete_instance = AuthMethodDelete.from_json(json)
# print the JSON string representation of the object
print(AuthMethodDelete.to_json())

# convert the object into a dict
auth_method_delete_dict = auth_method_delete_instance.to_dict()
# create an instance of AuthMethodDelete from a dict
auth_method_delete_from_dict = AuthMethodDelete.from_dict(auth_method_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


