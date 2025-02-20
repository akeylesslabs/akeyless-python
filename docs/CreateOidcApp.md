# CreateOidcApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**audience** | **str** | A comma separated list of allowed audiences | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the OIDC application (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | OIDC application name | 
**permission_assignment** | **str** | A json string defining the access permission assignment for this app | [optional] 
**public** | **bool** | Set to true if the app is public (cannot keep secrets) | [optional] 
**redirect_uris** | **str** | A comma separated list of allowed redirect uris | [optional] 
**scopes** | **str** | A comma separated list of allowed scopes | [optional] [default to 'openid']
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_oidc_app import CreateOidcApp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOidcApp from a JSON string
create_oidc_app_instance = CreateOidcApp.from_json(json)
# print the JSON string representation of the object
print(CreateOidcApp.to_json())

# convert the object into a dict
create_oidc_app_dict = create_oidc_app_instance.to_dict()
# create an instance of CreateOidcApp from a dict
create_oidc_app_from_dict = CreateOidcApp.from_dict(create_oidc_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


