# SignPKCS1

signPKCS1 is a command that calculates the signature of hashed data using RSASSA-PKCS1-V1_5-SIGN from RSA PKCS#1 v1.5.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the signing process | [optional] 
**hash_function** | **str** | HashFunction defines the hash function (e.g. sha-256) | [optional] 
**input_format** | **str** | Select default assumed format for the plaintext message. Currently supported options: [base64] | [optional] 
**item_id** | **int** | The item id of the key to use in the signing process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the RSA key to use in the signing process | [optional] 
**message** | **str** | The message to be signed | 
**prehashed** | **bool** | Markes that the message is already hashed | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The version of the key to use for signing | [optional] 

## Example

```python
from akeyless.models.sign_pkcs1 import SignPKCS1

# TODO update the JSON string below
json = "{}"
# create an instance of SignPKCS1 from a JSON string
sign_pkcs1_instance = SignPKCS1.from_json(json)
# print the JSON string representation of the object
print(SignPKCS1.to_json())

# convert the object into a dict
sign_pkcs1_dict = sign_pkcs1_instance.to_dict()
# create an instance of SignPKCS1 from a dict
sign_pkcs1_from_dict = SignPKCS1.from_dict(sign_pkcs1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


