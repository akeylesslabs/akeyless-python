# GatewayAddAllowedManagementAccess

gatewayAddAllowedManagementAccess is a command that adds sub-admins
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_gw_api** | **bool** |  | [optional] 
**allow_gw_login** | **bool** |  | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**sub_admin_access_id** | **str** | SubAdmins to add | 
**sub_claims** | **dict(str, str)** | key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


