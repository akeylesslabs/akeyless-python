# GatewayBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_display_name** | **str** |  | [optional] 
**cluster_id** | **int** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**cluster_url** | **str** |  | [optional] 
**is_cluster_available** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.gateway_basic_info import GatewayBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBasicInfo from a JSON string
gateway_basic_info_instance = GatewayBasicInfo.from_json(json)
# print the JSON string representation of the object
print(GatewayBasicInfo.to_json())

# convert the object into a dict
gateway_basic_info_dict = gateway_basic_info_instance.to_dict()
# create an instance of GatewayBasicInfo from a dict
gateway_basic_info_from_dict = GatewayBasicInfo.from_dict(gateway_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


