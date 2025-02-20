# KubeconfigExec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**command** | **str** |  | [optional] 
**interactive_mode** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_exec import KubeconfigExec

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigExec from a JSON string
kubeconfig_exec_instance = KubeconfigExec.from_json(json)
# print the JSON string representation of the object
print(KubeconfigExec.to_json())

# convert the object into a dict
kubeconfig_exec_dict = kubeconfig_exec_instance.to_dict()
# create an instance of KubeconfigExec from a dict
kubeconfig_exec_from_dict = KubeconfigExec.from_dict(kubeconfig_exec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


