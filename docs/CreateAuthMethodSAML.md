# CreateAuthMethodSAML

createAuthMethodSAML is a command that creates a new auth method that will be available to authenticate using SAML. [Deprecated: Use auth-method-create-saml command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**allowed_redirect_uri** | **List[str]** | Allowed redirect URIs after the authentication | [optional] 
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**idp_metadata_url** | **str** | IDP metadata url | [optional] 
**idp_metadata_xml_data** | **str** | IDP metadata xml data | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**subclaims_delimiters** | **List[str]** | A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | 

## Example

```python
from akeyless.models.create_auth_method_saml import CreateAuthMethodSAML

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodSAML from a JSON string
create_auth_method_saml_instance = CreateAuthMethodSAML.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodSAML.to_json())

# convert the object into a dict
create_auth_method_saml_dict = create_auth_method_saml_instance.to_dict()
# create an instance of CreateAuthMethodSAML from a dict
create_auth_method_saml_from_dict = CreateAuthMethodSAML.from_dict(create_auth_method_saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


