# DynamicSecretTmpCredsDelete

dynamicSecretTmpCredsDelete is a command that deletes dynamic secret temp creds

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
from akeyless.models.dynamic_secret_tmp_creds_delete import DynamicSecretTmpCredsDelete

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretTmpCredsDelete from a JSON string
dynamic_secret_tmp_creds_delete_instance = DynamicSecretTmpCredsDelete.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretTmpCredsDelete.to_json())

# convert the object into a dict
dynamic_secret_tmp_creds_delete_dict = dynamic_secret_tmp_creds_delete_instance.to_dict()
# create an instance of DynamicSecretTmpCredsDelete from a dict
dynamic_secret_tmp_creds_delete_from_dict = DynamicSecretTmpCredsDelete.from_dict(dynamic_secret_tmp_creds_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


