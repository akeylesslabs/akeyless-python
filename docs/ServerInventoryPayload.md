# ServerInventoryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_rotate** | **bool** |  | [optional] 
**auto_rotate_interval_in_days** | **int** |  | [optional] 
**auto_rotate_rotation_hour** | **int** |  | [optional] 
**enable_rdp_sra** | **bool** |  | [optional] 
**migration_target_id** | **int** |  | [optional] 
**server_targets_path_template** | **str** |  | [optional] 
**user_groups** | **List[str]** |  | [optional] 
**users_ignore_list** | **Dict[str, bool]** |  | [optional] 
**users_rotated_secrets_path_template** | **str** |  | [optional] 

## Example

```python
from akeyless.models.server_inventory_payload import ServerInventoryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInventoryPayload from a JSON string
server_inventory_payload_instance = ServerInventoryPayload.from_json(json)
# print the JSON string representation of the object
print(ServerInventoryPayload.to_json())

# convert the object into a dict
server_inventory_payload_dict = server_inventory_payload_instance.to_dict()
# create an instance of ServerInventoryPayload from a dict
server_inventory_payload_from_dict = ServerInventoryPayload.from_dict(server_inventory_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


