# UploadPKCS12

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_frg_id** | **str** | The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment) | [optional] 
**_in** | **str** | PKCS#12 input file (private key and certificate only) | 
**metadata** | **str** | A metadata about the key | [optional] 
**name** | **str** | Name of key to be created | 
**passphrase** | **str** | Passphrase to unlock the pkcs#12 bundle | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**split_level** | **int** | The number of fragments that the item will be split into | [optional] [default to 2]
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


