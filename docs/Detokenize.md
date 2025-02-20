# Detokenize

detokenize is a command that decrypts text with a tokenizer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Data to be decrypted | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**tokenizer_name** | **str** | The name of the tokenizer to use in the decryption process | 
**tweak** | **str** | Base64 encoded tweak for vaultless encryption | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.detokenize import Detokenize

# TODO update the JSON string below
json = "{}"
# create an instance of Detokenize from a JSON string
detokenize_instance = Detokenize.from_json(json)
# print the JSON string representation of the object
print(Detokenize.to_json())

# convert the object into a dict
detokenize_dict = detokenize_instance.to_dict()
# create an instance of Detokenize from a dict
detokenize_from_dict = Detokenize.from_dict(detokenize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


