# KubeconfigCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_authority** | **str** | CertificateAuthority is optional and can be omitted if not used. | [optional] 
**certificate_authority_data** | **str** |  | [optional] 
**server** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_cluster import KubeconfigCluster

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigCluster from a JSON string
kubeconfig_cluster_instance = KubeconfigCluster.from_json(json)
# print the JSON string representation of the object
print(KubeconfigCluster.to_json())

# convert the object into a dict
kubeconfig_cluster_dict = kubeconfig_cluster_instance.to_dict()
# create an instance of KubeconfigCluster from a dict
kubeconfig_cluster_from_dict = KubeconfigCluster.from_dict(kubeconfig_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


