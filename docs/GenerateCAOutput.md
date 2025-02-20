# GenerateCAOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intermediate_certificate_name** | **str** |  | [optional] 
**intermediate_issuer_name** | **str** |  | [optional] 
**intermediate_key_name** | **str** |  | [optional] 
**root_certificate_name** | **str** |  | [optional] 
**root_issuer_name** | **str** |  | [optional] 
**root_key_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.generate_ca_output import GenerateCAOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCAOutput from a JSON string
generate_ca_output_instance = GenerateCAOutput.from_json(json)
# print the JSON string representation of the object
print(GenerateCAOutput.to_json())

# convert the object into a dict
generate_ca_output_dict = generate_ca_output_instance.to_dict()
# create an instance of GenerateCAOutput from a dict
generate_ca_output_from_dict = GenerateCAOutput.from_dict(generate_ca_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


