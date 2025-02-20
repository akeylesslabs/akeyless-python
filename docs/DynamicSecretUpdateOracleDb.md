# DynamicSecretUpdateOracleDb

dynamicSecretUpdateOracleDb is a command that updates oracle db dynamic secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**oracle_host** | **str** | Oracle Host | [optional] [default to '127.0.0.1']
**oracle_password** | **str** | Oracle Password | [optional] 
**oracle_port** | **str** | Oracle Port | [optional] [default to '1521']
**oracle_revocation_statements** | **str** | Oracle Revocation statements | [optional] 
**oracle_screation_statements** | **str** | Oracle Creation statements | [optional] 
**oracle_service_name** | **str** | Oracle DB Name | [optional] 
**oracle_username** | **str** | Oracle Username | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] [default to 'false']
**secure_access_host** | **List[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.dynamic_secret_update_oracle_db import DynamicSecretUpdateOracleDb

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSecretUpdateOracleDb from a JSON string
dynamic_secret_update_oracle_db_instance = DynamicSecretUpdateOracleDb.from_json(json)
# print the JSON string representation of the object
print(DynamicSecretUpdateOracleDb.to_json())

# convert the object into a dict
dynamic_secret_update_oracle_db_dict = dynamic_secret_update_oracle_db_instance.to_dict()
# create an instance of DynamicSecretUpdateOracleDb from a dict
dynamic_secret_update_oracle_db_from_dict = DynamicSecretUpdateOracleDb.from_dict(dynamic_secret_update_oracle_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


