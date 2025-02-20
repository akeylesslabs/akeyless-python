# GwUpdateRemoteAccessSessionLogsLogzIo

gwUpdateRemoteAccessSessionLogsLogzIo is a command that updates session log forwarding config (logz-io target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**logz_io_token** | **str** | Logz-io token | [optional] 
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**protocol** | **str** | LogzIo protocol [tcp/https] | [optional] 
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gw_update_remote_access_session_logs_logz_io import GwUpdateRemoteAccessSessionLogsLogzIo

# TODO update the JSON string below
json = "{}"
# create an instance of GwUpdateRemoteAccessSessionLogsLogzIo from a JSON string
gw_update_remote_access_session_logs_logz_io_instance = GwUpdateRemoteAccessSessionLogsLogzIo.from_json(json)
# print the JSON string representation of the object
print(GwUpdateRemoteAccessSessionLogsLogzIo.to_json())

# convert the object into a dict
gw_update_remote_access_session_logs_logz_io_dict = gw_update_remote_access_session_logs_logz_io_instance.to_dict()
# create an instance of GwUpdateRemoteAccessSessionLogsLogzIo from a dict
gw_update_remote_access_session_logs_logz_io_from_dict = GwUpdateRemoteAccessSessionLogsLogzIo.from_dict(gw_update_remote_access_session_logs_logz_io_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


