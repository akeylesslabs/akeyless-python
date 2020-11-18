# CreateKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048] | 
**customer_frg_id** | **str** | The customer fragment ID that will be used to create the key (if empty, the key will be created independently of a customer fragment) | [optional] 
**metadata** | **str** | Metadata about the key | [optional] 
**name** | **str** | Key name | 
**split_level** | **int** | The number of fragments that the item will be split into (not includes customer fragment) | [optional] [default to 2]
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


