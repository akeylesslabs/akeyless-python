# EsmGetSecretOutput


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
from akeyless.models.esm_get_secret_output import EsmGetSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EsmGetSecretOutput from a JSON string
esm_get_secret_output_instance = EsmGetSecretOutput.from_json(json)
# print the JSON string representation of the object
print(EsmGetSecretOutput.to_json())

# convert the object into a dict
esm_get_secret_output_dict = esm_get_secret_output_instance.to_dict()
# create an instance of EsmGetSecretOutput from a dict
esm_get_secret_output_from_dict = EsmGetSecretOutput.from_dict(esm_get_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


