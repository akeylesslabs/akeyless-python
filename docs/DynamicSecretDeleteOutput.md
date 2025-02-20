# DynamicSecretDeleteOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_secret_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_delete_output import DynamicSecretDeleteOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretDeleteOutput from a JSON string
dynamic_secret_delete_output_instance = DynamicSecretDeleteOutput.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretDeleteOutput.to_json())

# convert the object into a dict
dynamic_secret_delete_output_dict = dynamic_secret_delete_output_instance.to_dict()
# create an instance of DynamicSecretDeleteOutput from a dict
dynamic_secret_delete_output_from_dict = DynamicSecretDeleteOutput.from_dict(dynamic_secret_delete_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


