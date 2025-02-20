# UpdateAuthMethodOIDC

updateAuthMethodOIDC is a command that updates a new auth method that will be available to authenticate using OIDC. [Deprecated: Use auth-method-update-oidc command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_redirect_uri** | **List[str]** | Allowed redirect URIs after the authentication | [optional] 
**audience** | **str** | Audience claim to be used as part of the authentication flow. In case set, it must match the one configured on the Identity Provider&#39;s Application | [optional] 
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**issuer** | **str** | Issuer URL | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**required_scopes** | **List[str]** | RequiredScopes is a list of required scopes that the oidc method will request from the oidc provider and the user must approve | [optional] 
**required_scopes_prefix** | **str** | RequiredScopesPrefix is a a prefix to add to all required-scopes when requesting them from the oidc server (for example, azures&#39; Application ID URI) | [optional] 
**subclaims_delimiters** | **List[str]** | A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OIDC, OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

## Example

```python
from akeyless.models.update_auth_method_oidc import UpdateAuthMethodOIDC

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthMethodOIDC from a JSON string
update_auth_method_oidc_instance = UpdateAuthMethodOIDC.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthMethodOIDC.to_json())

# convert the object into a dict
update_auth_method_oidc_dict = update_auth_method_oidc_instance.to_dict()
# create an instance of UpdateAuthMethodOIDC from a dict
update_auth_method_oidc_from_dict = UpdateAuthMethodOIDC.from_dict(update_auth_method_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


