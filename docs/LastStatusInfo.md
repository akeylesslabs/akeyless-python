# LastStatusInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrations_status** | [**MigrationStatus**](MigrationStatus.md) |  | [optional] 
**producers_errors** | **object** |  | [optional] 
**was_migrations_copied_to_new_table** | **bool** | flag to indicate migrationStatus copied to new table | [optional] 

## Example

```python
from akeyless.models.last_status_info import LastStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LastStatusInfo from a JSON string
last_status_info_instance = LastStatusInfo.from_json(json)
# print the JSON string representation of the object
print(LastStatusInfo.to_json())

# convert the object into a dict
last_status_info_dict = last_status_info_instance.to_dict()
# create an instance of LastStatusInfo from a dict
last_status_info_from_dict = LastStatusInfo.from_dict(last_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


