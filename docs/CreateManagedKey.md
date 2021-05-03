# CreateManagedKey

CreateManagedKey is a command that creates managed key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Managed Key type; options: [AES256GCM, RSA2048] | 
**managed_key_value** | **str** | Base64-encoded managed key value | [optional] 
**metadata** | **str** | Metadata about the managed key | [optional] 
**name** | **str** | ManagedKey name | 
**protection_key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**tags** | **list[str]** | List of the tags attached to this managed key | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


