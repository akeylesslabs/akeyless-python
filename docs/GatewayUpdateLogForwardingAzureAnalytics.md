# GatewayUpdateLogForwardingAzureAnalytics

gatewayUpdateLogForwardingAzureAnalytics is a command that updates log forwarding config (azure-analytics target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**workspace_id** | **str** | Azure workspace id | [optional] 
**workspace_key** | **str** | Azure workspace key | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_azure_analytics import GatewayUpdateLogForwardingAzureAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingAzureAnalytics from a JSON string
gateway_update_log_forwarding_azure_analytics_instance = GatewayUpdateLogForwardingAzureAnalytics.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingAzureAnalytics.to_json())

# convert the object into a dict
gateway_update_log_forwarding_azure_analytics_dict = gateway_update_log_forwarding_azure_analytics_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingAzureAnalytics from a dict
gateway_update_log_forwarding_azure_analytics_from_dict = GatewayUpdateLogForwardingAzureAnalytics.from_dict(gateway_update_log_forwarding_azure_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


