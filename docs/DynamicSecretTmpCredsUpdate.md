# DynamicSecretTmpCredsUpdate

dynamicSecretTmpCredsUpdate is a command that updates dynamic secret temp creds

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
from akeyless.models.dynamic_secret_tmp_creds_update import DynamicSecretTmpCredsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretTmpCredsUpdate from a JSON string
dynamic_secret_tmp_creds_update_instance = DynamicSecretTmpCredsUpdate.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretTmpCredsUpdate.to_json())

# convert the object into a dict
dynamic_secret_tmp_creds_update_dict = dynamic_secret_tmp_creds_update_instance.to_dict()
# create an instance of DynamicSecretTmpCredsUpdate from a dict
dynamic_secret_tmp_creds_update_from_dict = DynamicSecretTmpCredsUpdate.from_dict(dynamic_secret_tmp_creds_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


