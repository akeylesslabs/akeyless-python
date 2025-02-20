# UscUpdateSecretOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secret_id** | **str** |  | [optional] 
**version_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.usc_update_secret_output import UscUpdateSecretOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UscUpdateSecretOutput from a JSON string
usc_update_secret_output_instance = UscUpdateSecretOutput.from_json(json)
# print the JSON string representation of the object
print(UscUpdateSecretOutput.to_json())

# convert the object into a dict
usc_update_secret_output_dict = usc_update_secret_output_instance.to_dict()
# create an instance of UscUpdateSecretOutput from a dict
usc_update_secret_output_from_dict = UscUpdateSecretOutput.from_dict(usc_update_secret_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


