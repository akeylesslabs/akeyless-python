# ExportClassicKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_pem** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**ssh** | **str** |  | [optional] 
**wrapping_iv** | **str** |  | [optional] 

## Example

```python
from akeyless.models.export_classic_key_output import ExportClassicKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportClassicKeyOutput from a JSON string
export_classic_key_output_instance = ExportClassicKeyOutput.from_json(json)
# print the JSON string representation of the object
print(ExportClassicKeyOutput.to_json())

# convert the object into a dict
export_classic_key_output_dict = export_classic_key_output_instance.to_dict()
# create an instance of ExportClassicKeyOutput from a dict
export_classic_key_output_from_dict = ExportClassicKeyOutput.from_dict(export_classic_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


