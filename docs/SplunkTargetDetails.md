# SplunkTargetDetails

SplunkTargetDetails defines details related to connecting to a Splunk server
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | Token audience | [optional] 
**auth_mode** | **str** | Authentication mode: \&quot;username\&quot; or \&quot;token\&quot; | [optional] 
**password** | **str** |  | [optional] 
**splunk_payload** | [**SplunkPayload**](SplunkPayload.md) |  | [optional] 
**splunk_url** | **str** | Splunk server URL | [optional] 
**token** | **str** | Token is used when AuthMode &#x3D;&#x3D; \&quot;token\&quot; | [optional] 
**token_owner** | **str** | Token owner (the Splunk user who owns the token, required for token rotation) | [optional] 
**use_tls** | **bool** | Use TLS certificate verification when connecting to the Splunk management API. | [optional] 
**username** | **str** | Username &amp; Password are used when AuthMode &#x3D;&#x3D; \&quot;username\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


