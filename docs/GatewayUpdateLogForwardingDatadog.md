# GatewayUpdateLogForwardingDatadog

gatewayUpdateLogForwardingDatadog is a command that updates log forwarding config (datadog target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Datadog api key | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**host** | **str** | Datadog host | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**log_service** | **str** | Datadog log service | [optional] [default to 'use-existing']
**log_source** | **str** | Datadog log source | [optional] [default to 'use-existing']
**log_tags** | **str** | A comma-separated list of Datadog log tags formatted as \&quot;key:value\&quot; strings | [optional] [default to 'use-existing']
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_datadog import GatewayUpdateLogForwardingDatadog

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingDatadog from a JSON string
gateway_update_log_forwarding_datadog_instance = GatewayUpdateLogForwardingDatadog.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingDatadog.to_json())

# convert the object into a dict
gateway_update_log_forwarding_datadog_dict = gateway_update_log_forwarding_datadog_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingDatadog from a dict
gateway_update_log_forwarding_datadog_from_dict = GatewayUpdateLogForwardingDatadog.from_dict(gateway_update_log_forwarding_datadog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


