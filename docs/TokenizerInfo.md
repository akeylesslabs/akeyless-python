# TokenizerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vaultless_tokenizer_info** | [**VaultlessTokenizerInfo**](VaultlessTokenizerInfo.md) |  | [optional] 

## Example

```python
from akeyless.models.tokenizer_info import TokenizerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizerInfo from a JSON string
tokenizer_info_instance = TokenizerInfo.from_json(json)
# print the JSON string representation of the object
print(TokenizerInfo.to_json())

# convert the object into a dict
tokenizer_info_dict = tokenizer_info_instance.to_dict()
# create an instance of TokenizerInfo from a dict
tokenizer_info_from_dict = TokenizerInfo.from_dict(tokenizer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


