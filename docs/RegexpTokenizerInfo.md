# RegexpTokenizerInfo

RegexpTokenizerInfo represents a general Regexp tokenization template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabet** | **str** | The Alphabet used for the tokenization | [optional] 
**decryption_template** | **str** | Transformation to perform on the decrypted data | [optional] 
**encryption_template** | **str** | Transformation to perform on the encrypted data, if the required output template doesn&#39;t match the input string The output Should still be valid for the Pattern, otherwise the secret would be able to be decrypted. | [optional] 
**pattern** | **str** | Regexp pattern to extract and deposit the text/encdata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


