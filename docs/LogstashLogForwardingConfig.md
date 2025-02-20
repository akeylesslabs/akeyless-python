# LogstashLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logstash_dns** | **str** |  | [optional] 
**logstash_enable_tls** | **bool** |  | [optional] 
**logstash_protocol** | **str** |  | [optional] 
**logstash_tls_certificate** | **str** |  | [optional] 

## Example

```python
from akeyless.models.logstash_log_forwarding_config import LogstashLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LogstashLogForwardingConfig from a JSON string
logstash_log_forwarding_config_instance = LogstashLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(LogstashLogForwardingConfig.to_json())

# convert the object into a dict
logstash_log_forwarding_config_dict = logstash_log_forwarding_config_instance.to_dict()
# create an instance of LogstashLogForwardingConfig from a dict
logstash_log_forwarding_config_from_dict = LogstashLogForwardingConfig.from_dict(logstash_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


