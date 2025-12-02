# DynamicSecretUpdateMsSql

dynamicSecretUpdateMsSql is a command that updates mssql dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**mssql_allowed_db_names** | **str** | CSV of allowed DB names for runtime selection when getting the secret value. Empty &#x3D;&gt; use target DB only; \&quot;*\&quot; &#x3D;&gt; any DB allowed; One or more names &#x3D;&gt; user must choose from this list | [optional] 
**mssql_create_statements** | **str** | MSSQL Creation statements | [optional] 
**mssql_dbname** | **str** | MSSQL Name | [optional] 
**mssql_host** | **str** | MSSQL Host | [optional] [default to '127.0.0.1']
**mssql_password** | **str** | MSSQL Password | [optional] 
**mssql_port** | **str** | MSSQL Port | [optional] [default to '1433']
**mssql_revocation_statements** | **str** | MSSQL Revocation statements | [optional] 
**mssql_username** | **str** | MSSQL Username | [optional] 
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_db_name** | **str** | The DB name (relevant only for DB Dynamic-Secret) | [optional] 
**secure_access_db_schema** | **str** | The DB schema | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **list[str]** | Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts) | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


