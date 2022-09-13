# GatewayCreateMigration

gatewayCreateMigration is a command that create migration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_key** | **str** | AWS Secret Access Key (relevant only for AWS migration) | [optional] 
**aws_key_id** | **str** | AWS Access Key ID with sufficient permissions to get all secrets, e.g. &#39;arn:aws:secretsmanager:[Region]:[AccountId]:secret:[/path/to/secrets/*]&#39; (relevant only for AWS migration) | [optional] 
**aws_region** | **str** | AWS region of the required Secrets Manager (relevant only for AWS migration) | [optional] 
**azure_client_id** | **str** | Azure Key Vault Access client ID, should be Azure AD App with a service principal (relevant only for Azure Key Vault migration) | [optional] 
**azure_kv_name** | **str** | Azure Key Vault Name (relevant only for Azure Key Vault migration) | [optional] 
**azure_secret** | **str** | Azure Key Vault secret (relevant only for Azure Key Vault migration) | [optional] 
**azure_tenant_id** | **str** | Azure Key Vault Access tenant ID (relevant only for Azure Key Vault migration) | [optional] 
**gcp_key** | **str** | Base64-encoded GCP Service Account private key text with sufficient permissions to Secrets Manager, Minimum required permission is Secret Manager Secret Accessor, e.g. &#39;roles/secretmanager.secretAccessor&#39; (relevant only for GCP migration) | [optional] 
**hashi_json** | **str** | Import secret key as json value or independent secrets (relevant only for HasiCorp Vault migration) | [optional] 
**hashi_ns** | **list[str]** | HashiCorp Vault Namespaces is a comma-separated list of namespaces which need to be imported into Akeyless Vault. For every provided namespace, all its child namespaces are imported as well, e.g. nmsp/subnmsp1/subnmsp2,nmsp/anothernmsp. By default, import all namespaces (relevant only for HasiCorp Vault migration) | [optional] 
**hashi_token** | **str** | HashiCorp Vault access token with sufficient permissions to preform list &amp; read operations on secrets objects (relevant only for HasiCorp Vault migration) | [optional] 
**hashi_url** | **str** | HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 (relevant only for HasiCorp Vault migration) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**k8s_ca_certificate** | **list[int]** | For Certificate Authentication method K8s Cluster CA certificate (relevant only for K8s migration with Certificate Authentication method) | [optional] 
**k8s_client_certificate** | **list[int]** | K8s Client certificate with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Certificate Authentication method) | [optional] 
**k8s_client_key** | **list[int]** | K8s Client key (relevant only for K8s migration with Certificate Authentication method) | [optional] 
**k8s_namespace** | **str** | K8s Namespace, Use this field to import secrets from a particular namespace only. By default, the secrets are imported from all namespaces (relevant only for K8s migration) | [optional] 
**k8s_password** | **str** | K8s Client password (relevant only for K8s migration with Password Authentication method) | [optional] 
**k8s_skip_system** | **bool** | K8s Skip Control Plane Secrets, This option allows to avoid importing secrets from system namespaces (relevant only for K8s migration) | [optional] 
**k8s_token** | **str** | For Token Authentication method K8s Bearer Token with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Token Authentication method) | [optional] 
**k8s_url** | **str** | K8s API Server URL, e.g. https://k8s-api.mycompany.com:6443 (relevant only for K8s migration) | [optional] 
**k8s_username** | **str** | For Password Authentication method K8s Client username with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Password Authentication method) | [optional] 
**name** | **str** | Migration name | 
**op_email** | **str** | 1Password user email to connect to the API | [optional] 
**op_password** | **str** | 1Password user password to connect to the API | [optional] 
**op_secret_key** | **str** | 1Password user secret key to connect to the API | [optional] 
**op_url** | **str** | 1Password api container url | [optional] 
**op_vaults** | **list[str]** | 1Password list of vault to get the items from | [optional] 
**protection_key** | **str** | The name of the key that protects the classic key value (if empty, the account default key will be used) | [optional] 
**target_location** | **str** | Target location in Akeyless for imported secrets | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Migration type (hashi/aws/gcp/k8s/azure_kv/1password) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


