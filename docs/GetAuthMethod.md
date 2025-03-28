# GetAuthMethod

getAuthMethod is a command that returns information about the auth method. [Deprecated: Use auth-method-get command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_auth_method import GetAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthMethod from a JSON string
get_auth_method_instance = GetAuthMethod.from_json(json)
# print the JSON string representation of the object
print(GetAuthMethod.to_json())

# convert the object into a dict
get_auth_method_dict = get_auth_method_instance.to_dict()
# create an instance of GetAuthMethod from a dict
get_auth_method_from_dict = GetAuthMethod.from_dict(get_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


