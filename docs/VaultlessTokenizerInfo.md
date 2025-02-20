# VaultlessTokenizerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_tokenizer_info** | [**EmailTokenizerInfo**](EmailTokenizerInfo.md) |  | [optional] 
**key_name** | **str** |  | [optional] 
**regexp_tokenizer_info** | [**RegexpTokenizerInfo**](RegexpTokenizerInfo.md) |  | [optional] 
**template_type** | **str** |  | [optional] 
**tweak** | **str** | Tweak used in the case of internal tweak type | [optional] 
**tweak_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.vaultless_tokenizer_info import VaultlessTokenizerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VaultlessTokenizerInfo from a JSON string
vaultless_tokenizer_info_instance = VaultlessTokenizerInfo.from_json(json)
# print the JSON string representation of the object
print(VaultlessTokenizerInfo.to_json())

# convert the object into a dict
vaultless_tokenizer_info_dict = vaultless_tokenizer_info_instance.to_dict()
# create an instance of VaultlessTokenizerInfo from a dict
vaultless_tokenizer_info_from_dict = VaultlessTokenizerInfo.from_dict(vaultless_tokenizer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


