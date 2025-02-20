# GatewayDeleteK8SAuthConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**parts_change** | [**ConfigChange**](ConfigChange.md) |  | [optional] 
**total_hash** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_delete_k8_s_auth_config_output import GatewayDeleteK8SAuthConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeleteK8SAuthConfigOutput from a JSON string
gateway_delete_k8_s_auth_config_output_instance = GatewayDeleteK8SAuthConfigOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayDeleteK8SAuthConfigOutput.to_json())

# convert the object into a dict
gateway_delete_k8_s_auth_config_output_dict = gateway_delete_k8_s_auth_config_output_instance.to_dict()
# create an instance of GatewayDeleteK8SAuthConfigOutput from a dict
gateway_delete_k8_s_auth_config_output_from_dict = GatewayDeleteK8SAuthConfigOutput.from_dict(gateway_delete_k8_s_auth_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


