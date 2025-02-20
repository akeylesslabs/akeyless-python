# RegexpTokenizerInfo

RegexpTokenizerInfo represents a general Regexp tokenization template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabet** | **str** | The Alphabet used for the tokenization | [optional] 
**decoding_template** | **str** | Transformation to perform on the decrypted data | [optional] 
**encoding_template** | **str** | Transformation to perform on the encrypted data, if the required output template doesn&#39;t match the input string The output Should still be valid for the Pattern, otherwise the secret would be able to be decrypted. | [optional] 
**pattern** | **str** | Regexp pattern to extract and deposit the text/encdata | [optional] 

## Example

```python
from akeyless.models.regexp_tokenizer_info import RegexpTokenizerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RegexpTokenizerInfo from a JSON string
regexp_tokenizer_info_instance = RegexpTokenizerInfo.from_json(json)
# print the JSON string representation of the object
print(RegexpTokenizerInfo.to_json())

# convert the object into a dict
regexp_tokenizer_info_dict = regexp_tokenizer_info_instance.to_dict()
# create an instance of RegexpTokenizerInfo from a dict
regexp_tokenizer_info_from_dict = RegexpTokenizerInfo.from_dict(regexp_tokenizer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


