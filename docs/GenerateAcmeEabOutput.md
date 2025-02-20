# GenerateAcmeEabOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**kid** | **str** |  | [optional] 
**mac_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.generate_acme_eab_output import GenerateAcmeEabOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAcmeEabOutput from a JSON string
generate_acme_eab_output_instance = GenerateAcmeEabOutput.from_json(json)
# print the JSON string representation of the object
print(GenerateAcmeEabOutput.to_json())

# convert the object into a dict
generate_acme_eab_output_dict = generate_acme_eab_output_instance.to_dict()
# create an instance of GenerateAcmeEabOutput from a dict
generate_acme_eab_output_from_dict = GenerateAcmeEabOutput.from_dict(generate_acme_eab_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


