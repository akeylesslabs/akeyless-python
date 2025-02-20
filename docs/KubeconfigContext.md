# KubeconfigContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_context import KubeconfigContext

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigContext from a JSON string
kubeconfig_context_instance = KubeconfigContext.from_json(json)
# print the JSON string representation of the object
print(KubeconfigContext.to_json())

# convert the object into a dict
kubeconfig_context_dict = kubeconfig_context_instance.to_dict()
# create an instance of KubeconfigContext from a dict
kubeconfig_context_from_dict = KubeconfigContext.from_dict(kubeconfig_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


