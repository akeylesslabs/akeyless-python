# UploadRSA

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Key type. options: [RSA1024, RSA2048, RSA3072, RSA4096] | 
**cert_file_data** | **str** | Certificate in a PEM format. | [optional] 
**customer_frg_id** | **str** | The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Name of key to be created | 
**overwrite** | **str** | When the overwrite flag is set, this command will only update an existing key [true/false] | [optional] [default to 'false']
**rsa_file_data** | **str** | RSA private key data, base64 encoded | [optional] 
**split_level** | **int** | The number of fragments that the item will be split into | [optional] [default to 3]
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


