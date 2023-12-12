# GeneralConfigPart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**akeyless_url** | **str** | AkeylessUrl is here for BC only. Gator will still return it if it exists in the configuration, but new clients (&gt;&#x3D;2.34.0) will ignore it and override it with what exists in their local file. It will no longer be sent to Gator for update, so new clusters will only have the default value saved in the DB. | [optional] 
**api_token_ttl** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**enable_sni_proxy** | **bool** |  | [optional] 
**enable_tls** | **bool** |  | [optional] 
**enable_tls_configure** | **bool** |  | [optional] 
**enable_tls_curl** | **bool** |  | [optional] 
**enable_tls_hvp** | **bool** |  | [optional] 
**gw_cluster_url** | **str** |  | [optional] 
**notify_on_status_change** | **bool** |  | [optional] 
**tcp_port** | **str** |  | [optional] 
**tls_cert** | **str** |  | [optional] 
**tls_key** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


