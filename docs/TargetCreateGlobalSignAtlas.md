# TargetCreateGlobalSignAtlas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API Key of the GlobalSign Atlas account | 
**api_secret** | **str** | API Secret of the GlobalSign Atlas account | 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**mtls_cert_data_base64** | **str** | Mutual TLS Certificate contents of the GlobalSign Atlas account encoded in base64, either mtls-cert-file-path or mtls-cert-data-base64 must be supplied | [optional] 
**mtls_key_data_base64** | **str** | Mutual TLS Key contents of the GlobalSign Atlas account encoded in base64, either mtls-key-file-path or mtls-data-base64 must be supplied | [optional] 
**name** | **str** | Target name | 
**timeout** | **str** | Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h. | [optional] [default to '5m']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.target_create_global_sign_atlas import TargetCreateGlobalSignAtlas

# TODO update the JSON string below
json = "{}"
# create an instance of TargetCreateGlobalSignAtlas from a JSON string
target_create_global_sign_atlas_instance = TargetCreateGlobalSignAtlas.from_json(json)
# print the JSON string representation of the object
print(TargetCreateGlobalSignAtlas.to_json())

# convert the object into a dict
target_create_global_sign_atlas_dict = target_create_global_sign_atlas_instance.to_dict()
# create an instance of TargetCreateGlobalSignAtlas from a dict
target_create_global_sign_atlas_from_dict = TargetCreateGlobalSignAtlas.from_dict(target_create_global_sign_atlas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


