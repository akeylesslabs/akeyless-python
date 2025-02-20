# KubeconfigGenerateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicted_clusters_names** | **List[str]** |  | [optional] 
**data** | [**KubeConfigValue**](KubeConfigValue.md) |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_generate_output import KubeconfigGenerateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigGenerateOutput from a JSON string
kubeconfig_generate_output_instance = KubeconfigGenerateOutput.from_json(json)
# print the JSON string representation of the object
print(KubeconfigGenerateOutput.to_json())

# convert the object into a dict
kubeconfig_generate_output_dict = kubeconfig_generate_output_instance.to_dict()
# create an instance of KubeconfigGenerateOutput from a dict
kubeconfig_generate_output_from_dict = KubeconfigGenerateOutput.from_dict(kubeconfig_generate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


