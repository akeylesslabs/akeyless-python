# AuthMethodList

authMethodList is a command that returns a list of auth methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter by auth method name or part of it | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**pagination_token** | **str** | Next page reference | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **List[str]** | The Auth method types list of the requested method. In case it is empty, all types of auth methods will be returned. options: [api_key, azure_ad, oauth2/jwt, saml2, ldap, aws_iam, oidc, universal_identity, gcp, k8s, cert] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.auth_method_list import AuthMethodList

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodList from a JSON string
auth_method_list_instance = AuthMethodList.from_json(json)
# print the JSON string representation of the object
print(AuthMethodList.to_json())

# convert the object into a dict
auth_method_list_dict = auth_method_list_instance.to_dict()
# create an instance of AuthMethodList from a dict
auth_method_list_from_dict = AuthMethodList.from_dict(auth_method_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


