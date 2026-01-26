# GatewayUpdateTlsCert

gatewayUpdateTlsCert is a command that updates Gateway TLS certificate
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_data** | **str** | TLS Certificate (base64 encoded) | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_data** | **str** | TLS Private Key (base64 encoded) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


