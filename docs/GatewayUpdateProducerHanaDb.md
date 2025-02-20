# GatewayUpdateProducerHanaDb

gatewayUpdateProducerHanaDb is a command that updates hanadb producer [Deprecated: Use dynamic-secret-update-hanadb command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**hana_dbname** | **str** | HanaDb Name | [optional] 
**hanadb_create_statements** | **str** | HanaDb Creation statements | [optional] 
**hanadb_host** | **str** | HanaDb Host | [optional] [default to '127.0.0.1']
**hanadb_password** | **str** | HanaDb Password | [optional] 
**hanadb_port** | **str** | HanaDb Port | [optional] [default to '443']
**hanadb_revocation_statements** | **str** | HanaDb Revocation statements | [optional] 
**hanadb_username** | **str** | HanaDb Username | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_db_schema** | **str** | The DB schema | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **List[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_update_producer_hana_db import GatewayUpdateProducerHanaDb

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUpdateProducerHanaDb from a JSON string
gateway_update_producer_hana_db_instance = GatewayUpdateProducerHanaDb.from_json(json)
# print the JSON string representation of the object
print(GatewayUpdateProducerHanaDb.to_json())

# convert the object into a dict
gateway_update_producer_hana_db_dict = gateway_update_producer_hana_db_instance.to_dict()
# create an instance of GatewayUpdateProducerHanaDb from a dict
gateway_update_producer_hana_db_from_dict = GatewayUpdateProducerHanaDb.from_dict(gateway_update_producer_hana_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


