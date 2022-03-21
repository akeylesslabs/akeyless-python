# OIDCAccessRules

OIDCAccessRules contains access rules specific to Open Id Connect authentication method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_ur_is** | **list[str]** | Allowed redirect URIs after the authentication | [optional] 
**bound_claims** | [**list[OIDCCustomClaim]**](OIDCCustomClaim.md) | The claims that login is restricted to. | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret | [optional] 
**is_internal** | **bool** | IsInternal indicates whether this is an internal Auth Method where the client has no control over it, or it was created by the client e.g - Sign In with Google will create an OIDC Auth Method with IsInternal&#x3D;true | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


