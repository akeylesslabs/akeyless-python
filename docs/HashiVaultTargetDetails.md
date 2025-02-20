# HashiVaultTargetDetails

HashiVaultTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_namespaces** | **str** |  | [optional] 
**vault_token** | **str** |  | [optional] 
**vault_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.hashi_vault_target_details import HashiVaultTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HashiVaultTargetDetails from a JSON string
hashi_vault_target_details_instance = HashiVaultTargetDetails.from_json(json)
# print the JSON string representation of the object
print(HashiVaultTargetDetails.to_json())

# convert the object into a dict
hashi_vault_target_details_dict = hashi_vault_target_details_instance.to_dict()
# create an instance of HashiVaultTargetDetails from a dict
hashi_vault_target_details_from_dict = HashiVaultTargetDetails.from_dict(hashi_vault_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


