# UidRevokeToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** | The universal identity auth method name | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**revoke_token** | **str** | the universal identity token/token-id to revoke | 
**revoke_type** | **str** | revokeSelf/revokeAll (delete only this token/this token and his children) | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.uid_revoke_token import UidRevokeToken

# TODO update the JSON string below
json = "{}"
# create an instance of UidRevokeToken from a JSON string
uid_revoke_token_instance = UidRevokeToken.from_json(json)
# print the JSON string representation of the object
print(UidRevokeToken.to_json())

# convert the object into a dict
uid_revoke_token_dict = uid_revoke_token_instance.to_dict()
# create an instance of UidRevokeToken from a dict
uid_revoke_token_from_dict = UidRevokeToken.from_dict(uid_revoke_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


