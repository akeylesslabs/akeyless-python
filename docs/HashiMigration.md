# HashiMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**HashiPayload**](HashiPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.hashi_migration import HashiMigration

# TODO update the JSON string below
json = "{}"
# create an instance of HashiMigration from a JSON string
hashi_migration_instance = HashiMigration.from_json(json)
# print the JSON string representation of the object
print(HashiMigration.to_json())

# convert the object into a dict
hashi_migration_dict = hashi_migration_instance.to_dict()
# create an instance of HashiMigration from a dict
hashi_migration_from_dict = HashiMigration.from_dict(hashi_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


