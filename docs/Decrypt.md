# Decrypt

decrypt is a command that decrypts ciphertext into plaintext by using an AES key.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Ciphertext to be decrypted in base64 encoded format | [optional] 
**display_id** | **str** | The display id of the key to use in the decryption process | [optional] 
**encryption_context** | **dict(str, str)** | The encryption context. If this was specified in the encrypt command, it must be specified here or the decryption operation will fail | [optional] 
**item_id** | **int** | The item id of the key to use in the decryption process | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the decryption process | 
**output_format** | **str** | If specified, the output will be formatted accordingly. options: [base64] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | key version (relevant only for classic key) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


