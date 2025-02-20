# GatewayMigrationSyncOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_migration_sync_output import GatewayMigrationSyncOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayMigrationSyncOutput from a JSON string
gateway_migration_sync_output_instance = GatewayMigrationSyncOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayMigrationSyncOutput.to_json())

# convert the object into a dict
gateway_migration_sync_output_dict = gateway_migration_sync_output_instance.to_dict()
# create an instance of GatewayMigrationSyncOutput from a dict
gateway_migration_sync_output_from_dict = GatewayMigrationSyncOutput.from_dict(gateway_migration_sync_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


