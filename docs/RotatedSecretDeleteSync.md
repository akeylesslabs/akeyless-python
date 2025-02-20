# RotatedSecretDeleteSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Universal Secret Connector name | 

## Example

```python
from akeyless.models.rotated_secret_delete_sync import RotatedSecretDeleteSync

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretDeleteSync from a JSON string
rotated_secret_delete_sync_instance = RotatedSecretDeleteSync.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretDeleteSync.to_json())

# convert the object into a dict
rotated_secret_delete_sync_dict = rotated_secret_delete_sync_instance.to_dict()
# create an instance of RotatedSecretDeleteSync from a dict
rotated_secret_delete_sync_from_dict = RotatedSecretDeleteSync.from_dict(rotated_secret_delete_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


