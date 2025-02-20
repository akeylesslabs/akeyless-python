# MigrationsConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_migrations** | [**List[ActiveDirectoryMigration]**](ActiveDirectoryMigration.md) |  | [optional] 
**aws_secrets_migrations** | [**List[AWSSecretsMigration]**](AWSSecretsMigration.md) |  | [optional] 
**azure_kv_migrations** | [**List[AzureKeyVaultMigration]**](AzureKeyVaultMigration.md) |  | [optional] 
**gcp_secrets_migrations** | [**List[GCPSecretsMigration]**](GCPSecretsMigration.md) |  | [optional] 
**hashi_migrations** | [**List[HashiMigration]**](HashiMigration.md) |  | [optional] 
**k8s_migrations** | [**List[K8SMigration]**](K8SMigration.md) |  | [optional] 
**mock_migrations** | [**List[MockMigration]**](MockMigration.md) |  | [optional] 
**one_password_migrations** | [**List[OnePasswordMigration]**](OnePasswordMigration.md) |  | [optional] 
**server_inventory_migrations** | [**List[ServerInventoryMigration]**](ServerInventoryMigration.md) |  | [optional] 

## Example

```python
from akeyless.models.migrations_config_part import MigrationsConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsConfigPart from a JSON string
migrations_config_part_instance = MigrationsConfigPart.from_json(json)
# print the JSON string representation of the object
print(MigrationsConfigPart.to_json())

# convert the object into a dict
migrations_config_part_dict = migrations_config_part_instance.to_dict()
# create an instance of MigrationsConfigPart from a dict
migrations_config_part_from_dict = MigrationsConfigPart.from_dict(migrations_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


