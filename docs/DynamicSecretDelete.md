# DynamicSecretDelete

dynamicSecretDelete is a command that deletes dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_delete import DynamicSecretDelete

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretDelete from a JSON string
dynamic_secret_delete_instance = DynamicSecretDelete.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretDelete.to_json())

# convert the object into a dict
dynamic_secret_delete_dict = dynamic_secret_delete_instance.to_dict()
# create an instance of DynamicSecretDelete from a dict
dynamic_secret_delete_from_dict = DynamicSecretDelete.from_dict(dynamic_secret_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


