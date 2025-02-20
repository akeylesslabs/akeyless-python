# GatewayUpdateLogForwardingSplunk

gatewayUpdateLogForwardingSplunk is a command that updates log forwarding config (splunk target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**index** | **str** | Splunk index | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**source** | **str** | Splunk source | [optional] [default to 'use-existing']
**source_type** | **str** | Splunk source type | [optional] [default to 'use-existing']
**splunk_token** | **str** | Splunk token | [optional] 
**splunk_url** | **str** | Splunk server URL | [optional] 
**tls_certificate** | **str** | Splunk tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_splunk import GatewayUpdateLogForwardingSplunk

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingSplunk from a JSON string
gateway_update_log_forwarding_splunk_instance = GatewayUpdateLogForwardingSplunk.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingSplunk.to_json())

# convert the object into a dict
gateway_update_log_forwarding_splunk_dict = gateway_update_log_forwarding_splunk_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingSplunk from a dict
gateway_update_log_forwarding_splunk_from_dict = GatewayUpdateLogForwardingSplunk.from_dict(gateway_update_log_forwarding_splunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


