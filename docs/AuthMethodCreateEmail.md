# AuthMethodCreateEmail

authMethodCreateEmail is a command that creates a new auth method that will be able to authenticate using email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**email** | **str** | An email address to be invited to have access | 
**enable_mfa** | **str** | Enable MFA for this authentication method [True / False] | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**mfa_type** | **str** | Enable two-factor-authentication via [email/auth app] | [optional] [default to 'email']
**name** | **str** | Auth Method name | 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.auth_method_create_email import AuthMethodCreateEmail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethodCreateEmail from a JSON string
auth_method_create_email_instance = AuthMethodCreateEmail.from_json(json)
# print the JSON string representation of the object
print(AuthMethodCreateEmail.to_json())

# convert the object into a dict
auth_method_create_email_dict = auth_method_create_email_instance.to_dict()
# create an instance of AuthMethodCreateEmail from a dict
auth_method_create_email_from_dict = AuthMethodCreateEmail.from_dict(auth_method_create_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


