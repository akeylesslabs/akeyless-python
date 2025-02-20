# LastConfigChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_k8s_auths_change** | [**K8SAuthsConfigLastChange**](K8SAuthsConfigLastChange.md) |  | [optional] 
**last_migrations_change** | [**MigrationsConfigLastChange**](MigrationsConfigLastChange.md) |  | [optional] 

## Example

```python
from akeyless.models.last_config_change import LastConfigChange

# TODO update the JSON string below
json = "{}"
# create an instance of LastConfigChange from a JSON string
last_config_change_instance = LastConfigChange.from_json(json)
# print the JSON string representation of the object
print(LastConfigChange.to_json())

# convert the object into a dict
last_config_change_dict = last_config_change_instance.to_dict()
# create an instance of LastConfigChange from a dict
last_config_change_from_dict = LastConfigChange.from_dict(last_config_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


