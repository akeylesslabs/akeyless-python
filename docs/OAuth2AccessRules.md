# OAuth2AccessRules

OAuth2AccessRules contains access rules specific to OAuth2 authentication method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | The audience in the JWT. | [optional] 
**bound_claims** | [**list[OAuth2CustomClaim]**](OAuth2CustomClaim.md) | The claims that login is restricted to. | [optional] 
**bound_clients_id** | **list[str]** | The clients ids that login is restricted to. | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


