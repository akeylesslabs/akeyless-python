# CreateDBTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_defined_connection_type** | **str** |  | [optional] 
**azure_client_id** | **str** | (Optional) Client id (relevant for \&quot;cloud-service-provider\&quot; only) | [optional] 
**azure_client_secret** | **str** | (Optional) Client secret (relevant for \&quot;cloud-service-provider\&quot; only) | [optional] 
**azure_tenant_id** | **str** | (Optional) Tenant id (relevant for \&quot;cloud-service-provider\&quot; only) | [optional] 
**cloud_service_provider** | **str** | (Optional) Cloud service provider (currently only supports Azure) | [optional] 
**cluster_mode** | **bool** | Cluster Mode | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**connection_type** | **str** | (Optional) Type of connection to mssql database [credentials/cloud-identity] | [default to 'credentials']
**db_name** | **str** |  | [optional] 
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**db_type** | **str** |  | 
**description** | **str** | Description of the object | [optional] 
**host** | **str** |  | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**mongodb_atlas** | **bool** |  | [optional] 
**mongodb_atlas_api_private_key** | **str** | MongoDB Atlas private key | [optional] 
**mongodb_atlas_api_public_key** | **str** | MongoDB Atlas public key | [optional] 
**mongodb_atlas_project_id** | **str** | MongoDB Atlas project ID | [optional] 
**mongodb_default_auth_db** | **str** | MongoDB server default authentication database | [optional] 
**mongodb_uri_options** | **str** | MongoDB server URI options | [optional] 
**name** | **str** | Target name | 
**oracle_service_name** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**pwd** | **str** |  | [optional] 
**snowflake_account** | **str** |  | [optional] 
**snowflake_api_private_key** | **str** | RSA Private key (base64 encoded) | [optional] 
**snowflake_api_private_key_password** | **str** | The Private key passphrase | [optional] 
**ssl** | **bool** | Enable/Disable SSL [true/false] | [optional] [default to False]
**ssl_certificate** | **str** | SSL connection certificate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


