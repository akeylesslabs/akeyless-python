# EsmUpdateSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secret_id** | **str** |  | [optional] 
**version_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.esm_update_secret_output import EsmUpdateSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EsmUpdateSecretOutput from a JSON string
esm_update_secret_output_instance = EsmUpdateSecretOutput.from_json(json)
# print the JSON string representation of the object
print(EsmUpdateSecretOutput.to_json())

# convert the object into a dict
esm_update_secret_output_dict = esm_update_secret_output_instance.to_dict()
# create an instance of EsmUpdateSecretOutput from a dict
esm_update_secret_output_from_dict = EsmUpdateSecretOutput.from_dict(esm_update_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


