# DecryptFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enc_context** | **dict(str, str)** | The encryption context. If this was specified in the encrypt command, it must be specified here or the decryption operation will fail | [optional] 
**input_file** | **str** | Path to the file to be decrypted. If not provided, the content will be taken from stdin | 
**key_name** | **str** | The name of the key to use in the decryption process | 
**output_file_path** | **str** | Path to the output file. If not provided, the output will be sent to stdout | [optional] 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


