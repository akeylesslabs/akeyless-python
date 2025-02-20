# GetTargetDetailsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**Target**](Target.md) |  | [optional] 
**value** | [**TargetTypeDetailsInput**](TargetTypeDetailsInput.md) |  | [optional] 

## Example

```python
from akeyless.models.get_target_details_output import GetTargetDetailsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetTargetDetailsOutput from a JSON string
get_target_details_output_instance = GetTargetDetailsOutput.from_json(json)
# print the JSON string representation of the object
print(GetTargetDetailsOutput.to_json())

# convert the object into a dict
get_target_details_output_dict = get_target_details_output_instance.to_dict()
# create an instance of GetTargetDetailsOutput from a dict
get_target_details_output_from_dict = GetTargetDetailsOutput.from_dict(get_target_details_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


