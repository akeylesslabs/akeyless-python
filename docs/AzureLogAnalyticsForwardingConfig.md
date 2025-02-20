# AzureLogAnalyticsForwardingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_workspace_id** | **str** |  | [optional] 
**azure_workspace_key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.azure_log_analytics_forwarding_config import AzureLogAnalyticsForwardingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLogAnalyticsForwardingConfig from a JSON string
azure_log_analytics_forwarding_config_instance = AzureLogAnalyticsForwardingConfig.from_json(json)
# print the JSON string representation of the object
print(AzureLogAnalyticsForwardingConfig.to_json())

# convert the object into a dict
azure_log_analytics_forwarding_config_dict = azure_log_analytics_forwarding_config_instance.to_dict()
# create an instance of AzureLogAnalyticsForwardingConfig from a dict
azure_log_analytics_forwarding_config_from_dict = AzureLogAnalyticsForwardingConfig.from_dict(azure_log_analytics_forwarding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


