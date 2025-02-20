# K8SPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **List[int]** |  | [optional] 
**client_cert** | **List[int]** |  | [optional] 
**client_key** | **List[int]** |  | [optional] 
**namespace** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**server** | **str** |  | [optional] 
**skip_system** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.k8_s_payload import K8SPayload

# TODO update the JSON string below
json = "{}"
# create an instance of K8SPayload from a JSON string
k8_s_payload_instance = K8SPayload.from_json(json)
# print the JSON string representation of the object
print(K8SPayload.to_json())

# convert the object into a dict
k8_s_payload_dict = k8_s_payload_instance.to_dict()
# create an instance of K8SPayload from a dict
k8_s_payload_from_dict = K8SPayload.from_dict(k8_s_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


