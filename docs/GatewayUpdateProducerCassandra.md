# GatewayUpdateProducerCassandra

gatewayUpdateProducerCassandra is a command that updates a Cassandra producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_creation_statements** | **str** | Cassandra creation statements | [optional] 
**cassandra_hosts** | **str** | Cassandra hosts IP or addresses, comma separated | [optional] 
**cassandra_password** | **str** | Cassandra superuser password | [optional] 
**cassandra_port** | **str** | Cassandra port | [optional] [default to '9042']
**cassandra_username** | **str** | Cassandra superuser username | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**ssl_certificate** | **str** | SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA) | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


