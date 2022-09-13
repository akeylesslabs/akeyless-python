# UpdateRotationSettings

updateRotationSettings is a command that updates rotations settings of an existing key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_rotate** | **bool** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | 
**json** | **bool** | Set output format to JSON | [optional] 
**name** | **str** | Key name | 
**rotation_interval** | **int** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


