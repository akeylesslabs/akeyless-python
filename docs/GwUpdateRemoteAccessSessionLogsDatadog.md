# GwUpdateRemoteAccessSessionLogsDatadog

gwUpdateRemoteAccessSessionLogsDatadog is a command that updates session log forwarding config (datadog target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Datadog api key | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**host** | **str** | Datadog host | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**log_service** | **str** | Datadog log service | [optional] [default to 'use-existing']
**log_source** | **str** | Datadog log source | [optional] [default to 'use-existing']
**log_tags** | **str** | A comma-separated list of Datadog log tags formatted as \&quot;key:value\&quot; strings | [optional] [default to 'use-existing']
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


