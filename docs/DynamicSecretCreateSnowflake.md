# DynamicSecretCreateSnowflake

GatewayCreateProducerSnowflakeCmd is a command that creates a Snowflake dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**account_password** | **str** | Database Password | [optional] 
**account_username** | **str** | Database Username | [optional] 
**auth_mode** | **str** | The authentication mode for the temporary user [password/key] | [optional] [default to 'password']
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**db_name** | **str** | Database name | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_algo** | **str** |  | [optional] 
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**private_key** | **str** | RSA Private key (base64 encoded) | [optional] 
**private_key_passphrase** | **str** | The Private key passphrase | [optional] 
**role** | **str** | User role | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '24h']
**warehouse** | **str** | Warehouse name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


