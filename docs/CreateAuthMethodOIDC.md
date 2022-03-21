# CreateAuthMethodOIDC

createAuthMethodOIDC is a command that creates a new auth method that will be available to authenticate using OIDC.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_redirect_uri** | **list[str]** | Allowed redirect URIs after the authentication | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OIDC, OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


