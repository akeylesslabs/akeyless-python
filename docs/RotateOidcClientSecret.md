# RotateOidcClientSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | OIDC application name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.rotate_oidc_client_secret import RotateOidcClientSecret

# TODO update the JSON string below
json = "{}"
# create an instance of RotateOidcClientSecret from a JSON string
rotate_oidc_client_secret_instance = RotateOidcClientSecret.from_json(json)
# print the JSON string representation of the object
print(RotateOidcClientSecret.to_json())

# convert the object into a dict
rotate_oidc_client_secret_dict = rotate_oidc_client_secret_instance.to_dict()
# create an instance of RotateOidcClientSecret from a dict
rotate_oidc_client_secret_from_dict = RotateOidcClientSecret.from_dict(rotate_oidc_client_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


