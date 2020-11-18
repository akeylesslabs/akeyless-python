# RotateKey

rotateKey is a command that rotates an existing key, creating a new version of it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_rotate** | **str** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | [optional] 
**name** | **str** | Key name | 
**rotation_interval** | **str** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


