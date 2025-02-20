# UpdateOidcApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | A comma separated list of allowed audiences | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the OIDC application (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | OIDC application name | 
**permission_assignment** | **str** | A json string defining the access permission assignment for this app | [optional] 
**public** | **bool** | Set to true if the app is public (cannot keep secrets) | [optional] 
**redirect_uris** | **str** | A comma separated list of allowed redirect uris | [optional] 
**scopes** | **str** | A comma separated list of allowed scopes | [optional] [default to 'openid']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_oidc_app import UpdateOidcApp

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOidcApp from a JSON string
update_oidc_app_instance = UpdateOidcApp.from_json(json)
# print the JSON string representation of the object
print(UpdateOidcApp.to_json())

# convert the object into a dict
update_oidc_app_dict = update_oidc_app_instance.to_dict()
# create an instance of UpdateOidcApp from a dict
update_oidc_app_from_dict = UpdateOidcApp.from_dict(update_oidc_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


