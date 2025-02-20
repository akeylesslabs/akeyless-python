# DecryptFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cyphertext_header** | **str** |  | [optional] 
**display_id** | **str** | The display id of the key to use in the decryption process | [optional] 
**var_in** | **str** | Path to the file to be decrypted. If not provided, the content will be taken from stdin | 
**item_id** | **int** | The item id of the key to use in the decryption process | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_name** | **str** | The name of the key to use in the decryption process | 
**out** | **str** | Path to the output file. If not provided, the output will be sent to stdout | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | key version (relevant only for classic key) | [optional] 

## Example

```python
from akeyless.models.decrypt_file import DecryptFile

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptFile from a JSON string
decrypt_file_instance = DecryptFile.from_json(json)
# print the JSON string representation of the object
print(DecryptFile.to_json())

# convert the object into a dict
decrypt_file_dict = decrypt_file_instance.to_dict()
# create an instance of DecryptFile from a dict
decrypt_file_from_dict = DecryptFile.from_dict(decrypt_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


