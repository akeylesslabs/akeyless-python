# DecryptWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Ciphertext to be decrypted in base64 encoded format | 
**display_id** | **str** | The name of the key to use in the encryption process | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.decrypt_with_classic_key import DecryptWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptWithClassicKey from a JSON string
decrypt_with_classic_key_instance = DecryptWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(DecryptWithClassicKey.to_json())

# convert the object into a dict
decrypt_with_classic_key_dict = decrypt_with_classic_key_instance.to_dict()
# create an instance of DecryptWithClassicKey from a dict
decrypt_with_classic_key_from_dict = DecryptWithClassicKey.from_dict(decrypt_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


