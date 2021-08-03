# GatewayCreateProducerPostgreSQL

gatewayCreateProducerPostgreSQL is a command that creates postgresql producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_statements** | **str** | PostgreSQL Creation statements | [optional] 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**postgresql_db_name** | **str** | PostgreSQL DB Name | [optional] 
**postgresql_host** | **str** | PostgreSQL Host | [optional] [default to '127.0.0.1']
**postgresql_password** | **str** | PostgreSQL Password | [optional] 
**postgresql_port** | **str** | PostgreSQL Port | [optional] [default to '5432']
**postgresql_username** | **str** | PostgreSQL Username | [optional] 
**producer_encryption_key** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_db_schema** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


