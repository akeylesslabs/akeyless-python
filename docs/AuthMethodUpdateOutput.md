# AuthMethodUpdateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**prv_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.auth_method_update_output import AuthMethodUpdateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodUpdateOutput from a JSON string
auth_method_update_output_instance = AuthMethodUpdateOutput.from_json(json)
# print the JSON string representation of the object
print(AuthMethodUpdateOutput.to_json())

# convert the object into a dict
auth_method_update_output_dict = auth_method_update_output_instance.to_dict()
# create an instance of AuthMethodUpdateOutput from a dict
auth_method_update_output_from_dict = AuthMethodUpdateOutput.from_dict(auth_method_update_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


