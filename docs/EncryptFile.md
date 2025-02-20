# EncryptFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** | The display id of the key to use in the encryption process | [optional] 
**var_in** | **str** | Path to the file to be encrypted. If not provided, the content will be taken from stdin | 
**item_id** | **int** | The item id of the key to use in the encryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the encryption process | 
**out** | **str** | Path to the output file. If not provided, the output will be sent to stdout | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.encrypt_file import EncryptFile

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptFile from a JSON string
encrypt_file_instance = EncryptFile.from_json(json)
# print the JSON string representation of the object
print(EncryptFile.to_json())

# convert the object into a dict
encrypt_file_dict = encrypt_file_instance.to_dict()
# create an instance of EncryptFile from a dict
encrypt_file_from_dict = EncryptFile.from_dict(encrypt_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


