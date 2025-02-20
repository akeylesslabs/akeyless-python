# MigrationItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** |  | [optional] 
**migrated** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 

## Example

```python
from akeyless.models.migration_items import MigrationItems

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationItems from a JSON string
migration_items_instance = MigrationItems.from_json(json)
# print the JSON string representation of the object
print(MigrationItems.to_json())

# convert the object into a dict
migration_items_dict = migration_items_instance.to_dict()
# create an instance of MigrationItems from a dict
migration_items_from_dict = MigrationItems.from_dict(migration_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


