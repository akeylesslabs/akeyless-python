# GatewayUpdateTmpUsers

gatewayUpdateTmpUsers is a command that returns gateway configuration [Deprecated: Use dynamic-secret-tmp-creds-update command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_ttl_min** | **int** | New TTL in Minutes | 
**tmp_creds_id** | **str** | Tmp Creds ID | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_tmp_users import GatewayUpdateTmpUsers

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateTmpUsers from a JSON string
gateway_update_tmp_users_instance = GatewayUpdateTmpUsers.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateTmpUsers.to_json())

# convert the object into a dict
gateway_update_tmp_users_dict = gateway_update_tmp_users_instance.to_dict()
# create an instance of GatewayUpdateTmpUsers from a dict
gateway_update_tmp_users_from_dict = GatewayUpdateTmpUsers.from_dict(gateway_update_tmp_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


