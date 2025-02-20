# CreateAuthMethodK8SOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**prv_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_auth_method_k8_s_output import CreateAuthMethodK8SOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodK8SOutput from a JSON string
create_auth_method_k8_s_output_instance = CreateAuthMethodK8SOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodK8SOutput.to_json())

# convert the object into a dict
create_auth_method_k8_s_output_dict = create_auth_method_k8_s_output_instance.to_dict()
# create an instance of CreateAuthMethodK8SOutput from a dict
create_auth_method_k8_s_output_from_dict = CreateAuthMethodK8SOutput.from_dict(create_auth_method_k8_s_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


