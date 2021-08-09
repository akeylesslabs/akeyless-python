# GatewayCreateProducerRdp

gatewayCreateProducerRdp is a command that creates rdp producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_user_only** | **str** | Fixed user | [optional] [default to 'false']
**name** | **str** | Producer name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**rdp_admin_name** | **str** | RDP Admin Name | [optional] 
**rdp_admin_pwd** | **str** | RDP Admin password | [optional] 
**rdp_host_name** | **str** | Hostname | [optional] 
**rdp_host_port** | **str** | Port | [optional] [default to '22']
**rdp_user_groups** | **str** | Groups | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_rdp_domain** | **str** |  | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


