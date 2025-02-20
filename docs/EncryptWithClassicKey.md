# EncryptWithClassicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The name of the key to use in the encryption process | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**plaintext** | **str** | Data to be encrypted | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | classic key version | 

## Example

```python
from akeyless.models.encrypt_with_classic_key import EncryptWithClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptWithClassicKey from a JSON string
encrypt_with_classic_key_instance = EncryptWithClassicKey.from_json(json)
# print the JSON string representation of the object
print(EncryptWithClassicKey.to_json())

# convert the object into a dict
encrypt_with_classic_key_dict = encrypt_with_classic_key_instance.to_dict()
# create an instance of EncryptWithClassicKey from a dict
encrypt_with_classic_key_from_dict = EncryptWithClassicKey.from_dict(encrypt_with_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


