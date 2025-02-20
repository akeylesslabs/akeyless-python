# EsmCreateSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** |  | [optional] 
**version_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.esm_create_secret_output import EsmCreateSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EsmCreateSecretOutput from a JSON string
esm_create_secret_output_instance = EsmCreateSecretOutput.from_json(json)
# print the JSON string representation of the object
print(EsmCreateSecretOutput.to_json())

# convert the object into a dict
esm_create_secret_output_dict = esm_create_secret_output_instance.to_dict()
# create an instance of EsmCreateSecretOutput from a dict
esm_create_secret_output_from_dict = EsmCreateSecretOutput.from_dict(esm_create_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


