# CreateAuthMethodAzureAD

createAuthMethodAzureAD is a command that creates a new auth method that will be able to authenticate using Azure Active Directory credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience in the JWT | [optional] [default to 'https://management.azure.com/']
**bound_group_id** | **list[str]** | A list of group ids that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist of the IPs that the access is restricted to | [optional] 
**bound_providers** | **list[str]** | A list of resource providers that the access is restricted to (e.g, Microsoft.Compute, Microsoft.ManagedIdentity, etc) | [optional] 
**bound_resource_id** | **list[str]** | A list of full resource ids that the access is restricted to | [optional] 
**bound_resource_names** | **list[str]** | A list of resource names that the access is restricted to (e.g, a virtual machine name, scale set name, etc). | [optional] 
**bound_resource_types** | **list[str]** | A list of resource types that the access is restricted to (e.g, virtualMachines, userAssignedIdentities, etc) | [optional] 
**bound_rg_id** | **list[str]** | A list of resource groups that the access is restricted to | [optional] 
**bound_spid** | **list[str]** | A list of service principal IDs that the access is restricted to | [optional] 
**bound_sub_id** | **list[str]** | A list of subscription ids that the access is restricted to | [optional] 
**bound_tenant_id** | **str** | The Azure tenant id that the access is restricted to | 
**issuer** | **str** | Issuer URL | [optional] [default to 'https://sts.windows.net/---bound_tenant_id---']
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] [default to 'https://login.microsoftonline.com/common/discovery/keys']
**name** | **str** | Auth Method name | 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


