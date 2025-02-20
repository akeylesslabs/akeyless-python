# ActiveDirectoryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_target_id** | **int** |  | [optional] 
**auto_rotate** | **bool** |  | [optional] 
**auto_rotate_interval_in_days** | **int** |  | [optional] 
**auto_rotate_rotation_hour** | **int** |  | [optional] 
**computer_base_dn** | **str** |  | [optional] 
**discover_local_users** | **bool** | Deprecated | [optional] 
**discover_services** | **bool** |  | [optional] 
**discovery_types** | **List[str]** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**domain_server_targets_path_template** | **str** |  | [optional] 
**domain_users_rotated_secrets_path_template** | **str** |  | [optional] 
**enable_rdp_sra** | **bool** |  | [optional] 
**local_users_ignore_list** | **Dict[str, bool]** |  | [optional] 
**local_users_rotated_secrets_path_template** | **str** |  | [optional] 
**os_filter** | **str** |  | [optional] 
**ssh_port** | **str** |  | [optional] 
**target_format** | **str** |  | [optional] 
**targets_type** | **str** |  | [optional] 
**user_base_dn** | **str** |  | [optional] 
**user_groups** | **List[str]** |  | [optional] 
**winrm_over_http** | **bool** |  | [optional] 
**winrm_port** | **str** |  | [optional] 

## Example

```python
from akeyless.models.active_directory_payload import ActiveDirectoryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryPayload from a JSON string
active_directory_payload_instance = ActiveDirectoryPayload.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryPayload.to_json())

# convert the object into a dict
active_directory_payload_dict = active_directory_payload_instance.to_dict()
# create an instance of ActiveDirectoryPayload from a dict
active_directory_payload_from_dict = ActiveDirectoryPayload.from_dict(active_directory_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


