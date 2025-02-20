# DecryptFileOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**plain_text** | **str** |  | [optional] 

## Example

```python
from akeyless.models.decrypt_file_output import DecryptFileOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptFileOutput from a JSON string
decrypt_file_output_instance = DecryptFileOutput.from_json(json)
# print the JSON string representation of the object
print(DecryptFileOutput.to_json())

# convert the object into a dict
decrypt_file_output_dict = decrypt_file_output_instance.to_dict()
# create an instance of DecryptFileOutput from a dict
decrypt_file_output_from_dict = DecryptFileOutput.from_dict(decrypt_file_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


