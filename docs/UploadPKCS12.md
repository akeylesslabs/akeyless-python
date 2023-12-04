# UploadPKCS12

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_frg_id** | **str** | The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**_in** | **str** | PKCS#12 input file (private key and certificate only) | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Name of key to be created | 
**passphrase** | **str** | Passphrase to unlock the pkcs#12 bundle | 
**split_level** | **int** | The number of fragments that the item will be split into | [optional] [default to 3]
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


