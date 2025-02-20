# MigrationStatusReplyObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computers** | **int** |  | [optional] 
**duration_time** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**last_status_message** | **str** |  | [optional] 
**max_name_length** | **int** |  | [optional] 
**max_value_length** | **int** |  | [optional] 
**migration_id** | **str** |  | [optional] 
**migration_items** | [**MigrationItems**](MigrationItems.md) |  | [optional] 
**migration_name** | **str** |  | [optional] 
**migration_state** | **str** |  | [optional] 
**migration_type** | **str** |  | [optional] 
**migration_type_name** | **str** |  | [optional] 
**rotated_secrets** | [**MigrationItems**](MigrationItems.md) |  | [optional] 
**start_time** | **str** |  | [optional] 
**targets** | [**MigrationItems**](MigrationItems.md) |  | [optional] 

## Example

```python
from akeyless.models.migration_status_reply_obj import MigrationStatusReplyObj

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationStatusReplyObj from a JSON string
migration_status_reply_obj_instance = MigrationStatusReplyObj.from_json(json)
# print the JSON string representation of the object
print(MigrationStatusReplyObj.to_json())

# convert the object into a dict
migration_status_reply_obj_dict = migration_status_reply_obj_instance.to_dict()
# create an instance of MigrationStatusReplyObj from a dict
migration_status_reply_obj_from_dict = MigrationStatusReplyObj.from_dict(migration_status_reply_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


