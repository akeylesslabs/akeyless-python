# DynamicSecretCreatePostgreSql

dynamicSecretCreatePostgreSql is a command that creates postgresql dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_statements** | **str** | PostgreSQL Creation statements | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**postgresql_db_name** | **str** | PostgreSQL DB Name | [optional] 
**postgresql_host** | **str** | PostgreSQL Host | [optional] [default to '127.0.0.1']
**postgresql_password** | **str** | PostgreSQL Password | [optional] 
**postgresql_port** | **str** | PostgreSQL Port | [optional] [default to '5432']
**postgresql_username** | **str** | PostgreSQL Username | [optional] 
**producer_encryption_key** | **str** | Dynamic producer encryption key | [optional] 
**revocation_statement** | **str** | PostgreSQL Revocation statements | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_db_schema** | **str** | The DB schema | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.dynamic_secret_create_postgre_sql import DynamicSecretCreatePostgreSql

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretCreatePostgreSql from a JSON string
dynamic_secret_create_postgre_sql_instance = DynamicSecretCreatePostgreSql.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretCreatePostgreSql.to_json())

# convert the object into a dict
dynamic_secret_create_postgre_sql_dict = dynamic_secret_create_postgre_sql_instance.to_dict()
# create an instance of DynamicSecretCreatePostgreSql from a dict
dynamic_secret_create_postgre_sql_from_dict = DynamicSecretCreatePostgreSql.from_dict(dynamic_secret_create_postgre_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


