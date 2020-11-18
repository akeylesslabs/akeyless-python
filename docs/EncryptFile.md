# EncryptFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_context** | **dict(str, str)** | name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the decrypt command or decryption will fail | [optional] 
**_in** | **str** | Path to the file to be encrypted. If not provided, the content will be taken from stdin | 
**key_name** | **str** | The name of the key to use in the encryption process | 
**out** | **str** | Path to the output file. If not provided, the output will be sent to stdout | [optional] 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


