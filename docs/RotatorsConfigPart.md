# RotatorsConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotators** | [**List[Rotator]**](Rotator.md) |  | [optional] 

## Example

```python
from akeyless.models.rotators_config_part import RotatorsConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of RotatorsConfigPart from a JSON string
rotators_config_part_instance = RotatorsConfigPart.from_json(json)
# print the JSON string representation of the object
print(RotatorsConfigPart.to_json())

# convert the object into a dict
rotators_config_part_dict = rotators_config_part_instance.to_dict()
# create an instance of RotatorsConfigPart from a dict
rotators_config_part_from_dict = RotatorsConfigPart.from_dict(rotators_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


