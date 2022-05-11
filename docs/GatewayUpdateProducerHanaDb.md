# GatewayUpdateProducerHanaDb

gatewayUpdateProducerHanaDb is a command that updates hanadb producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hana_dbname** | **str** | HanaDb Name | [optional] 
**hanadb_create_statements** | **str** | HanaDb Creation statements | [optional] 
**hanadb_host** | **str** | HanaDb Host | [optional] [default to '127.0.0.1']
**hanadb_password** | **str** | HanaDb Password | [optional] 
**hanadb_port** | **str** | HanaDb Port | [optional] [default to '443']
**hanadb_revocation_statements** | **str** | HanaDb Revocation statements | [optional] 
**hanadb_username** | **str** | HanaDb Username | [optional] 
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


