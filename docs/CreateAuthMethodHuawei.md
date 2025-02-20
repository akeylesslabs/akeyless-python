# CreateAuthMethodHuawei

createAuthMethodHuawei is a command that creates a new auth method that will be able to authenticate using Huawei credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**auth_url** | **str** | sts URL | [optional] [default to 'https://iam.myhwclouds.com:443/v3']
**bound_domain_id** | **List[str]** | A list of domain IDs that the access is restricted to | [optional] 
**bound_domain_name** | **List[str]** | A list of domain names that the access is restricted to | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_tenant_id** | **List[str]** | A list of full tenant ids that the access is restricted to | [optional] 
**bound_tenant_name** | **List[str]** | A list of full tenant names that the access is restricted to | [optional] 
**bound_user_id** | **List[str]** | A list of full user ids that the access is restricted to | [optional] 
**bound_user_name** | **List[str]** | A list of full user-name that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_auth_method_huawei import CreateAuthMethodHuawei

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodHuawei from a JSON string
create_auth_method_huawei_instance = CreateAuthMethodHuawei.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodHuawei.to_json())

# convert the object into a dict
create_auth_method_huawei_dict = create_auth_method_huawei_instance.to_dict()
# create an instance of CreateAuthMethodHuawei from a dict
create_auth_method_huawei_from_dict = CreateAuthMethodHuawei.from_dict(create_auth_method_huawei_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


