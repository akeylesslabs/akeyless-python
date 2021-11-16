# GatewayUpdateProducerMySQL

gatewayUpdateProducerMySQL is a command that updates mysql producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**mysql_dbname** | **str** | MySQL DB Name | [optional] 
**mysql_host** | **str** | MySQL Host | [optional] [default to '127.0.0.1']
**mysql_password** | **str** | MySQL Password | [optional] 
**mysql_port** | **str** | MySQL Port | [optional] [default to '3306']
**mysql_screation_statements** | **str** | MySQL Creation statements | [optional] 
**mysql_username** | **str** | MySQL Username | [optional] 
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_web** | **bool** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


