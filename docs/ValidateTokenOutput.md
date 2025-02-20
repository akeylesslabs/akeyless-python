# ValidateTokenOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **str** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**last_rotate** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from akeyless.models.validate_token_output import ValidateTokenOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTokenOutput from a JSON string
validate_token_output_instance = ValidateTokenOutput.from_json(json)
# print the JSON string representation of the object
print(ValidateTokenOutput.to_json())

# convert the object into a dict
validate_token_output_dict = validate_token_output_instance.to_dict()
# create an instance of ValidateTokenOutput from a dict
validate_token_output_from_dict = ValidateTokenOutput.from_dict(validate_token_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


