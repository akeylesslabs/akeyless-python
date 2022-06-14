# GatewayCreateMigration

gatewayCreateMigration is a command that create migration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_key** | **str** | AWS Secret Access Key | [optional] 
**aws_key_id** | **str** | AWS Access Key ID | [optional] 
**aws_region** | **str** | AWS region | [optional] 
**azure_client_id** | **str** | Azure KV Access client ID | [optional] 
**azure_kv_name** | **str** | Azure Key Vault Name | [optional] 
**azure_secret** | **str** | Azure KV secret | [optional] 
**azure_tenant_id** | **str** | Azure KV Access tenant ID | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**hashi_json** | **str** | Import secret key as json value or independent secrets | [optional] 
**hashi_ns** | **list[str]** | Hashi namespaces | [optional] 
**hashi_token** | **str** | Hashi token | [optional] 
**hashi_url** | **str** | Hashi url | [optional] 
**k8s_ca_certificate** | **list[int]** | For Certificate Authentication method K8s Cluster CA certificate | [optional] 
**k8s_client_certificate** | **list[int]** | K8s Client certificate | [optional] 
**k8s_client_key** | **list[int]** | K8s Client key | [optional] 
**k8s_namespace** | **str** | K8s Namespace | [optional] 
**k8s_password** | **str** | K8s client password | [optional] 
**k8s_skip_system** | **bool** | K8s Skip Control Plane Secrets | [optional] 
**k8s_token** | **str** | For Token Authentication method K8s Bearer Token | [optional] 
**k8s_url** | **str** | K8s Endpoint URL | [optional] 
**k8s_username** | **str** | For Password Authentication method K8s client username | [optional] 
**name** | **str** | Migration name | 
**protection_key** | **str** | The name of the key that protects the classic key value (if empty, the account default key will be used) | [optional] 
**target_location** | **str** | Target location in Akeyless for imported secrets | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Migration type, can be: hashi/aws/gcp/k8s/azure_kv | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


