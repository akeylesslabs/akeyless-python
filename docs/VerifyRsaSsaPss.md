# VerifyRsaSsaPss

verifyRsaSsaPss is a command that Verifies an rsassa-pss signature
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the RSA key to use in the verification process | [optional] 
**hash_function** | **str** | HashFunction defines the hash function (e.g. sha-256) | [optional] 
**item_id** | **int** | The item id of the RSA key to use in the verification process | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the RSA key to use in the verification process | [optional] 
**message** | **str** | The input message to verify in a base64 format | 
**signature** | **str** | The message&#39;s signature | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


