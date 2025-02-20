# SignJWTOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 

## Example

```python
from akeyless.models.sign_jwt_output import SignJWTOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SignJWTOutput from a JSON string
sign_jwt_output_instance = SignJWTOutput.from_json(json)
# print the JSON string representation of the object
print(SignJWTOutput.to_json())

# convert the object into a dict
sign_jwt_output_dict = sign_jwt_output_instance.to_dict()
# create an instance of SignJWTOutput from a dict
sign_jwt_output_from_dict = SignJWTOutput.from_dict(sign_jwt_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


