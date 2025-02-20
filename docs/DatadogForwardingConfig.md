# DatadogForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datadog_api_key** | **str** |  | [optional] 
**datadog_host** | **str** |  | [optional] 
**datadog_log_service** | **str** |  | [optional] 
**datadog_log_source** | **str** |  | [optional] 
**datadog_log_tags** | **str** |  | [optional] 

## Example

```python
from akeyless.models.datadog_forwarding_config import DatadogForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DatadogForwardingConfig from a JSON string
datadog_forwarding_config_instance = DatadogForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(DatadogForwardingConfig.to_json())

# convert the object into a dict
datadog_forwarding_config_dict = datadog_forwarding_config_instance.to_dict()
# create an instance of DatadogForwardingConfig from a dict
datadog_forwarding_config_from_dict = DatadogForwardingConfig.from_dict(datadog_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


