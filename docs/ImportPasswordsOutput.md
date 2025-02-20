# ImportPasswordsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported** | **int** |  | [optional] 
**passwords_in_file** | **int** |  | [optional] 
**successfully_parsed** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 

## Example

```python
from akeyless.models.import_passwords_output import ImportPasswordsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPasswordsOutput from a JSON string
import_passwords_output_instance = ImportPasswordsOutput.from_json(json)
# print the JSON string representation of the object
print(ImportPasswordsOutput.to_json())

# convert the object into a dict
import_passwords_output_dict = import_passwords_output_instance.to_dict()
# create an instance of ImportPasswordsOutput from a dict
import_passwords_output_from_dict = ImportPasswordsOutput.from_dict(import_passwords_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


