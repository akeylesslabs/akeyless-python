# GatewayGetAllowedAccess

gatewayGetAllowedAccess is a command that gets allowed access from gateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Allowed access name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_get_allowed_access import GatewayGetAllowedAccess

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetAllowedAccess from a JSON string
gateway_get_allowed_access_instance = GatewayGetAllowedAccess.from_json(json)
# print the JSON string representation of the object
print(GatewayGetAllowedAccess.to_json())

# convert the object into a dict
gateway_get_allowed_access_dict = gateway_get_allowed_access_instance.to_dict()
# create an instance of GatewayGetAllowedAccess from a dict
gateway_get_allowed_access_from_dict = GatewayGetAllowedAccess.from_dict(gateway_get_allowed_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


