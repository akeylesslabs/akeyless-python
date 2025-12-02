# AuthMethodUpdateSAML

authMethodUpdateSAML is a command that updates a new auth method that will be available to authenticate using SAML.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_client_type** | **list[str]** |  | [optional] 
**allowed_redirect_uri** | **list[str]** | Allowed redirect URIs after the authentication | [optional] 
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**idp_metadata_url** | **str** | IDP metadata url | [optional] 
**idp_metadata_xml_data** | **str** | IDP metadata xml data | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **list[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**subclaims_delimiters** | **list[str]** | A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


