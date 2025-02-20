# EmailTokenizerInfo

EmailTokenizerInfo represents a tokenizer that specifically tokenizes emails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_suffix_length** | **int** | What length of a random domain suffix to generate used only if FixedDomainSuffix is empty | [optional] 
**fixed_domain_suffix** | **str** | if FixedDomainSuffix isn&#39;t empty, it will be appended to the output | [optional] 
**keep_prefix_length** | **int** | How many letters of the plaintext to keep in the output | [optional] 

## Example

```python
from akeyless.models.email_tokenizer_info import EmailTokenizerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTokenizerInfo from a JSON string
email_tokenizer_info_instance = EmailTokenizerInfo.from_json(json)
# print the JSON string representation of the object
print(EmailTokenizerInfo.to_json())

# convert the object into a dict
email_tokenizer_info_dict = email_tokenizer_info_instance.to_dict()
# create an instance of EmailTokenizerInfo from a dict
email_tokenizer_info_from_dict = EmailTokenizerInfo.from_dict(email_tokenizer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


