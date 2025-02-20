# GatewayUpdateLogForwardingSumologic

gatewayUpdateLogForwardingSumologic is a command that updates log forwarding config (sumologic target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**endpoint** | **str** | Sumologic endpoint URL | [optional] 
**host** | **str** | Sumologic host | [optional] [default to 'use-existing']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**sumologic_tags** | **str** | A comma-separated list of Sumologic tags | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_sumologic import GatewayUpdateLogForwardingSumologic

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingSumologic from a JSON string
gateway_update_log_forwarding_sumologic_instance = GatewayUpdateLogForwardingSumologic.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingSumologic.to_json())

# convert the object into a dict
gateway_update_log_forwarding_sumologic_dict = gateway_update_log_forwarding_sumologic_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingSumologic from a dict
gateway_update_log_forwarding_sumologic_from_dict = GatewayUpdateLogForwardingSumologic.from_dict(gateway_update_log_forwarding_sumologic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


