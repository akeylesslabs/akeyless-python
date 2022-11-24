# OIDCAccessRules

OIDCAccessRules contains access rules specific to Open Id Connect authentication method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_ur_is** | **list[str]** | Allowed redirect URIs after the authentication | [optional] 
**audience** | **str** | Audience claim to be used as part of the authentication flow. In case set, it must match the one configured on the Identity Provider&#39;s Application | [optional] 
**bound_claims** | [**list[OIDCCustomClaim]**](OIDCCustomClaim.md) | The claims that login is restricted to. | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret | [optional] 
**is_internal** | **bool** | IsInternal indicates whether this is an internal Auth Method where the client has no control over it, or it was created by the client e.g - Sign In with Google will create an OIDC Auth Method with IsInternal&#x3D;true | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**required_scopes** | **list[str]** | A list of required scopes to request from the oidc provider, and to check on the token | [optional] 
**required_scopes_prefix** | **str** | A prefix to add to the required scopes (for example, azures&#39; Application ID URI) | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


