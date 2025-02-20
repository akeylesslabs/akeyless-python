# K8SAuthsConfigLastChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_k8s_auths_ids** | **List[str]** |  | [optional] 
**created_k8s_auths_ids** | **List[str]** |  | [optional] 
**deleted_k8s_auths_ids** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.k8_s_auths_config_last_change import K8SAuthsConfigLastChange

# TODO update the JSON string below
json = "{}"
# create an instance of K8SAuthsConfigLastChange from a JSON string
k8_s_auths_config_last_change_instance = K8SAuthsConfigLastChange.from_json(json)
# print the JSON string representation of the object
print(K8SAuthsConfigLastChange.to_json())

# convert the object into a dict
k8_s_auths_config_last_change_dict = k8_s_auths_config_last_change_instance.to_dict()
# create an instance of K8SAuthsConfigLastChange from a dict
k8_s_auths_config_last_change_from_dict = K8SAuthsConfigLastChange.from_dict(k8_s_auths_config_last_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


