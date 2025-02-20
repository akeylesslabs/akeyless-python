# Rotator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**last_error** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rotation_interval** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.rotator import Rotator

# TODO update the JSON string below
json = "{}"
# create an instance of Rotator from a JSON string
rotator_instance = Rotator.from_json(json)
# print the JSON string representation of the object
print(Rotator.to_json())

# convert the object into a dict
rotator_dict = rotator_instance.to_dict()
# create an instance of Rotator from a dict
rotator_from_dict = Rotator.from_dict(rotator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


