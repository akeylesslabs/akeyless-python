# KMIPEnvironmentCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **List[int]** |  | [optional] 
**root** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_environment_create_response import KMIPEnvironmentCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KMIPEnvironmentCreateResponse from a JSON string
kmip_environment_create_response_instance = KMIPEnvironmentCreateResponse.from_json(json)
# print the JSON string representation of the object
print(KMIPEnvironmentCreateResponse.to_json())

# convert the object into a dict
kmip_environment_create_response_dict = kmip_environment_create_response_instance.to_dict()
# create an instance of KMIPEnvironmentCreateResponse from a dict
kmip_environment_create_response_from_dict = KMIPEnvironmentCreateResponse.from_dict(kmip_environment_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


