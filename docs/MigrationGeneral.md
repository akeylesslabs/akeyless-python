# MigrationGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**last_migration** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**protection_key** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.migration_general import MigrationGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationGeneral from a JSON string
migration_general_instance = MigrationGeneral.from_json(json)
# print the JSON string representation of the object
print(MigrationGeneral.to_json())

# convert the object into a dict
migration_general_dict = migration_general_instance.to_dict()
# create an instance of MigrationGeneral from a dict
migration_general_from_dict = MigrationGeneral.from_dict(migration_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


