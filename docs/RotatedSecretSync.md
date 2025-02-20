# RotatedSecretSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**namespace** | **str** | Vault namespace, releavnt only for Hashicorp Vault Target | [optional] 
**remote_secret_name** | **str** | Remote Secret Name that will be synced on the remote endpoint | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Universal Secret Connector name, If not provided all attached USC&#39;s will be synced | [optional] 

## Example

```python
from akeyless.models.rotated_secret_sync import RotatedSecretSync

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretSync from a JSON string
rotated_secret_sync_instance = RotatedSecretSync.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretSync.to_json())

# convert the object into a dict
rotated_secret_sync_dict = rotated_secret_sync_instance.to_dict()
# create an instance of RotatedSecretSync from a dict
rotated_secret_sync_from_dict = RotatedSecretSync.from_dict(rotated_secret_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


