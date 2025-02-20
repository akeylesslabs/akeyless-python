# ResetAuthMethodAccessKeyOutput

ResetAuthMethodAccessKeyOutput defines output of ResetAuthMethodAccessKey operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.reset_auth_method_access_key_output import ResetAuthMethodAccessKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ResetAuthMethodAccessKeyOutput from a JSON string
reset_auth_method_access_key_output_instance = ResetAuthMethodAccessKeyOutput.from_json(json)
# print the JSON string representation of the object
print(ResetAuthMethodAccessKeyOutput.to_json())

# convert the object into a dict
reset_auth_method_access_key_output_dict = reset_auth_method_access_key_output_instance.to_dict()
# create an instance of ResetAuthMethodAccessKeyOutput from a dict
reset_auth_method_access_key_output_from_dict = ResetAuthMethodAccessKeyOutput.from_dict(reset_auth_method_access_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


