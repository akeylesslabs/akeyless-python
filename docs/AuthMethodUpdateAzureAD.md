# AuthMethodUpdateAzureAD

authMethodUpdateAzureAD is a command that updates a new auth method that will be able to authenticate using Azure Active Directory credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | Deprecated (Deprecated) The audience in the JWT | [optional] [default to 'https://management.azure.com/']
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_group_id** | **list[str]** | A list of group ids that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_providers** | **list[str]** | A list of resource providers that the access is restricted to (e.g, Microsoft.Compute, Microsoft.ManagedIdentity, etc) | [optional] 
**bound_resource_id** | **list[str]** | A list of full resource ids that the access is restricted to | [optional] 
**bound_resource_names** | **list[str]** | A list of resource names that the access is restricted to (e.g, a virtual machine name, scale set name, etc). | [optional] 
**bound_resource_types** | **list[str]** | A list of resource types that the access is restricted to (e.g, virtualMachines, userAssignedIdentities, etc) | [optional] 
**bound_rg_id** | **list[str]** | A list of resource groups that the access is restricted to | [optional] 
**bound_spid** | **list[str]** | A list of service principal IDs that the access is restricted to | [optional] 
**bound_sub_id** | **list[str]** | A list of subscription ids that the access is restricted to | [optional] 
**bound_tenant_id** | **str** | The Azure tenant id that the access is restricted to | 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**issuer** | **str** | Issuer URL | [optional] [default to 'https://sts.windows.net/---bound_tenant_id---']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] [default to 'https://login.microsoftonline.com/common/discovery/keys']
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **list[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value which is a \&quot;sub claim\&quot; name that contains details uniquely identifying that resource. This \&quot;sub claim\&quot; is used to distinguish between different identities. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


