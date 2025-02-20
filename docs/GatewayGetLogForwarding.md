# GatewayGetLogForwarding

gatewayGetLogForwarding is a command to get log forwarding configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_get_log_forwarding import GatewayGetLogForwarding

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayGetLogForwarding from a JSON string
gateway_get_log_forwarding_instance = GatewayGetLogForwarding.from_json(json)
# print the JSON string representation of the object
print(GatewayGetLogForwarding.to_json())

# convert the object into a dict
gateway_get_log_forwarding_dict = gateway_get_log_forwarding_instance.to_dict()
# create an instance of GatewayGetLogForwarding from a dict
gateway_get_log_forwarding_from_dict = GatewayGetLogForwarding.from_dict(gateway_get_log_forwarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


