# Decrypt

decrypt is a command that decrypts ciphertext into plaintext by using an AES key.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Ciphertext to be decrypted in base64 encoded format | 
**display_id** | **str** | The display id of the key to use in the decryption process | [optional] 
**encryption_context** | **dict(str, str)** | The encryption context. If this was specified in the encrypt command, it must be specified here or the decryption operation will fail | [optional] 
**key_name** | **str** | The name of the key to use in the decryption process | [optional] 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


