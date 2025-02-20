# GatewayUpdateLogForwardingGoogleChronicle

gatewayUpdateLogForwardingGoogleChronicle is a command that updates log forwarding config (google-chronicle target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Google chronicle customer id | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**log_type** | **str** | Google chronicle log type | [optional] 
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**region** | **str** | Google chronicle region [eu_multi_region/london/us_multi_region/singapore/tel_aviv] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gateway_update_log_forwarding_google_chronicle import GatewayUpdateLogForwardingGoogleChronicle

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateLogForwardingGoogleChronicle from a JSON string
gateway_update_log_forwarding_google_chronicle_instance = GatewayUpdateLogForwardingGoogleChronicle.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateLogForwardingGoogleChronicle.to_json())

# convert the object into a dict
gateway_update_log_forwarding_google_chronicle_dict = gateway_update_log_forwarding_google_chronicle_instance.to_dict()
# create an instance of GatewayUpdateLogForwardingGoogleChronicle from a dict
gateway_update_log_forwarding_google_chronicle_from_dict = GatewayUpdateLogForwardingGoogleChronicle.from_dict(gateway_update_log_forwarding_google_chronicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


