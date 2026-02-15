# PolicyUpdateKeys

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_algorithms** | **list[str]** | Specify allowed key algorithms (e.g., [RSA2048,AES128GCM]) | [optional] 
**allowed_key_names** | **list[str]** | Specify allowed protection key names. To enforce using the account&#39;s default protection key, use &#39;default-account-key&#39; | [optional] 
**allowed_key_types** | **list[str]** | Specify allowed key protection types (dfc, classic-key) | [optional] 
**id** | **str** | Policy id | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_rotation_interval_days** | **int** | Set the maximum rotation interval for automatic key rotation. | [optional] 
**object_types** | **list[str]** | The object type this policy will apply to (items, targets) | [optional] 
**path** | **str** | The path the policy refers to | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


