# ValidateToken

validate-token is a command that validaties token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Token | [optional] 

## Example

```python
from akeyless.models.validate_token import ValidateToken

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateToken from a JSON string
validate_token_instance = ValidateToken.from_json(json)
# print the JSON string representation of the object
print(ValidateToken.to_json())

# convert the object into a dict
validate_token_dict = validate_token_instance.to_dict()
# create an instance of ValidateToken from a dict
validate_token_from_dict = ValidateToken.from_dict(validate_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


