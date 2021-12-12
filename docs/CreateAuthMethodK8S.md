# CreateAuthMethodK8S

createAuthMethodK8S is a command that creates a new auth method that will be able to authenticate using K8S.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience in the Kubernetes JWT that the access is restricted to | [optional] 
**bound_ips** | **list[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_namespaces** | **list[str]** | A list of namespaces that the access is restricted to | [optional] 
**bound_pod_names** | **list[str]** | A list of pod names that the access is restricted to | [optional] 
**bound_sa_names** | **list[str]** | A list of service account names that the access is restricted to | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gen_key** | **str** | If this flag is set to true, there is no need to manually provide a public key for the Kubernetes Auth Method, and instead, a key pair, will be generated as part of the command and the private part of the key will be returned (the private key is required for the K8S Auth Config in the Akeyless Gateway) | [optional] [default to 'true']
**name** | **str** | Auth Method name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**public_key** | **str** | Base64-encoded public key text for K8S authentication method is required [RSA2048] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


