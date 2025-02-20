# KubeConfigValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**clusters** | [**List[KubeconfigNamedCluster]**](KubeconfigNamedCluster.md) |  | [optional] 
**contexts** | [**List[KubeconfigNamedContext]**](KubeconfigNamedContext.md) |  | [optional] 
**current_context** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**users** | [**List[KubeconfigUser]**](KubeconfigUser.md) |  | [optional] 

## Example

```python
from akeyless.models.kube_config_value import KubeConfigValue

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigValue from a JSON string
kube_config_value_instance = KubeConfigValue.from_json(json)
# print the JSON string representation of the object
print(KubeConfigValue.to_json())

# convert the object into a dict
kube_config_value_dict = kube_config_value_instance.to_dict()
# create an instance of KubeConfigValue from a dict
kube_config_value_from_dict = KubeConfigValue.from_dict(kube_config_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


