# GwUpdateRemoteAccessSessionLogsSyslog

gwUpdateRemoteAccessSessionLogsSyslog is a command that updates session log forwarding config (syslog target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls relevant only for network type TCP | [optional] 
**formatter** | **str** | Syslog formatter [text/cef] | [optional] [default to 'text']
**host** | **str** | Syslog host | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**network** | **str** | Syslog network [tcp/udp] | [optional] [default to 'tcp']
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**target_tag** | **str** | Syslog target tag | [optional] [default to 'use-existing']
**tls_certificate** | **str** | Syslog tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


