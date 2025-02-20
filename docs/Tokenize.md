# Tokenize

tokenize is a command that encrypts text with a tokenizer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**plaintext** | **str** | Data to be encrypted | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**tokenizer_name** | **str** | The name of the tokenizer to use in the encryption process | 
**tweak** | **str** | Base64 encoded tweak for vaultless encryption | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.tokenize import Tokenize

# TODO update the JSON string below
json = "{}"
# create an instance of Tokenize from a JSON string
tokenize_instance = Tokenize.from_json(json)
# print the JSON string representation of the object
print(Tokenize.to_json())

# convert the object into a dict
tokenize_dict = tokenize_instance.to_dict()
# create an instance of Tokenize from a dict
tokenize_from_dict = Tokenize.from_dict(tokenize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


