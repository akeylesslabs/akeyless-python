# CreateAuthMethodK8S

createAuthMethodK8S is a command that creates a new auth method that will be able to authenticate using K8S. [Deprecated: Use auth-method-create-k8s command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expires** | **int** | Access expiration date in Unix timestamp (select 0 for access without expiry date) | [optional] [default to 0]
**audience** | **str** | The audience in the Kubernetes JWT that the access is restricted to | [optional] 
**audit_logs_claims** | **List[str]** | Subclaims to include in audit logs, e.g \&quot;--audit-logs-claims email --audit-logs-claims username\&quot; | [optional] 
**bound_ips** | **List[str]** | A CIDR whitelist with the IPs that the access is restricted to | [optional] 
**bound_namespaces** | **List[str]** | A list of namespaces that the access is restricted to | [optional] 
**bound_pod_names** | **List[str]** | A list of pod names that the access is restricted to | [optional] 
**bound_sa_names** | **List[str]** | A list of service account names that the access is restricted to | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Auth Method description | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the auth method would you like to be notified. | [optional] 
**force_sub_claims** | **bool** | if true: enforce role-association must include sub claims | [optional] 
**gen_key** | **str** | Automatically generate key-pair for K8S configuration. If set to false, a public key needs to be provided [true/false] | [optional] [default to 'true']
**gw_bound_ips** | **List[str]** | A CIDR whitelist with the GW IPs that the access is restricted to | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**jwt_ttl** | **int** | Jwt TTL | [optional] [default to 0]
**name** | **str** | Auth Method name | 
**product_type** | **List[str]** | Choose the relevant product type for the auth method [sm, sra, pm, dp, ca] | [optional] 
**public_key** | **str** | Base64-encoded or PEM formatted public key data for K8S authentication method is required [RSA2048] | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_auth_method_k8_s import CreateAuthMethodK8S

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthMethodK8S from a JSON string
create_auth_method_k8_s_instance = CreateAuthMethodK8S.from_json(json)
# print the JSON string representation of the object
print(CreateAuthMethodK8S.to_json())

# convert the object into a dict
create_auth_method_k8_s_dict = create_auth_method_k8_s_instance.to_dict()
# create an instance of CreateAuthMethodK8S from a dict
create_auth_method_k8_s_from_dict = CreateAuthMethodK8S.from_dict(create_auth_method_k8_s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


