# DSProducerDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**admin_name** | **str** |  | [optional] 
**admin_pwd** | **str** |  | [optional] 
**admin_rotation_interval_days** | **int** |  | [optional] 
**allow_subdomains** | **bool** |  | [optional] 
**allowed_domains** | **str** |  | [optional] 
**artifactory_admin_apikey** | **str** |  | [optional] 
**artifactory_admin_username** | **str** |  | [optional] 
**artifactory_base_url** | **str** |  | [optional] 
**artifactory_token_audience** | **str** |  | [optional] 
**artifactory_token_scope** | **str** |  | [optional] 
**auto_generated_folder** | **str** |  | [optional] 
**aws_access_key_id** | **str** |  | [optional] 
**aws_access_mode** | **str** |  | [optional] 
**aws_region** | **str** |  | [optional] 
**aws_role_arns** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**aws_session_token** | **str** |  | [optional] 
**aws_user_console_access** | **bool** |  | [optional] 
**aws_user_groups** | **str** |  | [optional] 
**aws_user_policies** | **str** |  | [optional] 
**aws_user_programmatic_access** | **bool** |  | [optional] 
**azure_app_object_id** | **str** |  | [optional] 
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 
**azure_user_groups_obj_id** | **str** |  | [optional] 
**azure_user_portal_access** | **bool** |  | [optional] 
**azure_user_programmatic_access** | **bool** |  | [optional] 
**azure_user_roles_template_id** | **str** |  | [optional] 
**chef_organizations** | **str** |  | [optional] 
**chef_server_access_mode** | **str** |  | [optional] 
**chef_server_host_name** | **str** |  | [optional] 
**chef_server_key** | **str** |  | [optional] 
**chef_server_port** | **str** |  | [optional] 
**chef_server_url** | **str** |  | [optional] 
**chef_server_username** | **str** |  | [optional] 
**chef_skip_ssl** | **bool** |  | [optional] 
**create_cert_using_pki** | **bool** |  | [optional] 
**db_host_name** | **str** |  | [optional] 
**db_isolation_level** | **str** |  | [optional] 
**db_max_idle_conns** | **str** |  | [optional] 
**db_max_open_conns** | **str** |  | [optional] 
**db_name** | **str** |  | [optional] 
**db_port** | **str** |  | [optional] 
**db_pwd** | **str** |  | [optional] 
**db_server_certificates** | **str** | (Optional) DBServerCertificates defines the set of root certificate authorities that clients use when verifying server certificates. If DBServerCertificates is empty, TLS uses the host&#39;s root CA set. | [optional] 
**db_server_name** | **str** | (Optional) ServerName is used to verify the hostname on the returned certificates unless InsecureSkipVerify is given. It is also included in the client&#39;s handshake to support virtual hosting unless it is an IP address. | [optional] 
**db_user_name** | **str** |  | [optional] 
**dynamic_secret_id** | **int** |  | [optional] 
**dynamic_secret_key** | **str** |  | [optional] 
**dynamic_secret_name** | **str** |  | [optional] 
**dynamic_secret_type** | **str** |  | [optional] 
**eks_access_key_id** | **str** |  | [optional] 
**eks_assume_role** | **str** |  | [optional] 
**eks_cluster_ca_certificate** | **str** |  | [optional] 
**eks_cluster_endpoint** | **str** |  | [optional] 
**eks_cluster_name** | **str** |  | [optional] 
**eks_region** | **str** |  | [optional] 
**eks_secret_access_key** | **str** |  | [optional] 
**enable_admin_rotation** | **bool** |  | [optional] 
**failure_message** | **str** |  | [optional] 
**fixed_user_only** | **str** |  | [optional] 
**gke_cluster_ca_certificate** | **str** |  | [optional] 
**gke_cluster_compute_zone** | **str** |  | [optional] 
**gke_cluster_endpoint** | **str** |  | [optional] 
**gke_cluster_name** | **str** |  | [optional] 
**gke_project_id** | **str** |  | [optional] 
**gke_service_account_key** | **str** |  | [optional] 
**gke_service_account_name** | **str** |  | [optional] 
**groups** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**host_port** | **str** |  | [optional] 
**last_admin_rotation** | **int** |  | [optional] 
**mongodb_atlas_api_private_key** | **str** |  | [optional] 
**mongodb_atlas_api_public_key** | **str** |  | [optional] 
**mongodb_atlas_project_id** | **str** | mongodb atlas fields | [optional] 
**mongodb_db_name** | **str** | common fields | [optional] 
**mongodb_default_auth_db** | **str** |  | [optional] 
**mongodb_host_port** | **str** |  | [optional] 
**mongodb_is_atlas** | **bool** |  | [optional] 
**mongodb_password** | **str** |  | [optional] 
**mongodb_roles** | **str** |  | [optional] 
**mongodb_uri_connection** | **str** | mongodb fields | [optional] 
**mongodb_uri_options** | **str** |  | [optional] 
**mongodb_username** | **str** |  | [optional] 
**mssql_creation_statements** | **str** |  | [optional] 
**mssql_revocation_statements** | **str** |  | [optional] 
**mysql_creation_statements** | **str** |  | [optional] 
**postgres_creation_statements** | **str** |  | [optional] 
**rabbitmq_server_password** | **str** |  | [optional] 
**rabbitmq_server_uri** | **str** |  | [optional] 
**rabbitmq_server_user** | **str** |  | [optional] 
**rabbitmq_user_conf_permission** | **str** |  | [optional] 
**rabbitmq_user_read_permission** | **str** |  | [optional] 
**rabbitmq_user_tags** | **str** |  | [optional] 
**rabbitmq_user_vhost** | **str** |  | [optional] 
**rabbitmq_user_write_permission** | **str** |  | [optional] 
**root_first_in_chain** | **bool** |  | [optional] 
**should_stop** | **str** | TODO delete this after migration | [optional] 
**signer_key_name** | **str** |  | [optional] 
**store_private_key** | **bool** |  | [optional] 
**user_principal_name** | **str** |  | [optional] 
**user_ttl** | **str** |  | [optional] 
**venafi_api_key** | **str** |  | [optional] 
**venafi_zone** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

