# CreateAuthMethodOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_auth_method_output import CreateAuthMethodOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodOutput from a JSON string
create_auth_method_output_instance = CreateAuthMethodOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodOutput.to_json())

# convert the object into a dict
create_auth_method_output_dict = create_auth_method_output_instance.to_dict()
# create an instance of CreateAuthMethodOutput from a dict
create_auth_method_output_from_dict = CreateAuthMethodOutput.from_dict(create_auth_method_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


