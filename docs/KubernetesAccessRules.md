# KubernetesAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**audience** | **str** | Audience is an optional Kubernetes jwt claim to verify | [optional] 
**bound_namespaces** | **List[str]** | A list of namespaces that the authentication is restricted to. | [optional] 
**bound_pod_names** | **List[str]** | A list of pods names that the authentication is restricted to. | [optional] 
**bound_service_account_names** | **List[str]** | A list of service account names that the authentication is restricted to. | [optional] 
**gen_key_pair** | **str** | Generate public/private key (the private key is required for the K8S Auth Config in the Akeyless Gateway) | [optional] 
**pub_key** | **str** | The public key value of the Kubernetes auth method configuration in the Akeyless Gateway. | [optional] 

## Example

```python
from akeyless.models.kubernetes_access_rules import KubernetesAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAccessRules from a JSON string
kubernetes_access_rules_instance = KubernetesAccessRules.from_json(json)
# print the JSON string representation of the object
print(KubernetesAccessRules.to_json())

# convert the object into a dict
kubernetes_access_rules_dict = kubernetes_access_rules_instance.to_dict()
# create an instance of KubernetesAccessRules from a dict
kubernetes_access_rules_from_dict = KubernetesAccessRules.from_dict(kubernetes_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


