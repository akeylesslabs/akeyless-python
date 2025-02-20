# GwUpdateRemoteAccessSessionLogsAzureAnalytics

gwUpdateRemoteAccessSessionLogsAzureAnalytics is a command that updates session log forwarding config (azure-analytics target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**workspace_id** | **str** | Azure workspace id | [optional] 
**workspace_key** | **str** | Azure workspace key | [optional] 

## Example

```python
from akeyless.models.gw_update_remote_access_session_logs_azure_analytics import GwUpdateRemoteAccessSessionLogsAzureAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of GwUpdateRemoteAccessSessionLogsAzureAnalytics from a JSON string
gw_update_remote_access_session_logs_azure_analytics_instance = GwUpdateRemoteAccessSessionLogsAzureAnalytics.from_json(json)
# print the JSON string representation of the object
print(GwUpdateRemoteAccessSessionLogsAzureAnalytics.to_json())

# convert the object into a dict
gw_update_remote_access_session_logs_azure_analytics_dict = gw_update_remote_access_session_logs_azure_analytics_instance.to_dict()
# create an instance of GwUpdateRemoteAccessSessionLogsAzureAnalytics from a dict
gw_update_remote_access_session_logs_azure_analytics_from_dict = GwUpdateRemoteAccessSessionLogsAzureAnalytics.from_dict(gw_update_remote_access_session_logs_azure_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


