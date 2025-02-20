# GatewayNameInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_display_name** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_name_info import GatewayNameInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayNameInfo from a JSON string
gateway_name_info_instance = GatewayNameInfo.from_json(json)
# print the JSON string representation of the object
print(GatewayNameInfo.to_json())

# convert the object into a dict
gateway_name_info_dict = gateway_name_info_instance.to_dict()
# create an instance of GatewayNameInfo from a dict
gateway_name_info_from_dict = GatewayNameInfo.from_dict(gateway_name_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


