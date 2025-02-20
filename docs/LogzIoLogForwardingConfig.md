# LogzIoLogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_logz_io_protocol** | **str** |  | [optional] 
**target_logz_io_token** | **str** |  | [optional] 

## Example

```python
from akeyless.models.logz_io_log_forwarding_config import LogzIoLogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LogzIoLogForwardingConfig from a JSON string
logz_io_log_forwarding_config_instance = LogzIoLogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(LogzIoLogForwardingConfig.to_json())

# convert the object into a dict
logz_io_log_forwarding_config_dict = logz_io_log_forwarding_config_instance.to_dict()
# create an instance of LogzIoLogForwardingConfig from a dict
logz_io_log_forwarding_config_from_dict = LogzIoLogForwardingConfig.from_dict(logz_io_log_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


