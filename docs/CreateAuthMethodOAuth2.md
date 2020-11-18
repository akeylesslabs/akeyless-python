# CreateAuthMethodOAuth2

createAuthMethodOAuth2 is a command that creates a new auth method that will be able to authenticate using OpenID/Oauth2.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience in the JWT | [optional] 
**bound_client_ids** | **list[str]** | The clients ids that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist of the IPs that the access is restricted to | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | 
**name** | **str** | Auth Method name | 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


