# ConfigureOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.configure_output import ConfigureOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureOutput from a JSON string
configure_output_instance = ConfigureOutput.from_json(json)
# print the JSON string representation of the object
print(ConfigureOutput.to_json())

# convert the object into a dict
configure_output_dict = configure_output_instance.to_dict()
# create an instance of ConfigureOutput from a dict
configure_output_from_dict = ConfigureOutput.from_dict(configure_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


