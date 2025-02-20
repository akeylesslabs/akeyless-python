# GetRSAPublicOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pem** | **str** |  | [optional] 
**raw** | **str** |  | [optional] 
**ssh** | **str** |  | [optional] 

## Example

```python
from akeyless.models.get_rsa_public_output import GetRSAPublicOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetRSAPublicOutput from a JSON string
get_rsa_public_output_instance = GetRSAPublicOutput.from_json(json)
# print the JSON string representation of the object
print(GetRSAPublicOutput.to_json())

# convert the object into a dict
get_rsa_public_output_dict = get_rsa_public_output_instance.to_dict()
# create an instance of GetRSAPublicOutput from a dict
get_rsa_public_output_from_dict = GetRSAPublicOutput.from_dict(get_rsa_public_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


