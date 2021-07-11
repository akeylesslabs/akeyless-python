# UpdateDBTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment about the target | [optional] 
**db_name** | **str** |  | [optional] 
**db_server_certificates** | **str** | (Optional) DB server certificates | [optional] 
**db_server_name** | **str** | (Optional) Server name for certificate verification | [optional] 
**db_type** | **str** |  | 
**host** | **str** |  | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**mongodb_atlas** | **bool** |  | [optional] 
**mongodb_atlas_api_private_key** | **str** | MongoDB Atlas private key | [optional] 
**mongodb_atlas_api_public_key** | **str** | MongoDB Atlas public key | [optional] 
**mongodb_atlas_project_id** | **str** | MongoDB Atlas project ID | [optional] 
**mongodb_default_auth_db** | **str** | MongoDB server default authentication database | [optional] 
**mongodb_host_port** | **str** | MongoDB server host and port | [optional] 
**mongodb_password** | **str** | MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters | [optional] 
**mongodb_server_uri** | **str** | MongoDB server URI | [optional] 
**mongodb_uri_options** | **str** | MongoDB server URI options | [optional] 
**mongodb_username** | **str** | MongoDB server username | [optional] 
**name** | **str** | Target name | 
**new_name** | **str** | New target name | [optional] 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**port** | **str** |  | [optional] 
**pwd** | **str** |  | [optional] 
**snowflake_account** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_version** | **bool** | Create new version for the target | [optional] [default to False]
**user_name** | **str** |  | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


