# GatewayUpdateProducerMSSQL

gatewayUpdateProducerMSSQL is a command that updates mssql producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**mssql_create_statements** | **str** | MSSQL Creation statements | [optional] 
**mssql_dbname** | **str** | MSSQL Name | [optional] 
**mssql_host** | **str** | MSSQL Host | [optional] [default to '127.0.0.1']
**mssql_password** | **str** | MSSQL Password | [optional] 
**mssql_port** | **str** | MSSQL Port | [optional] [default to '1433']
**mssql_revocation_statements** | **str** | MSSQL Revocation statements | [optional] 
**mssql_username** | **str** | MSSQL Username | [optional] 
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_db_schema** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_web** | **bool** |  | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


