# AuthMethodUpdateLdap

authMethodUpdateLdap is a command that updates a new auth method that will be able to authenticate using LDAP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gen_key** | **str** | Automatically generate key-pair for LDAP configuration. If set to false, a public key needs to be provided [true/false] | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**public_key_data** | **str** | A public key generated for LDAP authentication method on Akeyless in base64 or PEM format [RSA2048] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \&quot;sub claim\&quot; that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization. | [optional] [default to 'users']

## Example

```python
from akeyless.models.auth_method_update_ldap import AuthMethodUpdateLdap

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodUpdateLdap from a JSON string
auth_method_update_ldap_instance = AuthMethodUpdateLdap.from_json(json)
# print the JSON string representation of the object
print(AuthMethodUpdateLdap.to_json())

# convert the object into a dict
auth_method_update_ldap_dict = auth_method_update_ldap_instance.to_dict()
# create an instance of AuthMethodUpdateLdap from a dict
auth_method_update_ldap_from_dict = AuthMethodUpdateLdap.from_dict(auth_method_update_ldap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


