# GwUpdateRemoteAccessSessionLogsLogstash

gwUpdateRemoteAccessSessionLogsLogstash is a command that updates session log forwarding config (logstash target)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **str** | Logstash dns | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**protocol** | **str** | Logstash protocol [tcp/udp] | [optional] 
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**tls_certificate** | **str** | Logstash tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.gw_update_remote_access_session_logs_logstash import GwUpdateRemoteAccessSessionLogsLogstash

# TODO update the JSON string below
json = "{}"
# create an instance of GwUpdateRemoteAccessSessionLogsLogstash from a JSON string
gw_update_remote_access_session_logs_logstash_instance = GwUpdateRemoteAccessSessionLogsLogstash.from_json(json)
# print the JSON string representation of the object
print(GwUpdateRemoteAccessSessionLogsLogstash.to_json())

# convert the object into a dict
gw_update_remote_access_session_logs_logstash_dict = gw_update_remote_access_session_logs_logstash_instance.to_dict()
# create an instance of GwUpdateRemoteAccessSessionLogsLogstash from a dict
gw_update_remote_access_session_logs_logstash_from_dict = GwUpdateRemoteAccessSessionLogsLogstash.from_dict(gw_update_remote_access_session_logs_logstash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


