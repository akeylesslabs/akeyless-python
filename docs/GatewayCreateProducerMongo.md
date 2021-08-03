# GatewayCreateProducerMongo

gatewayCreateProducerMongo is a command that creates either mongodb  producer or mongodb atlas producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongodb_atlas_api_private_key** | **str** | MongoDB Atlas private key | [optional] 
**mongodb_atlas_api_public_key** | **str** | MongoDB Atlas public key | [optional] 
**mongodb_atlas_project_id** | **str** | MongoDB Atlas project ID | [optional] 
**mongodb_default_auth_db** | **str** | MongoDB server default authentication database | [optional] 
**mongodb_host_port** | **str** | MongoDB server host and port | [optional] 
**mongodb_name** | **str** | MongoDB Name | 
**mongodb_password** | **str** | MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters | [optional] 
**mongodb_roles** | **str** | MongoDB Roles | [optional] [default to '[]']
**mongodb_server_uri** | **str** | MongoDB server URI | [optional] 
**mongodb_uri_options** | **str** | MongoDB server URI options | [optional] 
**mongodb_username** | **str** | MongoDB server username | [optional] 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Encrypt producer with following key | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


