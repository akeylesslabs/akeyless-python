# CreateHashiVaultTarget

createHashiVaultTarget is a command that creates a new hashi-vault target. [Deprecated: Use target-create-hashi-vault command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**hashi_url** | **str** | HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**namespace** | **List[str]** | Comma-separated list of vault namespaces | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**vault_token** | **str** | Vault access token with sufficient permissions | [optional] 

## Example

```python
from akeyless.models.create_hashi_vault_target import CreateHashiVaultTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHashiVaultTarget from a JSON string
create_hashi_vault_target_instance = CreateHashiVaultTarget.from_json(json)
# print the JSON string representation of the object
print(CreateHashiVaultTarget.to_json())

# convert the object into a dict
create_hashi_vault_target_dict = create_hashi_vault_target_instance.to_dict()
# create an instance of CreateHashiVaultTarget from a dict
create_hashi_vault_target_from_dict = CreateHashiVaultTarget.from_dict(create_hashi_vault_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


