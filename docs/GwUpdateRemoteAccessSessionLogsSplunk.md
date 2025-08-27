# GwUpdateRemoteAccessSessionLogsSplunk

gwUpdateRemoteAccessSessionLogsSplunk is a command that updates session log forwarding config (splunk target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_batch** | **str** | Enable batch forwarding [true/false] | [optional] [default to 'true']
**enable_tls** | **bool** | Enable tls | [optional] 
**index** | **str** | Splunk index | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**source** | **str** | Splunk source | [optional] [default to 'use-existing']
**source_type** | **str** | Splunk source type | [optional] [default to 'use-existing']
**splunk_token** | **str** | Splunk token | [optional] 
**splunk_url** | **str** | Splunk server URL | [optional] 
**tls_certificate** | **str** | Splunk tls certificate | [optional] [default to 'use-existing']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


