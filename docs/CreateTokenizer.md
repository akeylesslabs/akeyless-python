# CreateTokenizer

createTokenizer is a command that creates a tokenizer item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabet** | **str** | Alphabet to use in regexp vaultless tokenization | [optional] 
**decoding_template** | **str** | The Decoding output template to use in regexp vaultless tokenization | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**encoding_template** | **str** | The Encoding output template to use in regexp vaultless tokenization | [optional] 
**encryption_key_name** | **str** | AES key name to use in vaultless tokenization | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Tokenizer name | 
**pattern** | **str** | Pattern to use in regexp vaultless tokenization | [optional] 
**tag** | **List[str]** | List of the tags attached to this key | [optional] 
**template_type** | **str** | Which template type this tokenizer is used for [SSN,CreditCard,USPhoneNumber,Email,Regexp] | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**tokenizer_type** | **str** | Tokenizer type | [default to 'vaultless']
**tweak_type** | **str** | The tweak type to use in vaultless tokenization [Supplied, Generated, Internal, Masking] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_tokenizer import CreateTokenizer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenizer from a JSON string
create_tokenizer_instance = CreateTokenizer.from_json(json)
# print the JSON string representation of the object
print(CreateTokenizer.to_json())

# convert the object into a dict
create_tokenizer_dict = create_tokenizer_instance.to_dict()
# create an instance of CreateTokenizer from a dict
create_tokenizer_from_dict = CreateTokenizer.from_dict(create_tokenizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


