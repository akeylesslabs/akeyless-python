# GatewayCreateProducerAzure

gatewayCreateProducerAzure is a command that creates azure producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_obj_id** | **str** | Azure App Object Id | [optional] 
**azure_client_id** | **str** | Azure Client ID | [optional] 
**azure_client_secret** | **str** | Azure Client Secret | [optional] 
**azure_tenant_id** | **str** | Azure Tenant ID | [optional] 
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_web** | **bool** |  | [optional] 
**secure_access_web_browsing** | **bool** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_group_obj_id** | **str** | User Group Object Id | [optional] 
**user_portal_access** | **bool** | Azure User portal access | [optional] [default to False]
**user_principal_name** | **str** | User Principal Name | [optional] 
**user_programmatic_access** | **bool** | Azure User programmatic access | [optional] [default to True]
**user_role_template_id** | **str** | User Role Template Id | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


