# GatewayCreateProducerMongo

gatewayCreateProducerMongo is a command that creates mongo producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**mongodb_name** | **str** | MongoDB Name | 
**mongodb_roles** | **str** | MongoDB Roles | [optional] [default to '[]']
**mongodb_server_uri** | **str** | Server URI | 
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


