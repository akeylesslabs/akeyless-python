# GatewayCreateProducerMySQL

gatewayCreateProducerMySQL is a command that creates mysql producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**mysql_dbname** | **str** | MySQL DB Name | 
**mysql_host** | **str** | MySQL Host | [optional] [default to '127.0.0.1']
**mysql_password** | **str** | MySQL Password | 
**mysql_port** | **str** | MySQL Port | [optional] [default to '3306']
**mysql_screation_statements** | **str** | MySQL Creation statements | [optional] 
**mysql_username** | **str** | MySQL Username | 
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


