# GatewayCreateProducerNativeK8S

gatewayCreateProducerNativeK8S is a command that creates k8s producer [Deprecated: Use dynamic-secret-create-k8s command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**k8s_allowed_namespaces** | **str** | Comma-separated list of allowed K8S namespaces for the generated ServiceAccount (relevant only for k8s-service-account-type&#x3D;dynamic) | [optional] 
**k8s_cluster_ca_cert** | **str** | K8S cluster CA certificate | [optional] 
**k8s_cluster_endpoint** | **str** | K8S cluster URL endpoint | [optional] 
**k8s_cluster_name** | **str** | K8S cluster name | [optional] 
**k8s_cluster_token** | **str** | K8S cluster Bearer token | [optional] 
**k8s_namespace** | **str** | K8S Namespace where the ServiceAccount exists. | [optional] 
**k8s_predefined_role_name** | **str** | The pre-existing Role or ClusterRole name to bind the generated ServiceAccount to (relevant only for k8s-service-account-type&#x3D;dynamic) | [optional] 
**k8s_predefined_role_type** | **str** | Specifies the type of the pre-existing K8S role [Role, ClusterRole] (relevant only for k8s-service-account-type&#x3D;dynamic) | [optional] 
**k8s_rolebinding_yaml_def** | **str** | Path to yaml file that contains definitions of K8S role and role binding (relevant only for k8s-service-account-type&#x3D;dynamic) | [optional] 
**k8s_service_account** | **str** | K8S ServiceAccount to extract token from. | [optional] 
**k8s_service_account_type** | **str** | K8S ServiceAccount type [fixed, dynamic]. | [optional] 
**name** | **str** | Dynamic secret name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**secure_access_allow_port_forwading** | **bool** | Enable Port forwarding while using CLI access | [optional] 
**secure_access_bastion_issuer** | **str** | Deprecated. use secure-access-certificate-issuer | [optional] 
**secure_access_certificate_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Secure Access | [optional] 
**secure_access_cluster_endpoint** | **str** | The K8s cluster endpoint URL | [optional] 
**secure_access_dashboard_url** | **str** | The K8s dashboard url | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_web** | **bool** | Enable Web Secure Remote Access | [optional] [default to False]
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**use_gw_service_account** | **bool** | Use the GW&#39;s service account | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

## Example

```python
from akeyless.models.gateway_create_producer_native_k8_s import GatewayCreateProducerNativeK8S

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateProducerNativeK8S from a JSON string
gateway_create_producer_native_k8_s_instance = GatewayCreateProducerNativeK8S.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateProducerNativeK8S.to_json())

# convert the object into a dict
gateway_create_producer_native_k8_s_dict = gateway_create_producer_native_k8_s_instance.to_dict()
# create an instance of GatewayCreateProducerNativeK8S from a dict
gateway_create_producer_native_k8_s_from_dict = GatewayCreateProducerNativeK8S.from_dict(gateway_create_producer_native_k8_s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


