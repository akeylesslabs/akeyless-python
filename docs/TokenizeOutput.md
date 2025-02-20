# TokenizeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**tweak** | **str** |  | [optional] 

## Example

```python
from akeyless.models.tokenize_output import TokenizeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizeOutput from a JSON string
tokenize_output_instance = TokenizeOutput.from_json(json)
# print the JSON string representation of the object
print(TokenizeOutput.to_json())

# convert the object into a dict
tokenize_output_dict = tokenize_output_instance.to_dict()
# create an instance of TokenizeOutput from a dict
tokenize_output_from_dict = TokenizeOutput.from_dict(tokenize_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


