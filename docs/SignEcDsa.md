# SignEcDsa

signEcDsa Calculates the signature of a given message using ECDSA and a sha hash algorithm matching the key size
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**display_id** | **str** | The display id of the EC key to use for the signing process | [optional] 
**item_id** | **int** | The item id of the EC key to use for the signing process | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the EC key to use for the signing process | [optional] 
**message** | **str** | The input message to sign in a base64 format | 
**prehashed** | **bool** | Markes that the message is already hashed | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The version of the key to use for signing | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


