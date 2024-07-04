# CreateAuthMethodHuawei

createAuthMethodHuawei is a command that creates a new auth method that will be able to authenticate using Huawei credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audit_logs_claims** | **list[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**auth_url** | **str** | sts URL | [optional] [default to 'https://iam.myhwclouds.com:443/v3']
**bound_domain_id** | **list[str]** | A list of domain IDs that the access is restricted to | [optional] 
**bound_domain_name** | **list[str]** | A list of domain names that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_tenant_id** | **list[str]** | A list of full tenant ids that the access is restricted to | [optional] 
**bound_tenant_name** | **list[str]** | A list of full tenant names that the access is restricted to | [optional] 
**bound_user_id** | **list[str]** | A list of full user ids that the access is restricted to | [optional] 
**bound_user_name** | **list[str]** | A list of full user-name that the access is restricted to | [optional] 
**description** | **str** | Auth Method description | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**product_type** | **list[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


