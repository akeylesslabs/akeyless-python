# DynamicSecretTmpCredsGet

dynamicSecretTmpCredsGet is a command that returns dynamic secret temp creds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_tmp_creds_get import DynamicSecretTmpCredsGet

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretTmpCredsGet from a JSON string
dynamic_secret_tmp_creds_get_instance = DynamicSecretTmpCredsGet.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretTmpCredsGet.to_json())

# convert the object into a dict
dynamic_secret_tmp_creds_get_dict = dynamic_secret_tmp_creds_get_instance.to_dict()
# create an instance of DynamicSecretTmpCredsGet from a dict
dynamic_secret_tmp_creds_get_from_dict = DynamicSecretTmpCredsGet.from_dict(dynamic_secret_tmp_creds_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


