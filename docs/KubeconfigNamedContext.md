# KubeconfigNamedContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**KubeconfigContext**](KubeconfigContext.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_named_context import KubeconfigNamedContext

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigNamedContext from a JSON string
kubeconfig_named_context_instance = KubeconfigNamedContext.from_json(json)
# print the JSON string representation of the object
print(KubeconfigNamedContext.to_json())

# convert the object into a dict
kubeconfig_named_context_dict = kubeconfig_named_context_instance.to_dict()
# create an instance of KubeconfigNamedContext from a dict
kubeconfig_named_context_from_dict = KubeconfigNamedContext.from_dict(kubeconfig_named_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


