# MockMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**MockPayload**](MockPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.mock_migration import MockMigration

# TODO update the JSON string below
json = "{}"
# create an instance of MockMigration from a JSON string
mock_migration_instance = MockMigration.from_json(json)
# print the JSON string representation of the object
print(MockMigration.to_json())

# convert the object into a dict
mock_migration_dict = mock_migration_instance.to_dict()
# create an instance of MockMigration from a dict
mock_migration_from_dict = MockMigration.from_dict(mock_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


