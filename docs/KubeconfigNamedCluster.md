# KubeconfigNamedCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KubeconfigCluster**](KubeconfigCluster.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_named_cluster import KubeconfigNamedCluster

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigNamedCluster from a JSON string
kubeconfig_named_cluster_instance = KubeconfigNamedCluster.from_json(json)
# print the JSON string representation of the object
print(KubeconfigNamedCluster.to_json())

# convert the object into a dict
kubeconfig_named_cluster_dict = kubeconfig_named_cluster_instance.to_dict()
# create an instance of KubeconfigNamedCluster from a dict
kubeconfig_named_cluster_from_dict = KubeconfigNamedCluster.from_dict(kubeconfig_named_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


