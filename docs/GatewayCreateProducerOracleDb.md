# GatewayCreateProducerOracleDb

gatewayCreateProducerOracleDb is a command that creates oracle db producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**name** | **str** | Producer name | 
**oracle_host** | **str** | Oracle Host | [optional] [default to '127.0.0.1']
**oracle_password** | **str** | Oracle Password | [optional] 
**oracle_port** | **str** | Oracle Port | [optional] [default to '1521']
**oracle_screation_statements** | **str** | Oracle Creation statements | [optional] 
**oracle_service_name** | **str** | Oracle DB Name | [optional] 
**oracle_username** | **str** | Oracle Username | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_web** | **bool** |  | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


