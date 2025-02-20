# DecryptPKCS1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Ciphertext to be decrypted in base64 encoded format | 
**display_id** | **str** | The display id of the key to use in the decryption process | [optional] 
**item_id** | **int** | The item id of the key to use in the decryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the decryption process | 
**output_format** | **str** | If specified, the output will be formatted accordingly. options: [base64] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | key version (relevant only for classic key) | [optional] 

## Example

```python
from akeyless.models.decrypt_pkcs1 import DecryptPKCS1

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptPKCS1 from a JSON string
decrypt_pkcs1_instance = DecryptPKCS1.from_json(json)
# print the JSON string representation of the object
print(DecryptPKCS1.to_json())

# convert the object into a dict
decrypt_pkcs1_dict = decrypt_pkcs1_instance.to_dict()
# create an instance of DecryptPKCS1 from a dict
decrypt_pkcs1_from_dict = DecryptPKCS1.from_dict(decrypt_pkcs1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


