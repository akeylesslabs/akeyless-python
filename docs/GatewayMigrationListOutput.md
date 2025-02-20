# GatewayMigrationListOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**MigrationsConfigPart**](MigrationsConfigPart.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_migration_list_output import GatewayMigrationListOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigrationListOutput from a JSON string
gateway_migration_list_output_instance = GatewayMigrationListOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayMigrationListOutput.to_json())

# convert the object into a dict
gateway_migration_list_output_dict = gateway_migration_list_output_instance.to_dict()
# create an instance of GatewayMigrationListOutput from a dict
gateway_migration_list_output_from_dict = GatewayMigrationListOutput.from_dict(gateway_migration_list_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


