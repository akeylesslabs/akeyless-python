# GatewayCreateProducerChef

gatewayCreateProducerChef is a command that creates chef producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chef_orgs** | **str** | Organizations | [optional] 
**chef_server_key** | **str** | Server key | [optional] 
**chef_server_url** | **str** | Server URL | [optional] 
**chef_server_username** | **str** | Server username | [optional] 
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**skip_ssl** | **bool** | Skip SSL | [optional] [default to True]
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


