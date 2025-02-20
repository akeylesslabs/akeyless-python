# AuthMethodCreateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prv_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.auth_method_create_output import AuthMethodCreateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodCreateOutput from a JSON string
auth_method_create_output_instance = AuthMethodCreateOutput.from_json(json)
# print the JSON string representation of the object
print(AuthMethodCreateOutput.to_json())

# convert the object into a dict
auth_method_create_output_dict = auth_method_create_output_instance.to_dict()
# create an instance of AuthMethodCreateOutput from a dict
auth_method_create_output_from_dict = AuthMethodCreateOutput.from_dict(auth_method_create_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


