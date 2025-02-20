# GatewayRevokeTmpUsers

gatewayRevokeTmpUsers is a command that revoke producer tmp user [Deprecated: Use dynamic-secret-tmp-creds-delete command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**revoke_all** | **bool** | Revoke All Temp Creds | [optional] 
**soft_delete** | **bool** | Soft Delete | [optional] 
**tmp_creds_id** | **str** | Tmp Creds ID | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_revoke_tmp_users import GatewayRevokeTmpUsers

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayRevokeTmpUsers from a JSON string
gateway_revoke_tmp_users_instance = GatewayRevokeTmpUsers.from_json(json)
# print the JSON string representation of the object
print(GatewayRevokeTmpUsers.to_json())

# convert the object into a dict
gateway_revoke_tmp_users_dict = gateway_revoke_tmp_users_instance.to_dict()
# create an instance of GatewayRevokeTmpUsers from a dict
gateway_revoke_tmp_users_from_dict = GatewayRevokeTmpUsers.from_dict(gateway_revoke_tmp_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


