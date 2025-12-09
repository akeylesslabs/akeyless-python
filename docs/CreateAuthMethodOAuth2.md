# CreateAuthMethodOAuth2

createAuthMethodOAuth2 is a command that creates a new auth method that will be able to authenticate using Oauth2. [Deprecated: Use auth-method-create-oauth2 command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_client_type** | **list[str]** | limit the auth method usage for specific client types [cli,ui,gateway-admin,sdk,mobile,extension] | [optional] 
**audience** | **str** | The audience in the JWT | [optional] 
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_client_ids** | **list[str]** | The clients ids that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**cert** | **str** | CertificateFile Path to a file that contain the certificate in a PEM format. | [optional] 
**cert_file_data** | **str** | CertificateFileData PEM Certificate in a Base64 format. | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gateway_url** | **str** | Akeyless Gateway URL (Configuration Management port). Relevant only when the jwks-uri is accessible only from the gateway. | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwks_json_data** | **str** | The JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. base64 encoded string | [optional] 
**jwks_uri** | **str** | The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. | [optional] 
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**product_type** | **list[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**subclaims_delimiters** | **list[str]** | A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


