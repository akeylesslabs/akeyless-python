# TargetUpdateHashiVault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**hashi_url** | **str** | HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**namespace** | **List[str]** | Comma-separated list of vault namespaces | [optional] 
**new_name** | **str** | New target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**vault_token** | **str** | Vault access token with sufficient permissions | [optional] 

## Example

```python
from akeyless.models.target_update_hashi_vault import TargetUpdateHashiVault

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpdateHashiVault from a JSON string
target_update_hashi_vault_instance = TargetUpdateHashiVault.from_json(json)
# print the JSON string representation of the object
print(TargetUpdateHashiVault.to_json())

# convert the object into a dict
target_update_hashi_vault_dict = target_update_hashi_vault_instance.to_dict()
# create an instance of TargetUpdateHashiVault from a dict
target_update_hashi_vault_from_dict = TargetUpdateHashiVault.from_dict(target_update_hashi_vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


