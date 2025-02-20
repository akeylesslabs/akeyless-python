# AuthMethodGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.auth_method_get import AuthMethodGet

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodGet from a JSON string
auth_method_get_instance = AuthMethodGet.from_json(json)
# print the JSON string representation of the object
print(AuthMethodGet.to_json())

# convert the object into a dict
auth_method_get_dict = auth_method_get_instance.to_dict()
# create an instance of AuthMethodGet from a dict
auth_method_get_from_dict = AuthMethodGet.from_dict(auth_method_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


