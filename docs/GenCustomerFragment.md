# GenCustomerFragment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the object | [optional] 
**hsm_key_label** | **str** | The label of the hsm key to use for customer fragment operations (relevant for hsm wrap customer fragments) | [optional] 
**hsm_provider** | **str** | The HSM provider to use for hsm wrap customer fragments | [optional] [default to 'pkcs11']
**hsm_wrap_alg** | **str** | The HSM wrap algorithm to use for hsm_wrap_encrypt  default for hsm_wrap_encrypt: rsa-oaep-sha256 | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Customer fragment name | [optional] 
**type** | **str** | Customer fragment type [standard/hsm_wrap_hmac/hsm_wrap_encrypt/hsm_secured] | [optional] [default to 'standard']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


