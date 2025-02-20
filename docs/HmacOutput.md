# HmacOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 

## Example

```python
from akeyless.models.hmac_output import HmacOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HmacOutput from a JSON string
hmac_output_instance = HmacOutput.from_json(json)
# print the JSON string representation of the object
print(HmacOutput.to_json())

# convert the object into a dict
hmac_output_dict = hmac_output_instance.to_dict()
# create an instance of HmacOutput from a dict
hmac_output_from_dict = HmacOutput.from_dict(hmac_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


