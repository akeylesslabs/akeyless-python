# VerifyPKCS1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the verification process | [optional] 
**hash_function** | **str** | HashFunction defines the hash function (e.g. sha-256) | [optional] 
**input_format** | **str** | Select default assumed format for the plaintext message. Currently supported options: [base64] | [optional] 
**item_id** | **int** | The item id of the key to use in the verification process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the RSA key to use in the verification process | 
**message** | **str** | The message to be verified | 
**prehashed** | **bool** | Markes that the message is already hashed | [optional] 
**signature** | **str** | The message&#39;s signature | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | The version of the key to use for verification | [optional] 

## Example

```python
from akeyless.models.verify_pkcs1 import VerifyPKCS1

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPKCS1 from a JSON string
verify_pkcs1_instance = VerifyPKCS1.from_json(json)
# print the JSON string representation of the object
print(VerifyPKCS1.to_json())

# convert the object into a dict
verify_pkcs1_dict = verify_pkcs1_instance.to_dict()
# create an instance of VerifyPKCS1 from a dict
verify_pkcs1_from_dict = VerifyPKCS1.from_dict(verify_pkcs1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


