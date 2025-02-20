# AuthMethodUpdateKerberos

authMethodUpdateKerberos is a command that updates an auth method that will be able to authenticate using Kerberos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bind_dn** | **str** |  | [optional] 
**bind_dn_password** | **str** |  | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**group_attr** | **str** |  | [optional] 
**group_dn** | **str** |  | [optional] 
**group_filter** | **str** |  | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**keytab_file_data** | **str** |  | [optional] 
**keytab_file_path** | **str** |  | [optional] 
**krb5_conf_data** | **str** |  | [optional] 
**krb5_conf_path** | **str** |  | [optional] 
**ldap_anonymous_search** | **bool** |  | [optional] 
**ldap_ca_cert** | **str** |  | [optional] 
**ldap_url** | **str** |  | [optional] 
**name** | **str** | Auth Method name | 
**new_name** | **str** |  | [optional] 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**subclaims_delimiters** | **List[str]** | A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**unique_identifier** | **str** | A unique identifier (ID) value which is a \&quot;sub claim\&quot; name that contains details uniquely identifying that resource. This \&quot;sub claim\&quot; is used to distinguish between different identities. | [optional] 
**user_attribute** | **str** |  | [optional] 
**user_dn** | **str** |  | [optional] 

## Example

```python
from akeyless.models.auth_method_update_kerberos import AuthMethodUpdateKerberos

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodUpdateKerberos from a JSON string
auth_method_update_kerberos_instance = AuthMethodUpdateKerberos.from_json(json)
# print the JSON string representation of the object
print(AuthMethodUpdateKerberos.to_json())

# convert the object into a dict
auth_method_update_kerberos_dict = auth_method_update_kerberos_instance.to_dict()
# create an instance of AuthMethodUpdateKerberos from a dict
auth_method_update_kerberos_from_dict = AuthMethodUpdateKerberos.from_dict(auth_method_update_kerberos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


