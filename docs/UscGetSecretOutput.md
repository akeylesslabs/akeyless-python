# UscGetSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_value** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from akeyless.models.usc_get_secret_output import UscGetSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UscGetSecretOutput from a JSON string
usc_get_secret_output_instance = UscGetSecretOutput.from_json(json)
# print the JSON string representation of the object
print(UscGetSecretOutput.to_json())

# convert the object into a dict
usc_get_secret_output_dict = usc_get_secret_output_instance.to_dict()
# create an instance of UscGetSecretOutput from a dict
usc_get_secret_output_from_dict = UscGetSecretOutput.from_dict(usc_get_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


