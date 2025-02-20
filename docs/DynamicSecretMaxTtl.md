# DynamicSecretMaxTtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**max_ttl_by_minutes** | **int** |  | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_max_ttl import DynamicSecretMaxTtl

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretMaxTtl from a JSON string
dynamic_secret_max_ttl_instance = DynamicSecretMaxTtl.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretMaxTtl.to_json())

# convert the object into a dict
dynamic_secret_max_ttl_dict = dynamic_secret_max_ttl_instance.to_dict()
# create an instance of DynamicSecretMaxTtl from a dict
dynamic_secret_max_ttl_from_dict = DynamicSecretMaxTtl.from_dict(dynamic_secret_max_ttl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


