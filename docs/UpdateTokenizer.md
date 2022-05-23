# UpdateTokenizer

updateTokenizer is a command that updates a tokenizer item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**alphabet** | **str** | Alphabet to use in regexp vaultless tokenization | [optional] 
**decryption_template** | **str** | The Decryption output template to use in regexp vaultless tokenization | [optional] 
**encryption_key_name** | **str** | AES key name to use in vaultless tokenization | [optional] 
**encryption_template** | **str** | The Encryption output template to use in regexp vaultless tokenization | [optional] 
**name** | **str** | Current item name | 
**new_metadata** | **str** | New item metadata | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**pattern** | **str** | Pattern to use in regexp vaultless tokenization | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**template_type** | **str** | Which template type this tokenizer is used for [SSN,CreditCard,USPhoneNumber,Email,Regexp] | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**tokenizer_type** | **str** | Tokenizer type | 
**tweak_type** | **str** | The tweak type to use in vaultless tokenization [Supplied, Generated, Internal, Masking] | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


