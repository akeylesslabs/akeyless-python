# GatewayUpdateLogForwardingLogstash

gatewayUpdateLogForwardingLogstash is a command that updates log forwarding config (logstash target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **str** | Logstash dns | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**protocol** | **str** | Logstash protocol [tcp/udp] | [optional] 
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**tls_certificate** | **str** | Logstash tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_logstash import GatewayUpdateLogForwardingLogstash

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingLogstash from a JSON string
gateway_update_log_forwarding_logstash_instance = GatewayUpdateLogForwardingLogstash.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingLogstash.to_json())

# convert the object into a dict
gateway_update_log_forwarding_logstash_dict = gateway_update_log_forwarding_logstash_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingLogstash from a dict
gateway_update_log_forwarding_logstash_from_dict = GatewayUpdateLogForwardingLogstash.from_dict(gateway_update_log_forwarding_logstash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


