# GwUpdateRemoteAccessSessionLogsLogstash

gwUpdateRemoteAccessSessionLogsLogstash is a command that updates session log forwarding config (logstash target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **str** | Logstash dns | [optional] 
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**protocol** | **str** | Logstash protocol [tcp/udp] | [optional] 
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**tls_certificate** | **str** | Logstash tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


