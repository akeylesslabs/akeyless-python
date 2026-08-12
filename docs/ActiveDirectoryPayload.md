# ActiveDirectoryPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_target_id** | **int** |  | [optional] 
**ai_certificate_discovery** | **bool** |  | [optional] 
**auto_rotate** | **bool** |  | [optional] 
**auto_rotate_interval_in_days** | **int** |  | [optional] 
**auto_rotate_rotation_hour** | **int** |  | [optional] 
**certificates_expiration_events** | [**list[CertificateExpirationEvent]**](CertificateExpirationEvent.md) |  | [optional] 
**certificates_path_template** | **str** |  | [optional] 
**computer_base_dn** | **str** |  | [optional] 
**discover_iis_apps** | **bool** |  | [optional] 
**discover_local_users** | **bool** | Deprecated | [optional] 
**discover_services** | **bool** |  | [optional] 
**discovery_types** | **list[str]** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**domain_server_targets_path_template** | **str** |  | [optional] 
**domain_users_rotated_secrets_path_template** | **str** |  | [optional] 
**enable_password_policy** | **bool** | EnablePasswordPolicy enables applying PasswordPolicy to newly created domain/local user rotated secrets. Pointer so omitted values are preserved on partial update (nil &#x3D; not provided). | [optional] 
**enable_rdp_sra** | **bool** |  | [optional] 
**local_users_ignore_list** | **dict(str, bool)** |  | [optional] 
**local_users_rotated_secrets_path_template** | **str** |  | [optional] 
**os_filter** | **str** |  | [optional] 
**password_policy** | [**PasswordPolicyInfo**](PasswordPolicyInfo.md) |  | [optional] 
**skip_dry_run** | **bool** | SkipDryRun enables skip_dry_run on newly created domain/local user rotated secrets. Pointer so omitted values are preserved on partial update (nil &#x3D; not provided). When false/unset, existing rotated-secret SkipDryRun values are left unchanged on sync. | [optional] 
**ssh_port** | **str** |  | [optional] 
**target_format** | **str** |  | [optional] 
**targets_type** | **str** |  | [optional] 
**user_base_dn** | **str** |  | [optional] 
**user_groups** | **list[str]** |  | [optional] 
**winrm_over_http** | **bool** |  | [optional] 
**winrm_port** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


