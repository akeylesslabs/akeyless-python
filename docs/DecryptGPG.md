# DecryptGPG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Ciphertext to be decrypted | 
**display_id** | **str** | The display id of the key to use in the decryption process | [optional] 
**input_format** | **str** | Select default assumed format for the ciphertext. Currently supported options: [base64,raw] | [optional] [default to 'base64']
**item_id** | **int** | The item id of the key to use in the decryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the decryption process | 
**output_format** | **str** | If specified, the output will be formatted accordingly. options: [base64] | [optional] 
**passphrase** | **str** | Passphrase that was used to generate the key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.decrypt_gpg import DecryptGPG

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptGPG from a JSON string
decrypt_gpg_instance = DecryptGPG.from_json(json)
# print the JSON string representation of the object
print(DecryptGPG.to_json())

# convert the object into a dict
decrypt_gpg_dict = decrypt_gpg_instance.to_dict()
# create an instance of DecryptGPG from a dict
decrypt_gpg_from_dict = DecryptGPG.from_dict(decrypt_gpg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


