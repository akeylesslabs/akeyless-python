# GatewayCreateProducerRabbitMQ

gatewayCreateProducerRabbitMQ is a command that creates rabbitmq producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**rabbitmq_admin_pwd** | **str** | RabbitMQ Admin password | 
**rabbitmq_admin_user** | **str** | RabbitMQ Admin User | 
**rabbitmq_server_uri** | **str** | Server URI | 
**rabbitmq_user_conf_permission** | **str** | User configuration permission | 
**rabbitmq_user_read_permission** | **str** | User read permission | 
**rabbitmq_user_tags** | **str** | User Tags | [optional] 
**rabbitmq_user_vhost** | **str** | User Virtual Host | [optional] 
**rabbitmq_user_write_permission** | **str** | User write permission | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


