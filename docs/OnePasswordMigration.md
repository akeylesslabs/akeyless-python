# OnePasswordMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**MigrationGeneral**](MigrationGeneral.md) |  | [optional] 
**payload** | [**OnePasswordPayload**](OnePasswordPayload.md) |  | [optional] 

## Example

```python
from akeyless.models.one_password_migration import OnePasswordMigration

# TODO update the JSON string below
json = "{}"
# create an instance of OnePasswordMigration from a JSON string
one_password_migration_instance = OnePasswordMigration.from_json(json)
# print the JSON string representation of the object
print(OnePasswordMigration.to_json())

# convert the object into a dict
one_password_migration_dict = one_password_migration_instance.to_dict()
# create an instance of OnePasswordMigration from a dict
one_password_migration_from_dict = OnePasswordMigration.from_dict(one_password_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


