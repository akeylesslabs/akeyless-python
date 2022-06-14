# UpdateAuthMethodUniversalIdentity

updateAuthMethodUniversalIdentity is a command that updates a new auth method that will be able to authenticate using Akeyless Universal Identity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**deny_inheritance** | **bool** | Deny from root to create children | [optional] 
**deny_rotate** | **bool** | Deny from the token to rotate | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**jwt_ttl** | **int** | Jwt TTL | [optional] 
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | Token ttl | [optional] [default to 60]
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


