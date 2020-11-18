# CreateDynamicSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of a key that used to encrypt the dynamic secret values (if empty, the account default protectionKey key will be used) | [optional] 
**metadata** | **str** | Metadata about the dynamic secret | [optional] [default to 'None']
**name** | **str** | Dynamic secret name | 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


