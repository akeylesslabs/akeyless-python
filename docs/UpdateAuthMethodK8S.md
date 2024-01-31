# UpdateAuthMethodK8S

updateAuthMethodK8S is a command that updates a new auth method that will be able to authenticate using K8S.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience in the Kubernetes JWT that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_namespaces** | **list[str]** | A list of namespaces that the access is restricted to | [optional] 
**bound_pod_names** | **list[str]** | A list of pod names that the access is restricted to | [optional] 
**bound_sa_names** | **list[str]** | A list of service account names that the access is restricted to | [optional] 
**description** | **str** | Auth Method description | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gen_key** | **str** | Automatically generate key-pair for K8S configuration. If set to false, a public key needs to be provided [true/false] | [optional] 
**gw_bound_ips** | **list[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**new_name** | **str** | Auth Method new name | [optional] 
**public_key** | **str** | Base64-encoded or PEM formatted public key data for K8S authentication method is required [RSA2048] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


