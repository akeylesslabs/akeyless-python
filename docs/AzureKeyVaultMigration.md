# AzureKeyVaultMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**AzurePayload**](AzurePayload.md) |  | [optional] 

## Example

```python
from akeyless.models.azure_key_vault_migration import AzureKeyVaultMigration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultMigration from a JSON string
azure_key_vault_migration_instance = AzureKeyVaultMigration.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultMigration.to_json())

# convert the object into a dict
azure_key_vault_migration_dict = azure_key_vault_migration_instance.to_dict()
# create an instance of AzureKeyVaultMigration from a dict
azure_key_vault_migration_from_dict = AzureKeyVaultMigration.from_dict(azure_key_vault_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


