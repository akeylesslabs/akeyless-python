# DynamicSecretList

dynamicSecretList is a command that returns a list of dynamic secrets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_list import DynamicSecretList

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretList from a JSON string
dynamic_secret_list_instance = DynamicSecretList.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretList.to_json())

# convert the object into a dict
dynamic_secret_list_dict = dynamic_secret_list_instance.to_dict()
# create an instance of DynamicSecretList from a dict
dynamic_secret_list_from_dict = DynamicSecretList.from_dict(dynamic_secret_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


