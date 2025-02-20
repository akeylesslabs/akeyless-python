# GatewayUpdateLogForwardingStdout

gatewayUpdateLogForwardingStdout is a command that updates log forwarding config (stdout target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_stdout import GatewayUpdateLogForwardingStdout

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingStdout from a JSON string
gateway_update_log_forwarding_stdout_instance = GatewayUpdateLogForwardingStdout.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingStdout.to_json())

# convert the object into a dict
gateway_update_log_forwarding_stdout_dict = gateway_update_log_forwarding_stdout_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingStdout from a dict
gateway_update_log_forwarding_stdout_from_dict = GatewayUpdateLogForwardingStdout.from_dict(gateway_update_log_forwarding_stdout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


