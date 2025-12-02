# DynamicSecretUpdateMongoDb

dynamicSecretUpdateMongoDb is a command that updates either mongodb  dynamic secret or mongodb atlas dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**mongodb_atlas_api_private_key** | **str** | MongoDB Atlas private key | [optional] 
**mongodb_atlas_api_public_key** | **str** | MongoDB Atlas public key | [optional] 
**mongodb_atlas_project_id** | **str** | MongoDB Atlas project ID | [optional] 
**mongodb_custom_data** | **str** | MongoDB custom data | [optional] 
**mongodb_default_auth_db** | **str** | MongoDB server default authentication database | [optional] 
**mongodb_host_port** | **str** | MongoDB server host and port | [optional] 
**mongodb_name** | **str** | MongoDB Name | [optional] 
**mongodb_password** | **str** | MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters | [optional] 
**mongodb_roles** | **str** | MongoDB Roles | [optional] [default to '[]']
**mongodb_scopes** | **str** | MongoDB Scopes (Atlas only) | [optional] 
**mongodb_server_uri** | **str** | MongoDB server URI | [optional] 
**mongodb_uri_options** | **str** | MongoDB server URI options | [optional] 
**mongodb_username** | **str** | MongoDB server username | [optional] 
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**password_length** | **str** | The length of the password to be generated | [optional] 
**producer_encryption_key_name** | **str** | Encrypt producer with following key | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_db_name** | **str** | The DB name (relevant only for DB Dynamic-Secret) | [optional] 
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


