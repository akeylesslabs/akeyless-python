# GatewayCreateProducerAzure

gatewayCreateProducerAzure is a command that creates azure producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_obj_id** | **str** | Azure App Object Id | [optional] 
**client_id** | **str** | Azure Client ID | 
**client_secret** | **str** | Azure Client Secret | 
**gateway_url** | **str** | Gateway url | [optional] [default to 'http://localhost:8000']
**name** | **str** | Producer name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tenant_id** | **str** | Azure Tenant ID | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_group_obj_id** | **str** | User Group Object Id | [optional] 
**user_portal_access** | **bool** | Azure User portal access | [optional] [default to False]
**user_principal_name** | **str** | User Principal Name | [optional] 
**user_programmatic_access** | **bool** | Azure User programmatic access | [optional] [default to True]
**user_role_template_id** | **str** | User Role Template Id | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


