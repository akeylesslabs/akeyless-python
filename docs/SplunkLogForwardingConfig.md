# SplunkLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splunk_enable_tls** | **bool** |  | [optional] 
**splunk_index** | **str** |  | [optional] 
**splunk_source** | **str** |  | [optional] 
**splunk_sourcetype** | **str** |  | [optional] 
**splunk_tls_certificate** | **str** |  | [optional] 
**splunk_token** | **str** |  | [optional] 
**splunk_url** | **str** |  | [optional] 

## Example

```python
from akeyless.models.splunk_log_forwarding_config import SplunkLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SplunkLogForwardingConfig from a JSON string
splunk_log_forwarding_config_instance = SplunkLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(SplunkLogForwardingConfig.to_json())

# convert the object into a dict
splunk_log_forwarding_config_dict = splunk_log_forwarding_config_instance.to_dict()
# create an instance of SplunkLogForwardingConfig from a dict
splunk_log_forwarding_config_from_dict = SplunkLogForwardingConfig.from_dict(splunk_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


