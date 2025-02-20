# EncryptGPG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the encryption process | [optional] 
**input_format** | **str** | If specified, the plaintext input is assumed to be formatted accordingly. Current supported options: [base64] | [optional] 
**item_id** | **int** | The item id of the key to use in the encryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the encryption process | 
**plaintext** | **str** | Data to be encrypted | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.encrypt_gpg import EncryptGPG

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptGPG from a JSON string
encrypt_gpg_instance = EncryptGPG.from_json(json)
# print the JSON string representation of the object
print(EncryptGPG.to_json())

# convert the object into a dict
encrypt_gpg_dict = encrypt_gpg_instance.to_dict()
# create an instance of EncryptGPG from a dict
encrypt_gpg_from_dict = EncryptGPG.from_dict(encrypt_gpg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


