# MigrationsConfigLastChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_migrations** | **List[str]** |  | [optional] 
**created_migrations** | **List[str]** |  | [optional] 
**deleted_migrations** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.migrations_config_last_change import MigrationsConfigLastChange

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsConfigLastChange from a JSON string
migrations_config_last_change_instance = MigrationsConfigLastChange.from_json(json)
# print the JSON string representation of the object
print(MigrationsConfigLastChange.to_json())

# convert the object into a dict
migrations_config_last_change_dict = migrations_config_last_change_instance.to_dict()
# create an instance of MigrationsConfigLastChange from a dict
migrations_config_last_change_from_dict = MigrationsConfigLastChange.from_dict(migrations_config_last_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


