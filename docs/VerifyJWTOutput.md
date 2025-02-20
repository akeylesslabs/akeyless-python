# VerifyJWTOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 

## Example

```python
from akeyless.models.verify_jwt_output import VerifyJWTOutput

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyJWTOutput from a JSON string
verify_jwt_output_instance = VerifyJWTOutput.from_json(json)
# print the JSON string representation of the object
print(VerifyJWTOutput.to_json())

# convert the object into a dict
verify_jwt_output_dict = verify_jwt_output_instance.to_dict()
# create an instance of VerifyJWTOutput from a dict
verify_jwt_output_from_dict = VerifyJWTOutput.from_dict(verify_jwt_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


