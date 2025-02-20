# LogForwardingConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_s3_config** | [**AwsS3LogForwardingConfig**](AwsS3LogForwardingConfig.md) |  | [optional] 
**azure_analytics_config** | [**AzureLogAnalyticsForwardingConfig**](AzureLogAnalyticsForwardingConfig.md) |  | [optional] 
**datadog_config** | [**DatadogForwardingConfig**](DatadogForwardingConfig.md) |  | [optional] 
**elasticsearch_config** | [**ElasticsearchLogForwardingConfig**](ElasticsearchLogForwardingConfig.md) |  | [optional] 
**google_chronicle_config** | [**GoogleChronicleForwardingConfig**](GoogleChronicleForwardingConfig.md) |  | [optional] 
**json_output** | **bool** |  | [optional] 
**logan_enable** | **bool** |  | [optional] 
**logan_url** | **str** |  | [optional] 
**logstash_config** | [**LogstashLogForwardingConfig**](LogstashLogForwardingConfig.md) |  | [optional] 
**logz_io_config** | [**LogzIoLogForwardingConfig**](LogzIoLogForwardingConfig.md) |  | [optional] 
**pull_interval_sec** | **str** |  | [optional] 
**splunk_config** | [**SplunkLogForwardingConfig**](SplunkLogForwardingConfig.md) |  | [optional] 
**sumo_logic_config** | [**SumologicLogForwardingConfig**](SumologicLogForwardingConfig.md) |  | [optional] 
**syslog_config** | [**SyslogLogForwardingConfig**](SyslogLogForwardingConfig.md) |  | [optional] 
**target_log_type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.log_forwarding_config_part import LogForwardingConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwardingConfigPart from a JSON string
log_forwarding_config_part_instance = LogForwardingConfigPart.from_json(json)
# print the JSON string representation of the object
print(LogForwardingConfigPart.to_json())

# convert the object into a dict
log_forwarding_config_part_dict = log_forwarding_config_part_instance.to_dict()
# create an instance of LogForwardingConfigPart from a dict
log_forwarding_config_part_from_dict = LogForwardingConfigPart.from_dict(log_forwarding_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


