# RotateKeyOutput

RotateKeyOutput defines output of RotateKey operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classic_key_gw_url** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**new_item_version** | **int** |  | [optional] 
**next_rotation_date** | **datetime** |  | [optional] 

## Example

```python
from akeyless.models.rotate_key_output import RotateKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RotateKeyOutput from a JSON string
rotate_key_output_instance = RotateKeyOutput.from_json(json)
# print the JSON string representation of the object
print(RotateKeyOutput.to_json())

# convert the object into a dict
rotate_key_output_dict = rotate_key_output_instance.to_dict()
# create an instance of RotateKeyOutput from a dict
rotate_key_output_from_dict = RotateKeyOutput.from_dict(rotate_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


