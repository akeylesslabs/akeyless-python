# DynamicSecretUpdateRabbitMq

dynamicSecretUpdateRabbitMq is a command that updates rabbitmq dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**rabbitmq_admin_pwd** | **str** | RabbitMQ Admin password | [optional] 
**rabbitmq_admin_user** | **str** | RabbitMQ Admin User | [optional] 
**rabbitmq_server_uri** | **str** | Server URI | [optional] 
**rabbitmq_user_conf_permission** | **str** | User configuration permission | [optional] 
**rabbitmq_user_read_permission** | **str** | User read permission | [optional] 
**rabbitmq_user_tags** | **str** | User Tags | [optional] 
**rabbitmq_user_vhost** | **str** | User Virtual Host | [optional] 
**rabbitmq_user_write_permission** | **str** | User write permission | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to True]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless Web Access Bastion | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless Web Access Bastion | [optional] [default to False]
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


