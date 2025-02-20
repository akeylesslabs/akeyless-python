# GatewaysListResponse

GatewaysListResponse Gateway cluster identity list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[GwClusterIdentity]**](GwClusterIdentity.md) |  | [optional] 

## Example

```python
from akeyless.models.gateways_list_response import GatewaysListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewaysListResponse from a JSON string
gateways_list_response_instance = GatewaysListResponse.from_json(json)
# print the JSON string representation of the object
print(GatewaysListResponse.to_json())

# convert the object into a dict
gateways_list_response_dict = gateways_list_response_instance.to_dict()
# create an instance of GatewaysListResponse from a dict
gateways_list_response_from_dict = GatewaysListResponse.from_dict(gateways_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


