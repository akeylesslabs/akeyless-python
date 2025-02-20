# KubeconfigUserExec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_exec** | [**KubeconfigExec**](KubeconfigExec.md) |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_user_exec import KubeconfigUserExec

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigUserExec from a JSON string
kubeconfig_user_exec_instance = KubeconfigUserExec.from_json(json)
# print the JSON string representation of the object
print(KubeconfigUserExec.to_json())

# convert the object into a dict
kubeconfig_user_exec_dict = kubeconfig_user_exec_instance.to_dict()
# create an instance of KubeconfigUserExec from a dict
kubeconfig_user_exec_from_dict = KubeconfigUserExec.from_dict(kubeconfig_user_exec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


