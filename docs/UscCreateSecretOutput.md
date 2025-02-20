# UscCreateSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** |  | [optional] 
**version_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.usc_create_secret_output import UscCreateSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UscCreateSecretOutput from a JSON string
usc_create_secret_output_instance = UscCreateSecretOutput.from_json(json)
# print the JSON string representation of the object
print(UscCreateSecretOutput.to_json())

# convert the object into a dict
usc_create_secret_output_dict = usc_create_secret_output_instance.to_dict()
# create an instance of UscCreateSecretOutput from a dict
usc_create_secret_output_from_dict = UscCreateSecretOutput.from_dict(usc_create_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


