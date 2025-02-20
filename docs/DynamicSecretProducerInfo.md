# DynamicSecretProducerInfo

DynamicSecretProducerInfo The dynamic secret producer info This parameter relevant and required only in case of create update dynamic secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_message** | **str** |  | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**k8s_allowed_namespaces** | **str** | Relevant only for generic k8s producer | [optional] 
**k8s_dynamic_mode** | **bool** | Relevant only for generic k8s producer | [optional] 
**producer_last_keep_alive** | **str** |  | [optional] 
**producer_metadata** | **str** |  | [optional] 
**producer_status** | **str** | RotationStatus defines types of rotation Status | [optional] 
**producer_type** | **str** |  | [optional] 
**user_ttl** | **str** |  | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_producer_info import DynamicSecretProducerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretProducerInfo from a JSON string
dynamic_secret_producer_info_instance = DynamicSecretProducerInfo.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretProducerInfo.to_json())

# convert the object into a dict
dynamic_secret_producer_info_dict = dynamic_secret_producer_info_instance.to_dict()
# create an instance of DynamicSecretProducerInfo from a dict
dynamic_secret_producer_info_from_dict = DynamicSecretProducerInfo.from_dict(dynamic_secret_producer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


