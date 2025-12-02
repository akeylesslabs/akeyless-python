# RotatedSecretDetailsInfo

RotatedSecretDetailsInfo The rotated secret rotator info
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_previous_version_in_days** | **int** |  | [optional] 
**enable_custom_password_policy** | **bool** |  | [optional] 
**grace_rotation** | **bool** |  | [optional] 
**grace_rotation_hour** | **int** |  | [optional] 
**grace_rotation_interval** | **int** |  | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**iis_apps_details** | [**list[WindowsService]**](WindowsService.md) |  | [optional] 
**last_rotation_error** | **str** |  | [optional] 
**managed_by_akeyless** | **bool** |  | [optional] 
**max_versions** | **int** |  | [optional] 
**next_auto_rotate_type** | **str** |  | [optional] 
**number_of_versions_to_save** | **int** |  | [optional] 
**public_key_remote_path** | **str** |  | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval_min** | **bool** |  | [optional] 
**rotation_statement** | **str** |  | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_status** | **str** | RotationStatus defines types of rotation Status | [optional] 
**rotator_type** | **str** |  | [optional] 
**same_password** | **bool** |  | [optional] 
**services_details** | [**list[WindowsService]**](WindowsService.md) |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


