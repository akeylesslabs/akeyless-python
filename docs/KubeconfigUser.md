# KubeconfigUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**user** | [**KubeconfigUserExec**](KubeconfigUserExec.md) |  | [optional] 

## Example

```python
from akeyless.models.kubeconfig_user import KubeconfigUser

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigUser from a JSON string
kubeconfig_user_instance = KubeconfigUser.from_json(json)
# print the JSON string representation of the object
print(KubeconfigUser.to_json())

# convert the object into a dict
kubeconfig_user_dict = kubeconfig_user_instance.to_dict()
# create an instance of KubeconfigUser from a dict
kubeconfig_user_from_dict = KubeconfigUser.from_dict(kubeconfig_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


