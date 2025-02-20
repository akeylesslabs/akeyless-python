# GatewayMigrationGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**MigrationsConfigPart**](MigrationsConfigPart.md) |  | [optional] 

## Example

```python
from akeyless.models.gateway_migration_get_output import GatewayMigrationGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigrationGetOutput from a JSON string
gateway_migration_get_output_instance = GatewayMigrationGetOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayMigrationGetOutput.to_json())

# convert the object into a dict
gateway_migration_get_output_dict = gateway_migration_get_output_instance.to_dict()
# create an instance of GatewayMigrationGetOutput from a dict
gateway_migration_get_output_from_dict = GatewayMigrationGetOutput.from_dict(gateway_migration_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


