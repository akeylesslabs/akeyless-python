# DeriveKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**salt** | **str** |  | [optional] 

## Example

```python
from akeyless.models.derive_key_output import DeriveKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveKeyOutput from a JSON string
derive_key_output_instance = DeriveKeyOutput.from_json(json)
# print the JSON string representation of the object
print(DeriveKeyOutput.to_json())

# convert the object into a dict
derive_key_output_dict = derive_key_output_instance.to_dict()
# create an instance of DeriveKeyOutput from a dict
derive_key_output_from_dict = DeriveKeyOutput.from_dict(derive_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


