# MigrationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_messages** | **Dict[str, str]** |  | [optional] 
**last_reports** | **Dict[str, str]** |  | [optional] 
**last_statuses** | **Dict[str, str]** |  | [optional] 

## Example

```python
from akeyless.models.migration_status import MigrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationStatus from a JSON string
migration_status_instance = MigrationStatus.from_json(json)
# print the JSON string representation of the object
print(MigrationStatus.to_json())

# convert the object into a dict
migration_status_dict = migration_status_instance.to_dict()
# create an instance of MigrationStatus from a dict
migration_status_from_dict = MigrationStatus.from_dict(migration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


