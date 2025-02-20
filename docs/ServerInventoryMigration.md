# ServerInventoryMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**ServerInventoryPayload**](ServerInventoryPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.server_inventory_migration import ServerInventoryMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInventoryMigration from a JSON string
server_inventory_migration_instance = ServerInventoryMigration.from_json(json)
# print the JSON string representation of the object
print(ServerInventoryMigration.to_json())

# convert the object into a dict
server_inventory_migration_dict = server_inventory_migration_instance.to_dict()
# create an instance of ServerInventoryMigration from a dict
server_inventory_migration_from_dict = ServerInventoryMigration.from_dict(server_inventory_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


