# DynamicSecretUpdateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_secret_details** | [**DSProducerDetails**](DSProducerDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_update_output import DynamicSecretUpdateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretUpdateOutput from a JSON string
dynamic_secret_update_output_instance = DynamicSecretUpdateOutput.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretUpdateOutput.to_json())

# convert the object into a dict
dynamic_secret_update_output_dict = dynamic_secret_update_output_instance.to_dict()
# create an instance of DynamicSecretUpdateOutput from a dict
dynamic_secret_update_output_from_dict = DynamicSecretUpdateOutput.from_dict(dynamic_secret_update_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


