# CreateClassicKey

CreateClassicKey is a command that creates classic key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Classic Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048, RSA3072, RSA4096, EC256, EC384] | 
**cert_file_data** | **str** | Certificate in a PEM format. | [optional] 
**key_data** | **str** | Base64-encoded classic key value | [optional] 
**key_operations** | **list[str]** | A list of allowed operations for the key (required for azure targets) | [optional] 
**metadata** | **str** | Metadata about the classic key | [optional] 
**name** | **str** | ClassicKey name | 
**protection_key_name** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**tags** | **list[str]** | List of the tags attached to this classic key | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**vault_name** | **str** | Name of the vault used (required for azure targets) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


