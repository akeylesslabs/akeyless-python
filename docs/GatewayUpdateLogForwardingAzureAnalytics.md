# GatewayUpdateLogForwardingAzureAnalytics

gatewayUpdateLogForwardingAzureAnalytics is a command that updates log forwarding config (azure-analytics target)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **str** | Enable Log Forwarding [true/false] | [optional] [default to 'true']
**enable_batch** | **str** | Enable batch forwarding [true/false] | [optional] [default to 'true']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**output_format** | **str** | Logs format [text/json] | [optional] [default to 'text']
**pull_interval** | **str** | Pull interval in seconds | [optional] [default to '10']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**workspace_id** | **str** | Azure workspace id | [optional] 
**workspace_key** | **str** | Azure workspace key | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


