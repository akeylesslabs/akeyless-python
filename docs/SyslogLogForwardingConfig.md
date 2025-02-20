# SyslogLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syslog_enable_tls** | **bool** |  | [optional] 
**syslog_formatter** | **str** |  | [optional] 
**syslog_host** | **str** |  | [optional] 
**syslog_network** | **str** |  | [optional] 
**syslog_target_tag** | **str** |  | [optional] 
**syslog_tls_certificate** | **str** |  | [optional] 

## Example

```python
from akeyless.models.syslog_log_forwarding_config import SyslogLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogLogForwardingConfig from a JSON string
syslog_log_forwarding_config_instance = SyslogLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(SyslogLogForwardingConfig.to_json())

# convert the object into a dict
syslog_log_forwarding_config_dict = syslog_log_forwarding_config_instance.to_dict()
# create an instance of SyslogLogForwardingConfig from a dict
syslog_log_forwarding_config_from_dict = SyslogLogForwardingConfig.from_dict(syslog_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


