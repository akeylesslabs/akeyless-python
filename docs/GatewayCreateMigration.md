# GatewayCreateMigration

gatewayCreateMigration is a command that create migration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_1password_email** | **str** | 1Password user email to connect to the API | [optional] 
**_1password_password** | **str** | 1Password user password to connect to the API | [optional] 
**_1password_secret_key** | **str** | 1Password user secret key to connect to the API | [optional] 
**_1password_url** | **str** | 1Password api container url | [optional] 
**_1password_vaults** | **list[str]** | 1Password list of vault to get the items from | [optional] 
**ad_discover_services** | **str** | Enable/Disable discovery of Windows services from each domain server as part of the SSH/Windows Rotated Secrets. Default is false. (Relevant only for Active Directory migration) | [optional] [default to 'false']
**ad_discovery_types** | **list[str]** | Set migration discovery types (domain-users, computers, local-users). (Relevant only for Active Directory migration) | [optional] 
**ad_os_filter** | **str** | Filter by Operating System to run the migration, can be used with wildcards, e.g. SRV20* (Relevant only for Active Directory migration) | [optional] 
**ad_ssh_port** | **str** | Set the SSH Port for further connection to the domain servers. Default is port 22 (Relevant only for Active Directory migration) | [optional] [default to '22']
**ad_targets_type** | **str** | Set the target type of the domain servers [ssh/windows](Relevant only for Active Directory migration) | [optional] [default to 'windows']
**ad_winrm_over_http** | **str** | Use WinRM over HTTP, by default runs over HTTPS | [optional] [default to 'false']
**ad_winrm_port** | **str** | Set the WinRM Port for further connection to the domain servers. Default is 5986 (Relevant only for Active Directory migration) | [optional] [default to '5986']
**ad_auto_rotate** | **str** | Enable/Disable automatic/recurrent rotation for migrated secrets. Default is false: only manual rotation is allowed for migrated secrets. If set to true, this command should be combined with --ad-rotation-interval and --ad-rotation-hour parameters (Relevant only for Active Directory migration) | [optional] 
**ad_computer_base_dn** | **str** | Distinguished Name of Computer objects (servers) to search in Active Directory e.g.: CN&#x3D;Computers,DC&#x3D;example,DC&#x3D;com (Relevant only for Active Directory migration) | [optional] 
**ad_discover_local_users** | **str** | Enable/Disable discovery of local users from each domain server and migrate them as SSH/Windows Rotated Secrets. Default is false: only domain users will be migrated. Discovery of local users might require further installation of SSH on the servers, based on the supplied computer base DN. This will be implemented automatically as part of the migration process (Relevant only for Active Directory migration) Deprecated: use AdDiscoverTypes | [optional] 
**ad_domain_name** | **str** | Active Directory Domain Name (Relevant only for Active Directory migration) | [optional] 
**ad_domain_users_path_template** | **str** | Path location template for migrating domain users as Rotated Secrets e.g.: .../DomainUsers/{{USERNAME}} (Relevant only for Active Directory migration) | [optional] 
**ad_local_users_ignore** | **str** | Comma-separated list of Local Users which should not be migrated (Relevant only for Active Directory migration) | [optional] 
**ad_local_users_path_template** | **str** | Path location template for migrating domain users as Rotated Secrets e.g.: .../LocalUsers/{{COMPUTER_NAME}}/{{USERNAME}} (Relevant only for Active Directory migration) | [optional] 
**ad_rotation_hour** | **int** | The hour of the scheduled rotation in UTC (Relevant only for Active Directory migration) | [optional] 
**ad_rotation_interval** | **int** | The number of days to wait between every automatic rotation [1-365] (Relevant only for Active Directory migration) | [optional] 
**ad_sra_enable_rdp** | **str** | Enable/Disable RDP Secure Remote Access for the migrated local users rotated secrets. Default is false: rotated secrets will not be created with SRA (Relevant only for Active Directory migration) | [optional] 
**ad_target_name** | **str** | Active Directory LDAP Target Name. Server type should be Active Directory (Relevant only for Active Directory migration) | [optional] 
**ad_targets_path_template** | **str** | Path location template for migrating domain servers as SSH/Windows Targets e.g.: .../Servers/{{COMPUTER_NAME}} (Relevant only for Active Directory migration) | [optional] 
**ad_user_base_dn** | **str** | Distinguished Name of User objects to search in Active Directory, e.g.: CN&#x3D;Users,DC&#x3D;example,DC&#x3D;com (Relevant only for Active Directory migration) | [optional] 
**ad_user_groups** | **str** | Comma-separated list of domain groups from which privileged domain users will be migrated. If empty, migrate all users based on the --ad-user-base-dn (Relevant only for Active Directory migration) | [optional] 
**aws_key** | **str** | AWS Secret Access Key (relevant only for AWS migration) | [optional] 
**aws_key_id** | **str** | AWS Access Key ID with sufficient permissions to get all secrets, e.g. &#39;arn:aws:secretsmanager:[Region]:[AccountId]:secret:[/path/to/secrets/*]&#39; (relevant only for AWS migration) | [optional] 
**aws_region** | **str** | AWS region of the required Secrets Manager (relevant only for AWS migration) | [optional] [default to 'us-east-2']
**azure_client_id** | **str** | Azure Key Vault Access client ID, should be Azure AD App with a service principal (relevant only for Azure Key Vault migration) | [optional] 
**azure_kv_name** | **str** | Azure Key Vault Name (relevant only for Azure Key Vault migration) | [optional] 
**azure_secret** | **str** | Azure Key Vault secret (relevant only for Azure Key Vault migration) | [optional] 
**azure_tenant_id** | **str** | Azure Key Vault Access tenant ID (relevant only for Azure Key Vault migration) | [optional] 
**gcp_key** | **str** | Base64-encoded GCP Service Account private key text with sufficient permissions to Secrets Manager, Minimum required permission is Secret Manager Secret Accessor, e.g. &#39;roles/secretmanager.secretAccessor&#39; (relevant only for GCP migration) | [optional] 
**hashi_json** | **str** | Import secret key as json value or independent secrets (relevant only for HasiCorp Vault migration) [true/false] | [optional] [default to 'true']
**hashi_ns** | **list[str]** | HashiCorp Vault Namespaces is a comma-separated list of namespaces which need to be imported into Akeyless Vault. For every provided namespace, all its child namespaces are imported as well, e.g. nmsp/subnmsp1/subnmsp2,nmsp/anothernmsp. By default, import all namespaces (relevant only for HasiCorp Vault migration) | [optional] 
**hashi_token** | **str** | HashiCorp Vault access token with sufficient permissions to preform list &amp; read operations on secrets objects (relevant only for HasiCorp Vault migration) | [optional] 
**hashi_url** | **str** | HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 (relevant only for HasiCorp Vault migration) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
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
**protection_key** | **str** | The name of the key that protects the classic key value (if empty, the account default key will be used) | [optional] 
**si_auto_rotate** | **str** | Enable/Disable automatic/recurrent rotation for migrated secrets. Default is false: only manual rotation is allowed for migrated secrets. If set to true, this command should be combined with --si-rotation-interval and --si-rotation-hour parameters (Relevant only for Server Inventory migration) | [optional] 
**si_rotation_hour** | **int** | The hour of the scheduled rotation in UTC (Relevant only for Server Inventory migration) | [optional] 
**si_rotation_interval** | **int** | The number of days to wait between every automatic rotation [1-365] (Relevant only for Server Inventory migration) | [optional] 
**si_sra_enable_rdp** | **str** | Enable/Disable RDP Secure Remote Access for the migrated local users rotated secrets. Default is false: rotated secrets will not be created with SRA (Relevant only for Server Inventory migration) | [optional] [default to 'false']
**si_target_name** | **str** | SSH, Windows or Linked Target Name. (Relevant only for Server Inventory migration) | 
**si_user_groups** | **str** | Comma-separated list of groups to migrate users from. If empty, all users from all groups will be migrated (Relevant only for Server Inventory migration) | [optional] 
**si_users_ignore** | **str** | Comma-separated list of Local Users which should not be migrated (Relevant only for Server Inventory migration) | [optional] 
**si_users_path_template** | **str** | Path location template for migrating users as Rotated Secrets e.g.: .../Users/{{COMPUTER_NAME}}/{{USERNAME}} (Relevant only for Server Inventory migration) | 
**target_location** | **str** | Target location in Akeyless for imported secrets | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Migration type (hashi/aws/gcp/k8s/azure_kv/1password/active_directory) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


