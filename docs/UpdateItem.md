# UpdateItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] 
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**cert_file_data** | **str** | PEM Certificate in a Base64 format. Used for updating RSA keys&#39; certificates. | [optional] 
**change_event** | **str** | Trigger an event when a secret value changed [true/false] (Relevant only for Static Secret) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_metadata']
**host_provider** | **str** | Host provider type [explicit/target], Relevant only for Secure Remote Access of ssh cert issuer and ldap rotated secret | [optional] [default to 'explicit']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Current item name | 
**new_metadata** | **str** | Deprecated - use description | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotate_after_disconnect** | **str** | Rotate the value of the secret after SRA session ends [true/false] | [optional] [default to 'false']
**secure_access_add_host** | **list[str]** | List of the new hosts that will be attached to SRA servers host | [optional] 
**secure_access_allow_external_user** | **str** | Allow providing external user for a domain users [true/false] | [optional] 
**secure_access_allow_port_forwading** | **bool** | Enable Port forwarding while using CLI access (relevant only for EKS/GKE/K8s Dynamic-Secret) | [optional] 
**secure_access_aws_account_id** | **str** | The AWS account id (relevant only for aws) | [optional] 
**secure_access_aws_native_cli** | **bool** | The AWS native cli (relevant only for aws) | [optional] 
**secure_access_aws_region** | **str** | The AWS region (relevant only for aws) | [optional] 
**secure_access_bastion_api** | **str** | Bastion&#39;s SSH control API endpoint. E.g. https://my.bastion:9900 (relevant only for ssh cert issuer) | [optional] 
**secure_access_bastion_issuer** | **str** | Path to the SSH Certificate Issuer for your Akeyless Bastion | [optional] 
**secure_access_bastion_ssh** | **str** | Bastion&#39;s SSH server. E.g. my.bastion:22 (relevant only for ssh cert issuer) | [optional] 
**secure_access_cluster_endpoint** | **str** | The K8s cluster endpoint URL (relevant only for EKS/GKE/K8s Dynamic-Secret) | [optional] 
**secure_access_dashboard_url** | **str** | The K8s dashboard url (relevant only for k8s) | [optional] 
**secure_access_db_name** | **str** | The DB name (relevant only for DB Dynamic-Secret) | [optional] 
**secure_access_db_schema** | **str** | The DB schema (relevant only for DB Dynamic-Secret) | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_host** | **list[str]** | Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers) | [optional] 
**secure_access_rd_gateway_server** | **str** | RD Gateway server (relevant only for rdp) | [optional] 
**secure_access_rdp_domain** | **str** | Required when the Dynamic Secret is used for a domain user (relevant only for RDP Dynamic-Secret) | [optional] 
**secure_access_rdp_user** | **str** | Override the RDP Domain username | [optional] 
**secure_access_rm_host** | **list[str]** | List of the existent hosts that will be removed from SRA servers host | [optional] 
**secure_access_ssh_creds** | **str** | Secret values contains SSH Credentials, either Private Key or Password [password/private-key] (relevant only for Static-Secret or Rotated-secret) | [optional] 
**secure_access_ssh_creds_user** | **str** | SSH username to connect to target server, must be in &#39;Allowed Users&#39; list (relevant only for ssh cert issuer) | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_use_internal_bastion** | **bool** | Use internal SSH Bastion | [optional] 
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless Web Access Bastion | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless Web Access Bastion | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


