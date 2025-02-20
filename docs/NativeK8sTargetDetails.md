# NativeK8sTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_auth_type** | **str** |  | [optional] 
**k8s_bearer_token** | **str** |  | [optional] 
**k8s_client_cert_data** | **str** | For K8s Client certificates authentication | [optional] 
**k8s_client_key_data** | **str** |  | [optional] 
**k8s_cluster_ca_certificate** | **str** |  | [optional] 
**k8s_cluster_endpoint** | **str** |  | [optional] 
**k8s_cluster_name** | **str** |  | [optional] 
**use_gw_service_account** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.native_k8s_target_details import NativeK8sTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NativeK8sTargetDetails from a JSON string
native_k8s_target_details_instance = NativeK8sTargetDetails.from_json(json)
# print the JSON string representation of the object
print(NativeK8sTargetDetails.to_json())

# convert the object into a dict
native_k8s_target_details_dict = native_k8s_target_details_instance.to_dict()
# create an instance of NativeK8sTargetDetails from a dict
native_k8s_target_details_from_dict = NativeK8sTargetDetails.from_dict(native_k8s_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


