# CreateAuthMethodHuawei

createAuthMethodHuawei is a command that creates a new auth method that will be able to authenticate using Huawei credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**auth_url** | **str** | sts URL | [optional] [default to 'https://iam.myhwclouds.com:443/v3']
**bound_domain_id** | **list[str]** | A list of domain IDs that the access is restricted to | [optional] 
**bound_domain_name** | **list[str]** | A list of domain names that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist of the IPs that the access is restricted to | [optional] 
**bound_tenant_id** | **list[str]** | A list of full tenant ids that the access is restricted to | [optional] 
**bound_tenant_name** | **list[str]** | A list of full tenant names that the access is restricted to | [optional] 
**bound_user_id** | **list[str]** | A list of full user ids that the access is restricted to | [optional] 
**bound_user_name** | **list[str]** | A list of full user-name that the access is restricted to | [optional] 
**name** | **str** | Auth Method name | 
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


