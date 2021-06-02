# CreateClassicKey

CreateClassicKey is a command that creates classic key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Classic Key type; options: [AES256GCM, RSA2048] | 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**key_data** | **str** | Base64-encoded classic key value | [optional] 
**metadata** | **str** | Metadata about the classic key | [optional] 
**name** | **str** | ClassicKey name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**tags** | **list[str]** | List of the tags attached to this classic key | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


