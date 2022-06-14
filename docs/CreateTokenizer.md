# CreateTokenizer

createTokenizer is a command that creates a tokenizer item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabet** | **str** | Alphabet to use in regexp vaultless tokenization | [optional] 
**decryption_template** | **str** | The Decryption output template to use in regexp vaultless tokenization | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**encryption_key_name** | **str** | AES key name to use in vaultless tokenization | [optional] 
**encryption_template** | **str** | The Encryption output template to use in regexp vaultless tokenization | [optional] 
**metadata** | **str** | A metadata about the tokenizer | [optional] 
**name** | **str** | Tokenizer name | 
**pattern** | **str** | Pattern to use in regexp vaultless tokenization | [optional] 
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**template_type** | **str** | Which template type this tokenizer is used for [SSN,CreditCard,USPhoneNumber,Email,Regexp] | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**tokenizer_type** | **str** | Tokenizer type | 
**tweak_type** | **str** | The tweak type to use in vaultless tokenization [Supplied, Generated, Internal, Masking] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


