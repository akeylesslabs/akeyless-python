# ActiveDirectoryMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**ActiveDirectoryPayload**](ActiveDirectoryPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.active_directory_migration import ActiveDirectoryMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryMigration from a JSON string
active_directory_migration_instance = ActiveDirectoryMigration.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryMigration.to_json())

# convert the object into a dict
active_directory_migration_dict = active_directory_migration_instance.to_dict()
# create an instance of ActiveDirectoryMigration from a dict
active_directory_migration_from_dict = ActiveDirectoryMigration.from_dict(active_directory_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


