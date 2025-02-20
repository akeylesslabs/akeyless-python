# GatewayCreateProducerMySQL

gatewayCreateProducerMySQL is a command that creates mysql producer [Deprecated: Use dynamic-secret-create-mysql command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**mysql_dbname** | **str** | MySQL DB Name | [optional] 
**mysql_host** | **str** | MySQL Host | [optional] [default to '127.0.0.1']
**mysql_password** | **str** | MySQL Password | [optional] 
**mysql_port** | **str** | MySQL Port | [optional] [default to '3306']
**mysql_revocation_statements** | **str** | MySQL Revocation statements | [optional] 
**mysql_screation_statements** | **str** | MySQL Creation statements | [optional] 
**mysql_username** | **str** | MySQL Username | [optional] 
**name** | **str** | Dynamic secret name | 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**ssl_certificate** | **str** | SSL connection certificate | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_create_producer_my_sql import GatewayCreateProducerMySQL

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerMySQL from a JSON string
gateway_create_producer_my_sql_instance = GatewayCreateProducerMySQL.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerMySQL.to_json())

# convert the object into a dict
gateway_create_producer_my_sql_dict = gateway_create_producer_my_sql_instance.to_dict()
# create an instance of GatewayCreateProducerMySQL from a dict
gateway_create_producer_my_sql_from_dict = GatewayCreateProducerMySQL.from_dict(gateway_create_producer_my_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


