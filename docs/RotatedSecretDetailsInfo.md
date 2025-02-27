# RotatedSecretDetailsInfo

RotatedSecretDetailsInfo The rotated secret rotator info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_previous_version_in_days** | **int** |  | [optional] 
**grace_rotation** | **bool** |  | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**last_rotation_error** | **str** |  | [optional] 
**managed_by_akeyless** | **bool** |  | [optional] 
**max_versions** | **int** |  | [optional] 
**number_of_versions_to_save** | **int** |  | [optional] 
**rotation_hour** | **int** |  | [optional] 
**rotation_interval_min** | **bool** |  | [optional] 
**rotation_statement** | **str** |  | [optional] 
**rotator_creds_type** | **str** |  | [optional] 
**rotator_status** | **str** | RotationStatus defines types of rotation Status | [optional] 
**rotator_type** | **str** |  | [optional] 
**same_password** | **bool** |  | [optional] 
**services_details** | [**List[WindowsService]**](WindowsService.md) |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 

## Example

```python
from akeyless.models.rotated_secret_details_info import RotatedSecretDetailsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RotatedSecretDetailsInfo from a JSON string
rotated_secret_details_info_instance = RotatedSecretDetailsInfo.from_json(json)
# print the JSON string representation of the object
print(RotatedSecretDetailsInfo.to_json())

# convert the object into a dict
rotated_secret_details_info_dict = rotated_secret_details_info_instance.to_dict()
# create an instance of RotatedSecretDetailsInfo from a dict
rotated_secret_details_info_from_dict = RotatedSecretDetailsInfo.from_dict(rotated_secret_details_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


