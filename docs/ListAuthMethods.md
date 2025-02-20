# ListAuthMethods

listAuthMethods is a command that returns a list of all auth methods in the account. [Deprecated: Use auth-method-list command]

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
from akeyless.models.list_auth_methods import ListAuthMethods

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthMethods from a JSON string
list_auth_methods_instance = ListAuthMethods.from_json(json)
# print the JSON string representation of the object
print(ListAuthMethods.to_json())

# convert the object into a dict
list_auth_methods_dict = list_auth_methods_instance.to_dict()
# create an instance of ListAuthMethods from a dict
list_auth_methods_from_dict = ListAuthMethods.from_dict(list_auth_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


