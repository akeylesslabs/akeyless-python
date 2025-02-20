# GatewayGetDefaultsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_access_id** | **str** |  | [optional] 
**default_protection_key_id** | **str** |  | [optional] 
**hvp_route_version** | **int** |  | [optional] 
**notify_on_status_change** | **bool** |  | [optional] 
**oidc_access_id** | **str** |  | [optional] 
**saml_access_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.gateway_get_defaults_output import GatewayGetDefaultsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetDefaultsOutput from a JSON string
gateway_get_defaults_output_instance = GatewayGetDefaultsOutput.from_json(json)
# print the JSON string representation of the object
print(GatewayGetDefaultsOutput.to_json())

# convert the object into a dict
gateway_get_defaults_output_dict = gateway_get_defaults_output_instance.to_dict()
# create an instance of GatewayGetDefaultsOutput from a dict
gateway_get_defaults_output_from_dict = GatewayGetDefaultsOutput.from_dict(gateway_get_defaults_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


