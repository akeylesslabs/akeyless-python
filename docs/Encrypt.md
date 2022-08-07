# Encrypt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the encryption process | [optional] 
**encryption_context** | **dict(str, str)** | name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the decrypt command or decryption will fail | [optional] 
**item_id** | **int** | The item id of the key to use in the encryption process | [optional] 
**key_name** | **str** | The name of the key to use in the encryption process | 
**plaintext** | **str** | Data to be encrypted | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


