# VerifyDataWithClassicKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data | 
**display_id** | **str** | The display id of the key to use in the verification process | [optional] 
**hashed** | **bool** | Defines whether the data should be hashed as part of the signing. If true, the data will not be hashed | [optional] [default to False]
**hashing_method** | **str** | HashingMethod | [optional] [default to 'SHA256']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | The name of the key to use in the verification process | 
**signature** | **str** | The data&#39;s signature in a Base64 format. | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


