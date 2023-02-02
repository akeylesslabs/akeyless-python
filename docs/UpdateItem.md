# UpdateItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**add_tag** | **list[str]** | List of the new tags that will be attached to this item | [optional] 
**cert_file_data** | **str** | PEM Certificate in a Base64 format. Used for updating RSA keys&#39; certificates. | [optional] 
**delete_protection** | **str** |  | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_metadata']
**json** | **bool** | Set output format to JSON | [optional] 
**name** | **str** | Current item name | 
**new_metadata** | **str** | Deprecated - use description | [optional] [default to 'default_metadata']
**new_name** | **str** | New item name | [optional] 
**rm_tag** | **list[str]** | List of the existent tags that will be removed from this item | [optional] 
**rotate_after_disconnect** | **str** | Rotate the value of the secret after SRA session ends | [optional] [default to 'false']
**secure_access_add_host** | **list[str]** |  | [optional] 
**secure_access_allow_external_user** | **str** |  | [optional] 
**secure_access_allow_port_forwading** | **bool** |  | [optional] 
**secure_access_aws_account_id** | **str** |  | [optional] 
**secure_access_aws_native_cli** | **bool** |  | [optional] 
**secure_access_aws_region** | **str** |  | [optional] 
**secure_access_bastion_api** | **str** |  | [optional] 
**secure_access_bastion_issuer** | **str** |  | [optional] 
**secure_access_bastion_ssh** | **str** |  | [optional] 
**secure_access_cluster_endpoint** | **str** |  | [optional] 
**secure_access_dashboard_url** | **str** |  | [optional] 
**secure_access_db_name** | **str** |  | [optional] 
**secure_access_db_schema** | **str** |  | [optional] 
**secure_access_enable** | **str** |  | [optional] 
**secure_access_host** | **list[str]** |  | [optional] 
**secure_access_rdp_domain** | **str** |  | [optional] 
**secure_access_rdp_user** | **str** |  | [optional] 
**secure_access_rm_host** | **list[str]** |  | [optional] 
**secure_access_ssh_creds** | **str** |  | [optional] 
**secure_access_ssh_creds_user** | **str** |  | [optional] 
**secure_access_url** | **str** |  | [optional] 
**secure_access_use_internal_bastion** | **bool** |  | [optional] 
**secure_access_web_browsing** | **bool** |  | [optional] 
**secure_access_web_proxy** | **bool** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


