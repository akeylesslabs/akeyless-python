# GatewayDeleteAllowedAccessOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_access_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_delete_allowed_access_output import GatewayDeleteAllowedAccessOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeleteAllowedAccessOutput from a JSON string
gateway_delete_allowed_access_output_instance = GatewayDeleteAllowedAccessOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayDeleteAllowedAccessOutput.to_json())

# convert the object into a dict
gateway_delete_allowed_access_output_dict = gateway_delete_allowed_access_output_instance.to_dict()
# create an instance of GatewayDeleteAllowedAccessOutput from a dict
gateway_delete_allowed_access_output_from_dict = GatewayDeleteAllowedAccessOutput.from_dict(gateway_delete_allowed_access_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


