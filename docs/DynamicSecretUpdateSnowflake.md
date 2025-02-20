# DynamicSecretUpdateSnowflake

GatewayUpdateProducerSnowflakeCmd is a command that updates a Snowflake dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**account_password** | **str** | Database Password | [optional] 
**account_username** | **str** | Database Username | [optional] 
**db_name** | **str** | Database name | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**private_key** | **str** | RSA Private key (base64 encoded) | [optional] 
**private_key_passphrase** | **str** | The Private key passphrase | [optional] 
**role** | **str** | User role | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '24h']
**warehouse** | **str** | Warehouse name | [optional] 

## Example

```python
from akeyless.models.dynamic_secret_update_snowflake import DynamicSecretUpdateSnowflake

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretUpdateSnowflake from a JSON string
dynamic_secret_update_snowflake_instance = DynamicSecretUpdateSnowflake.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretUpdateSnowflake.to_json())

# convert the object into a dict
dynamic_secret_update_snowflake_dict = dynamic_secret_update_snowflake_instance.to_dict()
# create an instance of DynamicSecretUpdateSnowflake from a dict
dynamic_secret_update_snowflake_from_dict = DynamicSecretUpdateSnowflake.from_dict(dynamic_secret_update_snowflake_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


