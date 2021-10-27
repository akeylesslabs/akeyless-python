# akeyless.V2Api

All URIs are relative to *https://api.akeyless.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assoc_role_auth_method**](V2Api.md#assoc_role_auth_method) | **POST** /assoc-role-am | 
[**assoc_target_item**](V2Api.md#assoc_target_item) | **POST** /assoc-target-item | 
[**auth**](V2Api.md#auth) | **POST** /auth | 
[**configure**](V2Api.md#configure) | **POST** /configure | 
[**connect**](V2Api.md#connect) | **POST** /connect | 
[**create_artifactory_target**](V2Api.md#create_artifactory_target) | **POST** /create-artifactory-target | 
[**create_auth_method**](V2Api.md#create_auth_method) | **POST** /create-auth-method | 
[**create_auth_method_awsiam**](V2Api.md#create_auth_method_awsiam) | **POST** /create-auth-method-aws-iam | 
[**create_auth_method_azure_ad**](V2Api.md#create_auth_method_azure_ad) | **POST** /create-auth-method-azure-ad | 
[**create_auth_method_gcp**](V2Api.md#create_auth_method_gcp) | **POST** /create-auth-method-gcp | 
[**create_auth_method_huawei**](V2Api.md#create_auth_method_huawei) | **POST** /create-auth-method-huawei | 
[**create_auth_method_o_auth2**](V2Api.md#create_auth_method_o_auth2) | **POST** /create-auth-method-oauth2 | 
[**create_auth_method_oidc**](V2Api.md#create_auth_method_oidc) | **POST** /create-auth-method-oidc | 
[**create_auth_method_saml**](V2Api.md#create_auth_method_saml) | **POST** /create-auth-method-saml | 
[**create_auth_method_universal_identity**](V2Api.md#create_auth_method_universal_identity) | **POST** /create-auth-method-universal-identity | 
[**create_aws_target**](V2Api.md#create_aws_target) | **POST** /create-aws-target | 
[**create_azure_target**](V2Api.md#create_azure_target) | **POST** /create-azure-target | 
[**create_classic_key**](V2Api.md#create_classic_key) | **POST** /create-classic-key | 
[**create_db_target**](V2Api.md#create_db_target) | **POST** /create-db-target | 
[**create_dfc_key**](V2Api.md#create_dfc_key) | **POST** /create-dfc-key | 
[**create_dynamic_secret**](V2Api.md#create_dynamic_secret) | **POST** /create-dynamic-secret | 
[**create_eks_target**](V2Api.md#create_eks_target) | **POST** /create-eks-target | 
[**create_gcp_target**](V2Api.md#create_gcp_target) | **POST** /create-gcp-target | 
[**create_gke_target**](V2Api.md#create_gke_target) | **POST** /create-gke-target | 
[**create_key**](V2Api.md#create_key) | **POST** /create-key | 
[**create_native_k8_s_target**](V2Api.md#create_native_k8_s_target) | **POST** /create-k8s-target | 
[**create_pki_cert_issuer**](V2Api.md#create_pki_cert_issuer) | **POST** /create-pki-cert-issuer | 
[**create_rabbit_mq_target**](V2Api.md#create_rabbit_mq_target) | **POST** /create-rabbitmq-target | 
[**create_role**](V2Api.md#create_role) | **POST** /create-role | 
[**create_rotated_secret**](V2Api.md#create_rotated_secret) | **POST** /create-rotated-secret | 
[**create_secret**](V2Api.md#create_secret) | **POST** /create-secret | 
[**create_ssh_cert_issuer**](V2Api.md#create_ssh_cert_issuer) | **POST** /create-ssh-cert-issuer | 
[**create_ssh_target**](V2Api.md#create_ssh_target) | **POST** /create-ssh-target | 
[**create_web_target**](V2Api.md#create_web_target) | **POST** /create-web-target | 
[**createldap_target**](V2Api.md#createldap_target) | **POST** /create-ldap-target | 
[**decrypt**](V2Api.md#decrypt) | **POST** /decrypt | 
[**decrypt_pkcs1**](V2Api.md#decrypt_pkcs1) | **POST** /decrypt-pkcs1 | 
[**decrypt_with_classic_key**](V2Api.md#decrypt_with_classic_key) | **POST** /decrypt-with-classic-key | 
[**delete_auth_method**](V2Api.md#delete_auth_method) | **POST** /delete-auth-method | 
[**delete_auth_methods**](V2Api.md#delete_auth_methods) | **POST** /delete-auth-methods | 
[**delete_item**](V2Api.md#delete_item) | **POST** /delete-item | 
[**delete_items**](V2Api.md#delete_items) | **POST** /delete-items | 
[**delete_role**](V2Api.md#delete_role) | **POST** /delete-role | 
[**delete_role_association**](V2Api.md#delete_role_association) | **POST** /delete-assoc | 
[**delete_role_rule**](V2Api.md#delete_role_rule) | **POST** /delete-role-rule | 
[**delete_roles**](V2Api.md#delete_roles) | **POST** /delete-roles | 
[**delete_target**](V2Api.md#delete_target) | **POST** /delete-target | 
[**delete_target_association**](V2Api.md#delete_target_association) | **POST** /delete-assoc-target-item | 
[**delete_targets**](V2Api.md#delete_targets) | **POST** /delete-targets | 
[**describe_item**](V2Api.md#describe_item) | **POST** /describe-item | 
[**describe_permissions**](V2Api.md#describe_permissions) | **POST** /describe-permissions | 
[**encrypt**](V2Api.md#encrypt) | **POST** /encrypt | 
[**encrypt_pkcs1**](V2Api.md#encrypt_pkcs1) | **POST** /encrypt-pkcs1 | 
[**encrypt_with_classic_key**](V2Api.md#encrypt_with_classic_key) | **POST** /encrypt-with-classic-key | 
[**gateway_create_k8_s_auth_config**](V2Api.md#gateway_create_k8_s_auth_config) | **POST** /gateway-create-k8s-auth-config | 
[**gateway_create_producer_artifactory**](V2Api.md#gateway_create_producer_artifactory) | **POST** /gateway-create-producer-artifactory | 
[**gateway_create_producer_aws**](V2Api.md#gateway_create_producer_aws) | **POST** /gateway-create-producer-aws | 
[**gateway_create_producer_azure**](V2Api.md#gateway_create_producer_azure) | **POST** /gateway-create-producer-azure | 
[**gateway_create_producer_cassandra**](V2Api.md#gateway_create_producer_cassandra) | **POST** /gateway-create-producer-cassandra | 
[**gateway_create_producer_certificate_automation**](V2Api.md#gateway_create_producer_certificate_automation) | **POST** /gateway-create-producer-certificate-automation | 
[**gateway_create_producer_custom**](V2Api.md#gateway_create_producer_custom) | **POST** /gateway-create-producer-custom | 
[**gateway_create_producer_eks**](V2Api.md#gateway_create_producer_eks) | **POST** /gateway-create-producer-eks | 
[**gateway_create_producer_gcp**](V2Api.md#gateway_create_producer_gcp) | **POST** /gateway-create-producer-gcp | 
[**gateway_create_producer_gke**](V2Api.md#gateway_create_producer_gke) | **POST** /gateway-create-producer-gke | 
[**gateway_create_producer_ldap**](V2Api.md#gateway_create_producer_ldap) | **POST** /gateway-create-producer-ldap | 
[**gateway_create_producer_mongo**](V2Api.md#gateway_create_producer_mongo) | **POST** /gateway-create-producer-mongo | 
[**gateway_create_producer_mssql**](V2Api.md#gateway_create_producer_mssql) | **POST** /gateway-create-producer-mssql | 
[**gateway_create_producer_my_sql**](V2Api.md#gateway_create_producer_my_sql) | **POST** /gateway-create-producer-mysql | 
[**gateway_create_producer_native_k8_s**](V2Api.md#gateway_create_producer_native_k8_s) | **POST** /gateway-create-producer-k8s-native | 
[**gateway_create_producer_oracle_db**](V2Api.md#gateway_create_producer_oracle_db) | **POST** /gateway-create-producer-oracle | 
[**gateway_create_producer_postgre_sql**](V2Api.md#gateway_create_producer_postgre_sql) | **POST** /gateway-create-producer-postgresql | 
[**gateway_create_producer_rabbit_mq**](V2Api.md#gateway_create_producer_rabbit_mq) | **POST** /gateway-create-producer-rabbitmq | 
[**gateway_create_producer_rdp**](V2Api.md#gateway_create_producer_rdp) | **POST** /gateway-create-producer-rdp | 
[**gateway_create_producer_redshift**](V2Api.md#gateway_create_producer_redshift) | **POST** /gateway-create-producer-redshift | 
[**gateway_create_producer_snowflake**](V2Api.md#gateway_create_producer_snowflake) | **POST** /gateway-create-producer-snowflake | 
[**gateway_delete_allowed_management_access**](V2Api.md#gateway_delete_allowed_management_access) | **POST** /gateway-delete-allowed-management-access | 
[**gateway_delete_k8_s_auth_config**](V2Api.md#gateway_delete_k8_s_auth_config) | **POST** /gateway-delete-k8s-auth-config | 
[**gateway_delete_producer**](V2Api.md#gateway_delete_producer) | **POST** /gateway-delete-producer | 
[**gateway_get_config**](V2Api.md#gateway_get_config) | **POST** /gateway-get-config | 
[**gateway_get_k8_s_auth_config**](V2Api.md#gateway_get_k8_s_auth_config) | **POST** /gateway-get-k8s-auth-config | 
[**gateway_get_producer**](V2Api.md#gateway_get_producer) | **POST** /gateway-get-producer | 
[**gateway_get_tmp_users**](V2Api.md#gateway_get_tmp_users) | **POST** /gateway-get-producer-tmp-creds | 
[**gateway_list_allowed_management_access**](V2Api.md#gateway_list_allowed_management_access) | **POST** /gateway-list-allowed-management-access | 
[**gateway_list_migration**](V2Api.md#gateway_list_migration) | **POST** /gateway-list-migration | 
[**gateway_list_producers**](V2Api.md#gateway_list_producers) | **POST** /gateway-list-producers | 
[**gateway_revoke_tmp_users**](V2Api.md#gateway_revoke_tmp_users) | **POST** /gateway-revoke-producer-tmp-creds | 
[**gateway_start_producer**](V2Api.md#gateway_start_producer) | **POST** /gateway-start-producer | 
[**gateway_stop_producer**](V2Api.md#gateway_stop_producer) | **POST** /gateway-stop-producer | 
[**gateway_sync_migration**](V2Api.md#gateway_sync_migration) | **POST** /gateway-sync-migration | 
[**gateway_update_tmp_users**](V2Api.md#gateway_update_tmp_users) | **POST** /gateway-update-producer-tmp-creds | 
[**get_account_logo**](V2Api.md#get_account_logo) | **POST** /get-account-logo | 
[**get_auth_method**](V2Api.md#get_auth_method) | **POST** /get-auth-method | 
[**get_dynamic_secret_value**](V2Api.md#get_dynamic_secret_value) | **POST** /get-dynamic-secret-value | 
[**get_kube_exec_creds**](V2Api.md#get_kube_exec_creds) | **POST** /get-kube-exec-creds | 
[**get_pki_certificate**](V2Api.md#get_pki_certificate) | **POST** /get-pki-certificate | 
[**get_role**](V2Api.md#get_role) | **POST** /get-role | 
[**get_rotated_secret_value**](V2Api.md#get_rotated_secret_value) | **POST** /get-rotated-secret-value | 
[**get_rsa_public**](V2Api.md#get_rsa_public) | **POST** /get-rsa-public | 
[**get_secret_value**](V2Api.md#get_secret_value) | **POST** /get-secret-value | 
[**get_ssh_certificate**](V2Api.md#get_ssh_certificate) | **POST** /get-ssh-certificate | 
[**get_target**](V2Api.md#get_target) | **POST** /get-target | 
[**get_target_details**](V2Api.md#get_target_details) | **POST** /get-target-details | 
[**kmip_client_delete_rule**](V2Api.md#kmip_client_delete_rule) | **POST** /kmip-client-delete-rule | 
[**kmip_client_set_rule**](V2Api.md#kmip_client_set_rule) | **POST** /kmip-client-set-rule | 
[**kmip_create_client**](V2Api.md#kmip_create_client) | **POST** /kmip-create-client | 
[**kmip_delete_client**](V2Api.md#kmip_delete_client) | **POST** /kmip-delete-client | 
[**kmip_describe_client**](V2Api.md#kmip_describe_client) | **POST** /kmip-get-client | 
[**kmip_describe_server**](V2Api.md#kmip_describe_server) | **POST** /kmip-get-environment | 
[**kmip_list_clients**](V2Api.md#kmip_list_clients) | **POST** /kmip-list-clients | 
[**kmip_renew_client_certificate**](V2Api.md#kmip_renew_client_certificate) | **POST** /kmip-renew-client | 
[**kmip_renew_server_certificate**](V2Api.md#kmip_renew_server_certificate) | **POST** /kmip-renew-environment | 
[**kmip_server_setup**](V2Api.md#kmip_server_setup) | **POST** /kmip-create-environment | 
[**kmip_set_server_state**](V2Api.md#kmip_set_server_state) | **POST** /kmip-set-environment-state | 
[**list_auth_methods**](V2Api.md#list_auth_methods) | **POST** /list-auth-methods | 
[**list_items**](V2Api.md#list_items) | **POST** /list-items | 
[**list_roles**](V2Api.md#list_roles) | **POST** /list-roles | 
[**list_targets**](V2Api.md#list_targets) | **POST** /list-targets | 
[**move_objects**](V2Api.md#move_objects) | **POST** /move-objects | 
[**raw_creds**](V2Api.md#raw_creds) | **POST** /raw-creds | 
[**refresh_key**](V2Api.md#refresh_key) | **POST** /refresh-key | 
[**reverse_rbac**](V2Api.md#reverse_rbac) | **POST** /reverse-rbac | 
[**rollback_secret**](V2Api.md#rollback_secret) | **POST** /rollback-secret | 
[**rotate_key**](V2Api.md#rotate_key) | **POST** /rotate-key | 
[**set_item_state**](V2Api.md#set_item_state) | **POST** /set-item-state | 
[**set_role_rule**](V2Api.md#set_role_rule) | **POST** /set-role-rule | 
[**sign_jwt_with_classic_key**](V2Api.md#sign_jwt_with_classic_key) | **POST** /sign-jwt-with-classic-key | 
[**sign_pkcs1**](V2Api.md#sign_pkcs1) | **POST** /sign-pkcs1 | 
[**sign_pki_cert_with_classic_key**](V2Api.md#sign_pki_cert_with_classic_key) | **POST** /sign-pki-cert-with-classic-key | 
[**static_creds_auth**](V2Api.md#static_creds_auth) | **POST** /static-creds-auth | 
[**uid_create_child_token**](V2Api.md#uid_create_child_token) | **POST** /uid-create-child-token | 
[**uid_generate_token**](V2Api.md#uid_generate_token) | **POST** /uid-generate-token | 
[**uid_list_children**](V2Api.md#uid_list_children) | **POST** /uid-list-children | 
[**uid_revoke_token**](V2Api.md#uid_revoke_token) | **POST** /uid-revoke-token | 
[**uid_rotate_token**](V2Api.md#uid_rotate_token) | **POST** /uid-rotate-token | 
[**update_assoc**](V2Api.md#update_assoc) | **POST** /update-assoc | 
[**update_aws_target**](V2Api.md#update_aws_target) | **PUT** /update-aws-target | 
[**update_aws_target_details**](V2Api.md#update_aws_target_details) | **POST** /update-aws-target-details | 
[**update_azure_target**](V2Api.md#update_azure_target) | **PUT** /update-azure-target | 
[**update_db_target**](V2Api.md#update_db_target) | **POST** /update-db-target | 
[**update_db_target_details**](V2Api.md#update_db_target_details) | **POST** /update-db-target-details | 
[**update_eks_target**](V2Api.md#update_eks_target) | **PUT** /update-eks-target | 
[**update_gcp_target**](V2Api.md#update_gcp_target) | **PUT** /update-gcp-target | 
[**update_gke_target**](V2Api.md#update_gke_target) | **PUT** /update-gke-target | 
[**update_item**](V2Api.md#update_item) | **POST** /update-item | 
[**update_native_k8_s_target**](V2Api.md#update_native_k8_s_target) | **PUT** /update-k8s-target | 
[**update_rabbit_mq_target**](V2Api.md#update_rabbit_mq_target) | **PUT** /update-rabbitmq-target | 
[**update_rabbit_mq_target_details**](V2Api.md#update_rabbit_mq_target_details) | **POST** /update-rabbitmq-target-details | 
[**update_rdp_target_details**](V2Api.md#update_rdp_target_details) | **POST** /update-rdp-target-details | 
[**update_role**](V2Api.md#update_role) | **POST** /update-role | 
[**update_rotated_secret**](V2Api.md#update_rotated_secret) | **POST** /update-rotated-secret | 
[**update_rotation_settings**](V2Api.md#update_rotation_settings) | **POST** /update-rotation-settingsrotate-key | 
[**update_secret_val**](V2Api.md#update_secret_val) | **POST** /update-secret-val | 
[**update_ssh_target**](V2Api.md#update_ssh_target) | **POST** /update-ssh-target | 
[**update_ssh_target_details**](V2Api.md#update_ssh_target_details) | **POST** /update-ssh-target-details | 
[**update_target**](V2Api.md#update_target) | **POST** /update-target | 
[**update_target_details**](V2Api.md#update_target_details) | **POST** /update-target-details | 
[**update_web_target**](V2Api.md#update_web_target) | **POST** /update-web-target | 
[**update_web_target_details**](V2Api.md#update_web_target_details) | **POST** /update-web-target-details | 
[**upload_rsa**](V2Api.md#upload_rsa) | **POST** /upload-rsa | 
[**verify_jwt_with_classic_key**](V2Api.md#verify_jwt_with_classic_key) | **POST** /verify-jwt-with-classic-key | 
[**verify_pkcs1**](V2Api.md#verify_pkcs1) | **POST** /verify-pkcs1 | 
[**verify_pki_cert_with_classic_key**](V2Api.md#verify_pki_cert_with_classic_key) | **POST** /verify-pki-cert-with-classic-key | 


# **assoc_role_auth_method**
> CreateRoleAuthMethodAssocOutput assoc_role_auth_method(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.AssocRoleAuthMethod() # AssocRoleAuthMethod | 

    try:
        api_response = api_instance.assoc_role_auth_method(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->assoc_role_auth_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssocRoleAuthMethod**](AssocRoleAuthMethod.md)|  | 

### Return type

[**CreateRoleAuthMethodAssocOutput**](CreateRoleAuthMethodAssocOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | assocRoleAuthMethodResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assoc_target_item**
> CreateTargetItemAssocOutput assoc_target_item(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.AssocTargetItem() # AssocTargetItem | 

    try:
        api_response = api_instance.assoc_target_item(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->assoc_target_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssocTargetItem**](AssocTargetItem.md)|  | 

### Return type

[**CreateTargetItemAssocOutput**](CreateTargetItemAssocOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | assocTargetItemResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth**
> AuthOutput auth(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.Auth() # Auth | 

    try:
        api_response = api_instance.auth(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auth**](Auth.md)|  | 

### Return type

[**AuthOutput**](AuthOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | authResponse wraps response body. |  -  |
**401** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure**
> ConfigureOutput configure(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.Configure() # Configure | 

    try:
        api_response = api_instance.configure(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->configure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Configure**](Configure.md)|  | 

### Return type

[**ConfigureOutput**](ConfigureOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configureResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect**
> object connect(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.Connect() # Connect | 

    try:
        api_response = api_instance.connect(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connect**](Connect.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | connectResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artifactory_target**
> CreateArtifactoryTargetOutput create_artifactory_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateArtifactoryTarget() # CreateArtifactoryTarget | 

    try:
        api_response = api_instance.create_artifactory_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_artifactory_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateArtifactoryTarget**](CreateArtifactoryTarget.md)|  | 

### Return type

[**CreateArtifactoryTargetOutput**](CreateArtifactoryTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createArtifactoryTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method**
> CreateAuthMethodOutput create_auth_method(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethod() # CreateAuthMethod | 

    try:
        api_response = api_instance.create_auth_method(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethod**](CreateAuthMethod.md)|  | 

### Return type

[**CreateAuthMethodOutput**](CreateAuthMethodOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_awsiam**
> CreateAuthMethodAWSIAMOutput create_auth_method_awsiam(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodAWSIAM() # CreateAuthMethodAWSIAM | 

    try:
        api_response = api_instance.create_auth_method_awsiam(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_awsiam: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodAWSIAM**](CreateAuthMethodAWSIAM.md)|  | 

### Return type

[**CreateAuthMethodAWSIAMOutput**](CreateAuthMethodAWSIAMOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodAWSIAMResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_azure_ad**
> CreateAuthMethodAzureADOutput create_auth_method_azure_ad(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodAzureAD() # CreateAuthMethodAzureAD | 

    try:
        api_response = api_instance.create_auth_method_azure_ad(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_azure_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodAzureAD**](CreateAuthMethodAzureAD.md)|  | 

### Return type

[**CreateAuthMethodAzureADOutput**](CreateAuthMethodAzureADOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodAzureADResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_gcp**
> CreateAuthMethodGCPOutput create_auth_method_gcp(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodGCP() # CreateAuthMethodGCP | 

    try:
        api_response = api_instance.create_auth_method_gcp(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodGCP**](CreateAuthMethodGCP.md)|  | 

### Return type

[**CreateAuthMethodGCPOutput**](CreateAuthMethodGCPOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodGCPResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_huawei**
> CreateAuthMethodHuaweiOutput create_auth_method_huawei(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodHuawei() # CreateAuthMethodHuawei | 

    try:
        api_response = api_instance.create_auth_method_huawei(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_huawei: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodHuawei**](CreateAuthMethodHuawei.md)|  | 

### Return type

[**CreateAuthMethodHuaweiOutput**](CreateAuthMethodHuaweiOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodHuaweiResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_o_auth2**
> CreateAuthMethodOAuth2Output create_auth_method_o_auth2(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodOAuth2() # CreateAuthMethodOAuth2 | 

    try:
        api_response = api_instance.create_auth_method_o_auth2(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_o_auth2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodOAuth2**](CreateAuthMethodOAuth2.md)|  | 

### Return type

[**CreateAuthMethodOAuth2Output**](CreateAuthMethodOAuth2Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodOAuth2Response wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_oidc**
> CreateAuthMethodOIDCOutput create_auth_method_oidc(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodOIDC() # CreateAuthMethodOIDC | 

    try:
        api_response = api_instance.create_auth_method_oidc(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_oidc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodOIDC**](CreateAuthMethodOIDC.md)|  | 

### Return type

[**CreateAuthMethodOIDCOutput**](CreateAuthMethodOIDCOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodOIDCResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_saml**
> CreateAuthMethodSAMLOutput create_auth_method_saml(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodSAML() # CreateAuthMethodSAML | 

    try:
        api_response = api_instance.create_auth_method_saml(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_saml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodSAML**](CreateAuthMethodSAML.md)|  | 

### Return type

[**CreateAuthMethodSAMLOutput**](CreateAuthMethodSAMLOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodSAMLResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_method_universal_identity**
> CreateAuthMethodUniversalIdentityOutput create_auth_method_universal_identity(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAuthMethodUniversalIdentity() # CreateAuthMethodUniversalIdentity | 

    try:
        api_response = api_instance.create_auth_method_universal_identity(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_auth_method_universal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAuthMethodUniversalIdentity**](CreateAuthMethodUniversalIdentity.md)|  | 

### Return type

[**CreateAuthMethodUniversalIdentityOutput**](CreateAuthMethodUniversalIdentityOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAuthMethodUniversalIdentityResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aws_target**
> CreateAWSTargetOutput create_aws_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAWSTarget() # CreateAWSTarget | 

    try:
        api_response = api_instance.create_aws_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_aws_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAWSTarget**](CreateAWSTarget.md)|  | 

### Return type

[**CreateAWSTargetOutput**](CreateAWSTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAWSTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_target**
> CreateAzureTargetOutput create_azure_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateAzureTarget() # CreateAzureTarget | 

    try:
        api_response = api_instance.create_azure_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_azure_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureTarget**](CreateAzureTarget.md)|  | 

### Return type

[**CreateAzureTargetOutput**](CreateAzureTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createAzureTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classic_key**
> CreateClassicKeyOutput create_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateClassicKey() # CreateClassicKey | 

    try:
        api_response = api_instance.create_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClassicKey**](CreateClassicKey.md)|  | 

### Return type

[**CreateClassicKeyOutput**](CreateClassicKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CreateClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_db_target**
> CreateDBTargetOutput create_db_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateDBTarget() # CreateDBTarget | 

    try:
        api_response = api_instance.create_db_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_db_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDBTarget**](CreateDBTarget.md)|  | 

### Return type

[**CreateDBTargetOutput**](CreateDBTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createDBTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfc_key**
> CreateDFCKeyOutput create_dfc_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateDFCKey() # CreateDFCKey | 

    try:
        api_response = api_instance.create_dfc_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_dfc_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDFCKey**](CreateDFCKey.md)|  | 

### Return type

[**CreateDFCKeyOutput**](CreateDFCKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createDFCKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dynamic_secret**
> object create_dynamic_secret(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateDynamicSecret() # CreateDynamicSecret | 

    try:
        api_response = api_instance.create_dynamic_secret(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_dynamic_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDynamicSecret**](CreateDynamicSecret.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createDynamicSecretResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_eks_target**
> CreateEKSTargetOutput create_eks_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateEKSTarget() # CreateEKSTarget | 

    try:
        api_response = api_instance.create_eks_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_eks_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEKSTarget**](CreateEKSTarget.md)|  | 

### Return type

[**CreateEKSTargetOutput**](CreateEKSTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createEKSTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_target**
> CreateGcpTargetOutput create_gcp_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateGcpTarget() # CreateGcpTarget | 

    try:
        api_response = api_instance.create_gcp_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_gcp_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGcpTarget**](CreateGcpTarget.md)|  | 

### Return type

[**CreateGcpTargetOutput**](CreateGcpTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createGcpTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gke_target**
> CreateGKETargetOutput create_gke_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateGKETarget() # CreateGKETarget | 

    try:
        api_response = api_instance.create_gke_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_gke_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGKETarget**](CreateGKETarget.md)|  | 

### Return type

[**CreateGKETargetOutput**](CreateGKETargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createGKETargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key**
> CreateKeyOutput create_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateKey() # CreateKey | 

    try:
        api_response = api_instance.create_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKey**](CreateKey.md)|  | 

### Return type

[**CreateKeyOutput**](CreateKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_native_k8_s_target**
> CreateNativeK8STarget create_native_k8_s_target()



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    
    try:
        api_response = api_instance.create_native_k8_s_target()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_native_k8_s_target: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateNativeK8STarget**](CreateNativeK8STarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createNativeK8STarget |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pki_cert_issuer**
> CreatePKICertIssuerOutput create_pki_cert_issuer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreatePKICertIssuer() # CreatePKICertIssuer | 

    try:
        api_response = api_instance.create_pki_cert_issuer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_pki_cert_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePKICertIssuer**](CreatePKICertIssuer.md)|  | 

### Return type

[**CreatePKICertIssuerOutput**](CreatePKICertIssuerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPKICertIssuerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rabbit_mq_target**
> CreateRabbitMQTargetOutput create_rabbit_mq_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateRabbitMQTarget() # CreateRabbitMQTarget | 

    try:
        api_response = api_instance.create_rabbit_mq_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_rabbit_mq_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRabbitMQTarget**](CreateRabbitMQTarget.md)|  | 

### Return type

[**CreateRabbitMQTargetOutput**](CreateRabbitMQTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createRabbitMQTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> object create_role(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateRole() # CreateRole | 

    try:
        api_response = api_instance.create_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRole**](CreateRole.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createRoleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rotated_secret**
> CreateRotatedSecretOutput create_rotated_secret(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateRotatedSecret() # CreateRotatedSecret | 

    try:
        api_response = api_instance.create_rotated_secret(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_rotated_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRotatedSecret**](CreateRotatedSecret.md)|  | 

### Return type

[**CreateRotatedSecretOutput**](CreateRotatedSecretOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createRotatedSecretResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret**
> CreateSecretOutput create_secret(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateSecret() # CreateSecret | 

    try:
        api_response = api_instance.create_secret(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSecret**](CreateSecret.md)|  | 

### Return type

[**CreateSecretOutput**](CreateSecretOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createSecretResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_cert_issuer**
> CreateSSHCertIssuerOutput create_ssh_cert_issuer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateSSHCertIssuer() # CreateSSHCertIssuer | 

    try:
        api_response = api_instance.create_ssh_cert_issuer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_ssh_cert_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSSHCertIssuer**](CreateSSHCertIssuer.md)|  | 

### Return type

[**CreateSSHCertIssuerOutput**](CreateSSHCertIssuerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createSSHCertIssuerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_target**
> CreateSSHTargetOutput create_ssh_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateSSHTarget() # CreateSSHTarget | 

    try:
        api_response = api_instance.create_ssh_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_ssh_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSSHTarget**](CreateSSHTarget.md)|  | 

### Return type

[**CreateSSHTargetOutput**](CreateSSHTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createSSHTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_target**
> CreateWebTargetOutput create_web_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateWebTarget() # CreateWebTarget | 

    try:
        api_response = api_instance.create_web_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->create_web_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebTarget**](CreateWebTarget.md)|  | 

### Return type

[**CreateWebTargetOutput**](CreateWebTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createWebTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createldap_target**
> CreateLdapTargetOutput createldap_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.CreateLdapTarget() # CreateLdapTarget | 

    try:
        api_response = api_instance.createldap_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->createldap_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLdapTarget**](CreateLdapTarget.md)|  | 

### Return type

[**CreateLdapTargetOutput**](CreateLdapTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createldapTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrypt**
> DecryptOutput decrypt(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.Decrypt() # Decrypt | 

    try:
        api_response = api_instance.decrypt(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Decrypt**](Decrypt.md)|  | 

### Return type

[**DecryptOutput**](DecryptOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | decryptResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrypt_pkcs1**
> DecryptPKCS1Output decrypt_pkcs1(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DecryptPKCS1() # DecryptPKCS1 | 

    try:
        api_response = api_instance.decrypt_pkcs1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->decrypt_pkcs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DecryptPKCS1**](DecryptPKCS1.md)|  | 

### Return type

[**DecryptPKCS1Output**](DecryptPKCS1Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | decryptPKCS1Response wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrypt_with_classic_key**
> DecryptWithClassicKeyOutput decrypt_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DecryptWithClassicKey() # DecryptWithClassicKey | 

    try:
        api_response = api_instance.decrypt_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->decrypt_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DecryptWithClassicKey**](DecryptWithClassicKey.md)|  | 

### Return type

[**DecryptWithClassicKeyOutput**](DecryptWithClassicKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | decryptWithClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_method**
> DeleteAuthMethodOutput delete_auth_method(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteAuthMethod() # DeleteAuthMethod | 

    try:
        api_response = api_instance.delete_auth_method(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_auth_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAuthMethod**](DeleteAuthMethod.md)|  | 

### Return type

[**DeleteAuthMethodOutput**](DeleteAuthMethodOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteAuthMethodResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_methods**
> DeleteAuthMethodsOutput delete_auth_methods(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteAuthMethods() # DeleteAuthMethods | 

    try:
        api_response = api_instance.delete_auth_methods(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_auth_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAuthMethods**](DeleteAuthMethods.md)|  | 

### Return type

[**DeleteAuthMethodsOutput**](DeleteAuthMethodsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteAuthMethodsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> DeleteItemOutput delete_item(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteItem() # DeleteItem | 

    try:
        api_response = api_instance.delete_item(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteItem**](DeleteItem.md)|  | 

### Return type

[**DeleteItemOutput**](DeleteItemOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteItemResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items**
> DeleteItemsOutput delete_items(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteItems() # DeleteItems | 

    try:
        api_response = api_instance.delete_items(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteItems**](DeleteItems.md)|  | 

### Return type

[**DeleteItemsOutput**](DeleteItemsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteItemsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> object delete_role(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteRole() # DeleteRole | 

    try:
        api_response = api_instance.delete_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRole**](DeleteRole.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteRoleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_association**
> object delete_role_association(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteRoleAssociation() # DeleteRoleAssociation | 

    try:
        api_response = api_instance.delete_role_association(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_role_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRoleAssociation**](DeleteRoleAssociation.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteRoleAssociationResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_rule**
> DeleteRoleRuleOutput delete_role_rule(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteRoleRule() # DeleteRoleRule | 

    try:
        api_response = api_instance.delete_role_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_role_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRoleRule**](DeleteRoleRule.md)|  | 

### Return type

[**DeleteRoleRuleOutput**](DeleteRoleRuleOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteRoleRuleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roles**
> object delete_roles(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteRoles() # DeleteRoles | 

    try:
        api_response = api_instance.delete_roles(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRoles**](DeleteRoles.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteRolesResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target**
> object delete_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteTarget() # DeleteTarget | 

    try:
        api_response = api_instance.delete_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTarget**](DeleteTarget.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target_association**
> object delete_target_association(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteTargetAssociation() # DeleteTargetAssociation | 

    try:
        api_response = api_instance.delete_target_association(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_target_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTargetAssociation**](DeleteTargetAssociation.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteTargetAssociationResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_targets**
> object delete_targets(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DeleteTargets() # DeleteTargets | 

    try:
        api_response = api_instance.delete_targets(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->delete_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTargets**](DeleteTargets.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteTargetsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_item**
> Item describe_item(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DescribeItem() # DescribeItem | 

    try:
        api_response = api_instance.describe_item(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->describe_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DescribeItem**](DescribeItem.md)|  | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | describeItemResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_permissions**
> DescribePermissionsOutput describe_permissions(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.DescribePermissions() # DescribePermissions | 

    try:
        api_response = api_instance.describe_permissions(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->describe_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DescribePermissions**](DescribePermissions.md)|  | 

### Return type

[**DescribePermissionsOutput**](DescribePermissionsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DescribePermissionsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encrypt**
> EncryptOutput encrypt(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.Encrypt() # Encrypt | 

    try:
        api_response = api_instance.encrypt(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Encrypt**](Encrypt.md)|  | 

### Return type

[**EncryptOutput**](EncryptOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | encryptResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encrypt_pkcs1**
> EncryptPKCS1Output encrypt_pkcs1(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.EncryptPKCS1() # EncryptPKCS1 | 

    try:
        api_response = api_instance.encrypt_pkcs1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->encrypt_pkcs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EncryptPKCS1**](EncryptPKCS1.md)|  | 

### Return type

[**EncryptPKCS1Output**](EncryptPKCS1Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | encryptPKCS1Response wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encrypt_with_classic_key**
> EncryptOutput encrypt_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.EncryptWithClassicKey() # EncryptWithClassicKey | 

    try:
        api_response = api_instance.encrypt_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->encrypt_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EncryptWithClassicKey**](EncryptWithClassicKey.md)|  | 

### Return type

[**EncryptOutput**](EncryptOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | encryptResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_k8_s_auth_config**
> GatewayCreateK8SAuthConfigOutput gateway_create_k8_s_auth_config(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateK8SAuthConfig() # GatewayCreateK8SAuthConfig | 

    try:
        api_response = api_instance.gateway_create_k8_s_auth_config(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_k8_s_auth_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateK8SAuthConfig**](GatewayCreateK8SAuthConfig.md)|  | 

### Return type

[**GatewayCreateK8SAuthConfigOutput**](GatewayCreateK8SAuthConfigOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateK8SAuthConfigResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_artifactory**
> GatewayCreateProducerArtifactoryOutput gateway_create_producer_artifactory(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerArtifactory() # GatewayCreateProducerArtifactory | 

    try:
        api_response = api_instance.gateway_create_producer_artifactory(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerArtifactory**](GatewayCreateProducerArtifactory.md)|  | 

### Return type

[**GatewayCreateProducerArtifactoryOutput**](GatewayCreateProducerArtifactoryOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerArtifactoryResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_aws**
> GatewayCreateProducerAwsOutput gateway_create_producer_aws(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerAws() # GatewayCreateProducerAws | 

    try:
        api_response = api_instance.gateway_create_producer_aws(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_aws: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerAws**](GatewayCreateProducerAws.md)|  | 

### Return type

[**GatewayCreateProducerAwsOutput**](GatewayCreateProducerAwsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerAwsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_azure**
> GatewayCreateProducerAzureOutput gateway_create_producer_azure(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerAzure() # GatewayCreateProducerAzure | 

    try:
        api_response = api_instance.gateway_create_producer_azure(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_azure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerAzure**](GatewayCreateProducerAzure.md)|  | 

### Return type

[**GatewayCreateProducerAzureOutput**](GatewayCreateProducerAzureOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerAzureResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_cassandra**
> GatewayCreateProducerCassandraOutput gateway_create_producer_cassandra(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerCassandra() # GatewayCreateProducerCassandra | 

    try:
        api_response = api_instance.gateway_create_producer_cassandra(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_cassandra: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerCassandra**](GatewayCreateProducerCassandra.md)|  | 

### Return type

[**GatewayCreateProducerCassandraOutput**](GatewayCreateProducerCassandraOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerCassandraResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_certificate_automation**
> GatewayCreateProducerCertificateAutomationOutput gateway_create_producer_certificate_automation(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerCertificateAutomation() # GatewayCreateProducerCertificateAutomation | 

    try:
        api_response = api_instance.gateway_create_producer_certificate_automation(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_certificate_automation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerCertificateAutomation**](GatewayCreateProducerCertificateAutomation.md)|  | 

### Return type

[**GatewayCreateProducerCertificateAutomationOutput**](GatewayCreateProducerCertificateAutomationOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerCertificateAutomationResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_custom**
> GatewayCreateProducerCustomOutput gateway_create_producer_custom(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerCustom() # GatewayCreateProducerCustom |  (optional)

    try:
        api_response = api_instance.gateway_create_producer_custom(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_custom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerCustom**](GatewayCreateProducerCustom.md)|  | [optional] 

### Return type

[**GatewayCreateProducerCustomOutput**](GatewayCreateProducerCustomOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayCreateProducerCustomResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_eks**
> GatewayCreateProducerEksOutput gateway_create_producer_eks(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerEks() # GatewayCreateProducerEks | 

    try:
        api_response = api_instance.gateway_create_producer_eks(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_eks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerEks**](GatewayCreateProducerEks.md)|  | 

### Return type

[**GatewayCreateProducerEksOutput**](GatewayCreateProducerEksOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerEksResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_gcp**
> GatewayCreateProducerGcpOutput gateway_create_producer_gcp(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerGcp() # GatewayCreateProducerGcp | 

    try:
        api_response = api_instance.gateway_create_producer_gcp(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerGcp**](GatewayCreateProducerGcp.md)|  | 

### Return type

[**GatewayCreateProducerGcpOutput**](GatewayCreateProducerGcpOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerGcpResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_gke**
> GatewayCreateProducerGkeOutput gateway_create_producer_gke(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerGke() # GatewayCreateProducerGke | 

    try:
        api_response = api_instance.gateway_create_producer_gke(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_gke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerGke**](GatewayCreateProducerGke.md)|  | 

### Return type

[**GatewayCreateProducerGkeOutput**](GatewayCreateProducerGkeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerGkeResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_ldap**
> GatewayCreateProducerLdapOutput gateway_create_producer_ldap(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerLdap() # GatewayCreateProducerLdap | 

    try:
        api_response = api_instance.gateway_create_producer_ldap(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerLdap**](GatewayCreateProducerLdap.md)|  | 

### Return type

[**GatewayCreateProducerLdapOutput**](GatewayCreateProducerLdapOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerLdapResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_mongo**
> GatewayCreateProducerMongoOutput gateway_create_producer_mongo(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerMongo() # GatewayCreateProducerMongo | 

    try:
        api_response = api_instance.gateway_create_producer_mongo(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_mongo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerMongo**](GatewayCreateProducerMongo.md)|  | 

### Return type

[**GatewayCreateProducerMongoOutput**](GatewayCreateProducerMongoOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerMongoResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_mssql**
> GatewayCreateProducerMSSQLOutput gateway_create_producer_mssql(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerMSSQL() # GatewayCreateProducerMSSQL | 

    try:
        api_response = api_instance.gateway_create_producer_mssql(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_mssql: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerMSSQL**](GatewayCreateProducerMSSQL.md)|  | 

### Return type

[**GatewayCreateProducerMSSQLOutput**](GatewayCreateProducerMSSQLOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerMSSQLResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_my_sql**
> GatewayCreateProducerMySQLOutput gateway_create_producer_my_sql(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerMySQL() # GatewayCreateProducerMySQL | 

    try:
        api_response = api_instance.gateway_create_producer_my_sql(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_my_sql: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerMySQL**](GatewayCreateProducerMySQL.md)|  | 

### Return type

[**GatewayCreateProducerMySQLOutput**](GatewayCreateProducerMySQLOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerMySQLResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_native_k8_s**
> GatewayCreateProducerNativeK8SOutput gateway_create_producer_native_k8_s(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerNativeK8S() # GatewayCreateProducerNativeK8S | 

    try:
        api_response = api_instance.gateway_create_producer_native_k8_s(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_native_k8_s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerNativeK8S**](GatewayCreateProducerNativeK8S.md)|  | 

### Return type

[**GatewayCreateProducerNativeK8SOutput**](GatewayCreateProducerNativeK8SOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerNativeK8SResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_oracle_db**
> GatewayCreateProducerOracleDbOutput gateway_create_producer_oracle_db(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerOracleDb() # GatewayCreateProducerOracleDb | 

    try:
        api_response = api_instance.gateway_create_producer_oracle_db(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_oracle_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerOracleDb**](GatewayCreateProducerOracleDb.md)|  | 

### Return type

[**GatewayCreateProducerOracleDbOutput**](GatewayCreateProducerOracleDbOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerOracleDbResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_postgre_sql**
> GatewayCreateProducerPostgreSQLOutput gateway_create_producer_postgre_sql(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerPostgreSQL() # GatewayCreateProducerPostgreSQL | 

    try:
        api_response = api_instance.gateway_create_producer_postgre_sql(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_postgre_sql: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerPostgreSQL**](GatewayCreateProducerPostgreSQL.md)|  | 

### Return type

[**GatewayCreateProducerPostgreSQLOutput**](GatewayCreateProducerPostgreSQLOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerPostgreSQLResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_rabbit_mq**
> GatewayCreateProducerRabbitMQOutput gateway_create_producer_rabbit_mq(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerRabbitMQ() # GatewayCreateProducerRabbitMQ | 

    try:
        api_response = api_instance.gateway_create_producer_rabbit_mq(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_rabbit_mq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerRabbitMQ**](GatewayCreateProducerRabbitMQ.md)|  | 

### Return type

[**GatewayCreateProducerRabbitMQOutput**](GatewayCreateProducerRabbitMQOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerRabbitMQResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_rdp**
> GatewayCreateProducerRdpOutput gateway_create_producer_rdp(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerRdp() # GatewayCreateProducerRdp | 

    try:
        api_response = api_instance.gateway_create_producer_rdp(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_rdp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerRdp**](GatewayCreateProducerRdp.md)|  | 

### Return type

[**GatewayCreateProducerRdpOutput**](GatewayCreateProducerRdpOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerRdpResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_redshift**
> GatewayCreateProducerRedshiftOutput gateway_create_producer_redshift(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerRedshift() # GatewayCreateProducerRedshift | 

    try:
        api_response = api_instance.gateway_create_producer_redshift(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_redshift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerRedshift**](GatewayCreateProducerRedshift.md)|  | 

### Return type

[**GatewayCreateProducerRedshiftOutput**](GatewayCreateProducerRedshiftOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerRedshiftResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create_producer_snowflake**
> GatewayCreateProducerSnowflakeOutput gateway_create_producer_snowflake(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayCreateProducerSnowflake() # GatewayCreateProducerSnowflake | 

    try:
        api_response = api_instance.gateway_create_producer_snowflake(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_create_producer_snowflake: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayCreateProducerSnowflake**](GatewayCreateProducerSnowflake.md)|  | 

### Return type

[**GatewayCreateProducerSnowflakeOutput**](GatewayCreateProducerSnowflakeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayCreateProducerSnowflakeResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_delete_allowed_management_access**
> object gateway_delete_allowed_management_access(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayDeleteAllowedManagementAccess() # GatewayDeleteAllowedManagementAccess | 

    try:
        api_response = api_instance.gateway_delete_allowed_management_access(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_delete_allowed_management_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayDeleteAllowedManagementAccess**](GatewayDeleteAllowedManagementAccess.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayDeleteSubAdminsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_delete_k8_s_auth_config**
> GatewayDeleteK8SAuthConfigOutput gateway_delete_k8_s_auth_config(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayDeleteK8SAuthConfig() # GatewayDeleteK8SAuthConfig | 

    try:
        api_response = api_instance.gateway_delete_k8_s_auth_config(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_delete_k8_s_auth_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayDeleteK8SAuthConfig**](GatewayDeleteK8SAuthConfig.md)|  | 

### Return type

[**GatewayDeleteK8SAuthConfigOutput**](GatewayDeleteK8SAuthConfigOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayDeleteK8SAuthConfigResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_delete_producer**
> GatewayDeleteProducerOutput gateway_delete_producer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayDeleteProducer() # GatewayDeleteProducer | 

    try:
        api_response = api_instance.gateway_delete_producer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_delete_producer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayDeleteProducer**](GatewayDeleteProducer.md)|  | 

### Return type

[**GatewayDeleteProducerOutput**](GatewayDeleteProducerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayDeleteProducerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_get_config**
> AkeylessGatewayConfig gateway_get_config(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayGetConfig() # GatewayGetConfig | 

    try:
        api_response = api_instance.gateway_get_config(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayGetConfig**](GatewayGetConfig.md)|  | 

### Return type

[**AkeylessGatewayConfig**](AkeylessGatewayConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayGetConfigResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_get_k8_s_auth_config**
> GatewayGetK8SAuthConfigOutput gateway_get_k8_s_auth_config(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayGetK8SAuthConfig() # GatewayGetK8SAuthConfig | 

    try:
        api_response = api_instance.gateway_get_k8_s_auth_config(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_get_k8_s_auth_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayGetK8SAuthConfig**](GatewayGetK8SAuthConfig.md)|  | 

### Return type

[**GatewayGetK8SAuthConfigOutput**](GatewayGetK8SAuthConfigOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | gatewayGetK8SAuthConfigResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_get_producer**
> DSProducerDetails gateway_get_producer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayGetProducer() # GatewayGetProducer | 

    try:
        api_response = api_instance.gateway_get_producer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_get_producer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayGetProducer**](GatewayGetProducer.md)|  | 

### Return type

[**DSProducerDetails**](DSProducerDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayGetProducerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_get_tmp_users**
> list[TmpUserData] gateway_get_tmp_users(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayGetTmpUsers() # GatewayGetTmpUsers | 

    try:
        api_response = api_instance.gateway_get_tmp_users(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_get_tmp_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayGetTmpUsers**](GatewayGetTmpUsers.md)|  | 

### Return type

[**list[TmpUserData]**](TmpUserData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayGetTmpUsersResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_list_allowed_management_access**
> GetSubAdminsListReplyObj gateway_list_allowed_management_access(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayListAllowedManagementAccess() # GatewayListAllowedManagementAccess | 

    try:
        api_response = api_instance.gateway_list_allowed_management_access(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_list_allowed_management_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayListAllowedManagementAccess**](GatewayListAllowedManagementAccess.md)|  | 

### Return type

[**GetSubAdminsListReplyObj**](GetSubAdminsListReplyObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayListSubAdminsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_list_migration**
> GatewayMigrationListOutput gateway_list_migration(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayListMigration() # GatewayListMigration | 

    try:
        api_response = api_instance.gateway_list_migration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_list_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayListMigration**](GatewayListMigration.md)|  | 

### Return type

[**GatewayMigrationListOutput**](GatewayMigrationListOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayMigrationListResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_list_producers**
> GetProducersListReplyObj gateway_list_producers(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayListProducers() # GatewayListProducers | 

    try:
        api_response = api_instance.gateway_list_producers(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_list_producers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayListProducers**](GatewayListProducers.md)|  | 

### Return type

[**GetProducersListReplyObj**](GetProducersListReplyObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayListProducersResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_revoke_tmp_users**
> gateway_revoke_tmp_users(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayRevokeTmpUsers() # GatewayRevokeTmpUsers | 

    try:
        api_instance.gateway_revoke_tmp_users(body)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_revoke_tmp_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayRevokeTmpUsers**](GatewayRevokeTmpUsers.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayRevokeTmpUsersResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_start_producer**
> GatewayStartProducerOutput gateway_start_producer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayStartProducer() # GatewayStartProducer | 

    try:
        api_response = api_instance.gateway_start_producer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_start_producer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayStartProducer**](GatewayStartProducer.md)|  | 

### Return type

[**GatewayStartProducerOutput**](GatewayStartProducerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayStartProducerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_stop_producer**
> GatewayStopProducerOutput gateway_stop_producer(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayStopProducer() # GatewayStopProducer | 

    try:
        api_response = api_instance.gateway_stop_producer(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_stop_producer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayStopProducer**](GatewayStopProducer.md)|  | 

### Return type

[**GatewayStopProducerOutput**](GatewayStopProducerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayStopProducerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_sync_migration**
> GatewayMigrationSyncOutput gateway_sync_migration(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewaySyncMigration() # GatewaySyncMigration | 

    try:
        api_response = api_instance.gateway_sync_migration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_sync_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewaySyncMigration**](GatewaySyncMigration.md)|  | 

### Return type

[**GatewayMigrationSyncOutput**](GatewayMigrationSyncOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayMigrationSyncResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_update_tmp_users**
> gateway_update_tmp_users(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GatewayUpdateTmpUsers() # GatewayUpdateTmpUsers | 

    try:
        api_instance.gateway_update_tmp_users(body)
    except ApiException as e:
        print("Exception when calling V2Api->gateway_update_tmp_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayUpdateTmpUsers**](GatewayUpdateTmpUsers.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gatewayUpdateTmpUsersResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_logo**
> dict(str, str) get_account_logo()



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    
    try:
        api_response = api_instance.get_account_logo()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_account_logo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getAccountLogoResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_method**
> AuthMethod get_auth_method(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetAuthMethod() # GetAuthMethod | 

    try:
        api_response = api_instance.get_auth_method(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_auth_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAuthMethod**](GetAuthMethod.md)|  | 

### Return type

[**AuthMethod**](AuthMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getAuthMethodResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_secret_value**
> dict(str, str) get_dynamic_secret_value(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetDynamicSecretValue() # GetDynamicSecretValue | 

    try:
        api_response = api_instance.get_dynamic_secret_value(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_dynamic_secret_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetDynamicSecretValue**](GetDynamicSecretValue.md)|  | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDynamicSecretValueResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kube_exec_creds**
> GetKubeExecCredsOutput get_kube_exec_creds(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetKubeExecCreds() # GetKubeExecCreds | 

    try:
        api_response = api_instance.get_kube_exec_creds(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_kube_exec_creds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetKubeExecCreds**](GetKubeExecCreds.md)|  | 

### Return type

[**GetKubeExecCredsOutput**](GetKubeExecCredsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getKubeExecCredsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pki_certificate**
> GetPKICertificateOutput get_pki_certificate(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetPKICertificate() # GetPKICertificate | 

    try:
        api_response = api_instance.get_pki_certificate(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_pki_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetPKICertificate**](GetPKICertificate.md)|  | 

### Return type

[**GetPKICertificateOutput**](GetPKICertificateOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPKICertificateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetRole() # GetRole | 

    try:
        api_response = api_instance.get_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetRole**](GetRole.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getRoleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rotated_secret_value**
> dict(str, object) get_rotated_secret_value(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetRotatedSecretValue() # GetRotatedSecretValue | 

    try:
        api_response = api_instance.get_rotated_secret_value(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_rotated_secret_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetRotatedSecretValue**](GetRotatedSecretValue.md)|  | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getRotatedSecretValueResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rsa_public**
> GetRSAPublicOutput get_rsa_public(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetRSAPublic() # GetRSAPublic | 

    try:
        api_response = api_instance.get_rsa_public(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_rsa_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetRSAPublic**](GetRSAPublic.md)|  | 

### Return type

[**GetRSAPublicOutput**](GetRSAPublicOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getRSAPublicResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_value**
> dict(str, str) get_secret_value(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetSecretValue() # GetSecretValue | 

    try:
        api_response = api_instance.get_secret_value(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_secret_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSecretValue**](GetSecretValue.md)|  | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getSecretValueResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_certificate**
> GetSSHCertificateOutput get_ssh_certificate(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetSSHCertificate() # GetSSHCertificate | 

    try:
        api_response = api_instance.get_ssh_certificate(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_ssh_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSSHCertificate**](GetSSHCertificate.md)|  | 

### Return type

[**GetSSHCertificateOutput**](GetSSHCertificateOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getSSHCertificateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target**
> Target get_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetTarget() # GetTarget | 

    try:
        api_response = api_instance.get_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTarget**](GetTarget.md)|  | 

### Return type

[**Target**](Target.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_details**
> GetTargetDetailsOutput get_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.GetTargetDetails() # GetTargetDetails | 

    try:
        api_response = api_instance.get_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->get_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTargetDetails**](GetTargetDetails.md)|  | 

### Return type

[**GetTargetDetailsOutput**](GetTargetDetailsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getTargetDetailsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_client_delete_rule**
> KMIPClientUpdateResponse kmip_client_delete_rule(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipClientDeleteRule() # KmipClientDeleteRule |  (optional)

    try:
        api_response = api_instance.kmip_client_delete_rule(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_client_delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipClientDeleteRule**](KmipClientDeleteRule.md)|  | [optional] 

### Return type

[**KMIPClientUpdateResponse**](KMIPClientUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipClientDeleteRuleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_client_set_rule**
> KMIPClientUpdateResponse kmip_client_set_rule(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipClientSetRule() # KmipClientSetRule |  (optional)

    try:
        api_response = api_instance.kmip_client_set_rule(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_client_set_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipClientSetRule**](KmipClientSetRule.md)|  | [optional] 

### Return type

[**KMIPClientUpdateResponse**](KMIPClientUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipClientSetRuleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_create_client**
> KmipCreateClientOutput kmip_create_client(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipCreateClient() # KmipCreateClient |  (optional)

    try:
        api_response = api_instance.kmip_create_client(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipCreateClient**](KmipCreateClient.md)|  | [optional] 

### Return type

[**KmipCreateClientOutput**](KmipCreateClientOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipCreateClientResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_delete_client**
> object kmip_delete_client(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipDeleteClient() # KmipDeleteClient |  (optional)

    try:
        api_response = api_instance.kmip_delete_client(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipDeleteClient**](KmipDeleteClient.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipDeleteClientResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_describe_client**
> KMIPClientGetResponse kmip_describe_client(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipDescribeClient() # KmipDescribeClient |  (optional)

    try:
        api_response = api_instance.kmip_describe_client(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_describe_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipDescribeClient**](KmipDescribeClient.md)|  | [optional] 

### Return type

[**KMIPClientGetResponse**](KMIPClientGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipDescribeClientResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_describe_server**
> KmipDescribeServerOutput kmip_describe_server(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipDescribeServer() # KmipDescribeServer |  (optional)

    try:
        api_response = api_instance.kmip_describe_server(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_describe_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipDescribeServer**](KmipDescribeServer.md)|  | [optional] 

### Return type

[**KmipDescribeServerOutput**](KmipDescribeServerOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipDescribeServerResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_list_clients**
> KMIPClientListResponse kmip_list_clients(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipListClients() # KmipListClients |  (optional)

    try:
        api_response = api_instance.kmip_list_clients(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipListClients**](KmipListClients.md)|  | [optional] 

### Return type

[**KMIPClientListResponse**](KMIPClientListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipListClientsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_renew_client_certificate**
> KmipRenewClientCertificateOutput kmip_renew_client_certificate(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipRenewClientCertificate() # KmipRenewClientCertificate |  (optional)

    try:
        api_response = api_instance.kmip_renew_client_certificate(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_renew_client_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipRenewClientCertificate**](KmipRenewClientCertificate.md)|  | [optional] 

### Return type

[**KmipRenewClientCertificateOutput**](KmipRenewClientCertificateOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipRenewClientCertificateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_renew_server_certificate**
> KmipRenewServerCertificateOutput kmip_renew_server_certificate(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipRenewServerCertificate() # KmipRenewServerCertificate |  (optional)

    try:
        api_response = api_instance.kmip_renew_server_certificate(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_renew_server_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipRenewServerCertificate**](KmipRenewServerCertificate.md)|  | [optional] 

### Return type

[**KmipRenewServerCertificateOutput**](KmipRenewServerCertificateOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipRenewServerCertificateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_server_setup**
> KMIPEnvironmentCreateResponse kmip_server_setup(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipServerSetup() # KmipServerSetup |  (optional)

    try:
        api_response = api_instance.kmip_server_setup(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_server_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipServerSetup**](KmipServerSetup.md)|  | [optional] 

### Return type

[**KMIPEnvironmentCreateResponse**](KMIPEnvironmentCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipServerSetupResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_set_server_state**
> KmipSetServerStateOutput kmip_set_server_state(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.KmipSetServerState() # KmipSetServerState |  (optional)

    try:
        api_response = api_instance.kmip_set_server_state(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->kmip_set_server_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmipSetServerState**](KmipSetServerState.md)|  | [optional] 

### Return type

[**KmipSetServerStateOutput**](KmipSetServerStateOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | kmipSetServerStateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_methods**
> ListAuthMethodsOutput list_auth_methods(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.ListAuthMethods() # ListAuthMethods | 

    try:
        api_response = api_instance.list_auth_methods(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->list_auth_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListAuthMethods**](ListAuthMethods.md)|  | 

### Return type

[**ListAuthMethodsOutput**](ListAuthMethodsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listAuthMethodsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ListItemsInPathOutput list_items(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.ListItems() # ListItems | 

    try:
        api_response = api_instance.list_items(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListItems**](ListItems.md)|  | 

### Return type

[**ListItemsInPathOutput**](ListItemsInPathOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listItemsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> ListRolesOutput list_roles(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.ListRoles() # ListRoles | 

    try:
        api_response = api_instance.list_roles(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListRoles**](ListRoles.md)|  | 

### Return type

[**ListRolesOutput**](ListRolesOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listRolesResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_targets**
> ListTargetsOutput list_targets(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.ListTargets() # ListTargets | 

    try:
        api_response = api_instance.list_targets(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->list_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListTargets**](ListTargets.md)|  | 

### Return type

[**ListTargetsOutput**](ListTargetsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listTargetsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_objects**
> object move_objects(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.MoveObjects() # MoveObjects | 

    try:
        api_response = api_instance.move_objects(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->move_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveObjects**](MoveObjects.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | moveObjectsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_creds**
> SystemAccessCredentialsReplyObj raw_creds(body=body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.RawCreds() # RawCreds |  (optional)

    try:
        api_response = api_instance.raw_creds(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->raw_creds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawCreds**](RawCreds.md)|  | [optional] 

### Return type

[**SystemAccessCredentialsReplyObj**](SystemAccessCredentialsReplyObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rawCredsResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_key**
> RefreshKeyOutput refresh_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.RefreshKey() # RefreshKey | 

    try:
        api_response = api_instance.refresh_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->refresh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshKey**](RefreshKey.md)|  | 

### Return type

[**RefreshKeyOutput**](RefreshKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | refreshKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_rbac**
> ReverseRBACOutput reverse_rbac(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.ReverseRBAC() # ReverseRBAC | 

    try:
        api_response = api_instance.reverse_rbac(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->reverse_rbac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReverseRBAC**](ReverseRBAC.md)|  | 

### Return type

[**ReverseRBACOutput**](ReverseRBACOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reverseRBACResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_secret**
> RollbackSecretOutput rollback_secret(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.RollbackSecret() # RollbackSecret | 

    try:
        api_response = api_instance.rollback_secret(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->rollback_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RollbackSecret**](RollbackSecret.md)|  | 

### Return type

[**RollbackSecretOutput**](RollbackSecretOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rollbackSecretResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_key**
> RotateKeyOutput rotate_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRotationSettings() # UpdateRotationSettings | 

    try:
        api_response = api_instance.rotate_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->rotate_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRotationSettings**](UpdateRotationSettings.md)|  | 

### Return type

[**RotateKeyOutput**](RotateKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rotateKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_item_state**
> object set_item_state(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.SetItemState() # SetItemState | 

    try:
        api_response = api_instance.set_item_state(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->set_item_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetItemState**](SetItemState.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | setItemStateResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_rule**
> object set_role_rule(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.SetRoleRule() # SetRoleRule | 

    try:
        api_response = api_instance.set_role_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->set_role_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetRoleRule**](SetRoleRule.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | setRoleRuleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_jwt_with_classic_key**
> SignJWTOutput sign_jwt_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.SignJWTWithClassicKey() # SignJWTWithClassicKey | 

    try:
        api_response = api_instance.sign_jwt_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->sign_jwt_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignJWTWithClassicKey**](SignJWTWithClassicKey.md)|  | 

### Return type

[**SignJWTOutput**](SignJWTOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | signJWTWithClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_pkcs1**
> SignPKCS1Output sign_pkcs1(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.SignPKCS1() # SignPKCS1 | 

    try:
        api_response = api_instance.sign_pkcs1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->sign_pkcs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignPKCS1**](SignPKCS1.md)|  | 

### Return type

[**SignPKCS1Output**](SignPKCS1Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | signPKCS1Response wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_pki_cert_with_classic_key**
> SignPKICertOutput sign_pki_cert_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.SignPKICertWithClassicKey() # SignPKICertWithClassicKey | 

    try:
        api_response = api_instance.sign_pki_cert_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->sign_pki_cert_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignPKICertWithClassicKey**](SignPKICertWithClassicKey.md)|  | 

### Return type

[**SignPKICertOutput**](SignPKICertOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | signPKICertWithClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_creds_auth**
> StaticCredsAuthOutput static_creds_auth(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.StaticCredsAuth() # StaticCredsAuth | 

    try:
        api_response = api_instance.static_creds_auth(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->static_creds_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticCredsAuth**](StaticCredsAuth.md)|  | 

### Return type

[**StaticCredsAuthOutput**](StaticCredsAuthOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | staticCredsAuthResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uid_create_child_token**
> UidCreateChildTokenOutput uid_create_child_token(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidCreateChildToken() # UidCreateChildToken | 

    try:
        api_response = api_instance.uid_create_child_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_create_child_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidCreateChildToken**](UidCreateChildToken.md)|  | 

### Return type

[**UidCreateChildTokenOutput**](UidCreateChildTokenOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uidCreateChildTokenResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uid_generate_token**
> UidGenerateTokenOutput uid_generate_token(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidGenerateToken() # UidGenerateToken | 

    try:
        api_response = api_instance.uid_generate_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_generate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidGenerateToken**](UidGenerateToken.md)|  | 

### Return type

[**UidGenerateTokenOutput**](UidGenerateTokenOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uidGenerateTokenResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uid_list_children**
> UniversalIdentityDetails uid_list_children(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidListChildren() # UidListChildren | 

    try:
        api_response = api_instance.uid_list_children(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_list_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidListChildren**](UidListChildren.md)|  | 

### Return type

[**UniversalIdentityDetails**](UniversalIdentityDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uidListChildrenResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uid_revoke_token**
> object uid_revoke_token(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidRevokeToken() # UidRevokeToken | 

    try:
        api_response = api_instance.uid_revoke_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_revoke_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidRevokeToken**](UidRevokeToken.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uidRevokeTokenResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uid_rotate_token**
> UidRotateTokenOutput uid_rotate_token(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidRotateToken() # UidRotateToken | 

    try:
        api_response = api_instance.uid_rotate_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_rotate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidRotateToken**](UidRotateToken.md)|  | 

### Return type

[**UidRotateTokenOutput**](UidRotateTokenOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uidRotateTokenResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assoc**
> object update_assoc(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateAssoc() # UpdateAssoc | 

    try:
        api_response = api_instance.update_assoc(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_assoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAssoc**](UpdateAssoc.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateAssocResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_target**
> object update_aws_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateAWSTarget() # UpdateAWSTarget | 

    try:
        api_response = api_instance.update_aws_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_aws_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAWSTarget**](UpdateAWSTarget.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateAWSTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_target_details**
> UpdateTargetOutput update_aws_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateAWSTargetDetails() # UpdateAWSTargetDetails | 

    try:
        api_response = api_instance.update_aws_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_aws_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAWSTargetDetails**](UpdateAWSTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_target**
> UpdateAzureTargetOutput update_azure_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateAzureTarget() # UpdateAzureTarget | 

    try:
        api_response = api_instance.update_azure_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_azure_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAzureTarget**](UpdateAzureTarget.md)|  | 

### Return type

[**UpdateAzureTargetOutput**](UpdateAzureTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateAzureTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_db_target**
> UpdateDBTargetOutput update_db_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateDBTarget() # UpdateDBTarget | 

    try:
        api_response = api_instance.update_db_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_db_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDBTarget**](UpdateDBTarget.md)|  | 

### Return type

[**UpdateDBTargetOutput**](UpdateDBTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateDBTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_db_target_details**
> UpdateTargetOutput update_db_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateDBTargetDetails() # UpdateDBTargetDetails | 

    try:
        api_response = api_instance.update_db_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_db_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDBTargetDetails**](UpdateDBTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_eks_target**
> UpdateEKSTargetOutput update_eks_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateEKSTarget() # UpdateEKSTarget | 

    try:
        api_response = api_instance.update_eks_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_eks_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEKSTarget**](UpdateEKSTarget.md)|  | 

### Return type

[**UpdateEKSTargetOutput**](UpdateEKSTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateEKSTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_target**
> UpdateGcpTargetOutput update_gcp_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateGcpTarget() # UpdateGcpTarget | 

    try:
        api_response = api_instance.update_gcp_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_gcp_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGcpTarget**](UpdateGcpTarget.md)|  | 

### Return type

[**UpdateGcpTargetOutput**](UpdateGcpTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateGcpTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gke_target**
> UpdateGKETargetOutput update_gke_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateGKETarget() # UpdateGKETarget | 

    try:
        api_response = api_instance.update_gke_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_gke_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGKETarget**](UpdateGKETarget.md)|  | 

### Return type

[**UpdateGKETargetOutput**](UpdateGKETargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateGKETargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> UpdateItemOutput update_item(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateItem() # UpdateItem | 

    try:
        api_response = api_instance.update_item(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateItem**](UpdateItem.md)|  | 

### Return type

[**UpdateItemOutput**](UpdateItemOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateItemResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_native_k8_s_target**
> UpdateNativeK8STarget update_native_k8_s_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateNativeK8STarget() # UpdateNativeK8STarget | 

    try:
        api_response = api_instance.update_native_k8_s_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_native_k8_s_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateNativeK8STarget**](UpdateNativeK8STarget.md)|  | 

### Return type

[**UpdateNativeK8STarget**](UpdateNativeK8STarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateNativeK8STarget |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rabbit_mq_target**
> UpdateRabbitMQTargetOutput update_rabbit_mq_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRabbitMQTarget() # UpdateRabbitMQTarget | 

    try:
        api_response = api_instance.update_rabbit_mq_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_rabbit_mq_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRabbitMQTarget**](UpdateRabbitMQTarget.md)|  | 

### Return type

[**UpdateRabbitMQTargetOutput**](UpdateRabbitMQTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateRabbitMQTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rabbit_mq_target_details**
> UpdateTargetOutput update_rabbit_mq_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRabbitMQTargetDetails() # UpdateRabbitMQTargetDetails | 

    try:
        api_response = api_instance.update_rabbit_mq_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_rabbit_mq_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRabbitMQTargetDetails**](UpdateRabbitMQTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rdp_target_details**
> UpdateTargetOutput update_rdp_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRDPTargetDetails() # UpdateRDPTargetDetails | 

    try:
        api_response = api_instance.update_rdp_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_rdp_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRDPTargetDetails**](UpdateRDPTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRoleOutput update_role(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRole() # UpdateRole | 

    try:
        api_response = api_instance.update_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRole**](UpdateRole.md)|  | 

### Return type

[**UpdateRoleOutput**](UpdateRoleOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateRoleResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rotated_secret**
> UpdateRotatedSecretOutput update_rotated_secret(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateRotatedSecret() # UpdateRotatedSecret | 

    try:
        api_response = api_instance.update_rotated_secret(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_rotated_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRotatedSecret**](UpdateRotatedSecret.md)|  | 

### Return type

[**UpdateRotatedSecretOutput**](UpdateRotatedSecretOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateRotatedSecretResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rotation_settings**
> RotateKeyOutput update_rotation_settings()



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    
    try:
        api_response = api_instance.update_rotation_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_rotation_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RotateKeyOutput**](RotateKeyOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rotateKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_val**
> UpdateSecretValOutput update_secret_val(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateSecretVal() # UpdateSecretVal | 

    try:
        api_response = api_instance.update_secret_val(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_secret_val: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSecretVal**](UpdateSecretVal.md)|  | 

### Return type

[**UpdateSecretValOutput**](UpdateSecretValOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateSecretValResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_target**
> UpdateSSHTargetOutput update_ssh_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateSSHTarget() # UpdateSSHTarget | 

    try:
        api_response = api_instance.update_ssh_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_ssh_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSSHTarget**](UpdateSSHTarget.md)|  | 

### Return type

[**UpdateSSHTargetOutput**](UpdateSSHTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateSSHTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_target_details**
> UpdateTargetOutput update_ssh_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateSSHTargetDetails() # UpdateSSHTargetDetails | 

    try:
        api_response = api_instance.update_ssh_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_ssh_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSSHTargetDetails**](UpdateSSHTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target**
> UpdateTargetOutput update_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateTarget() # UpdateTarget | 

    try:
        api_response = api_instance.update_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTarget**](UpdateTarget.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_details**
> UpdateTargetOutput update_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = None # object | 

    try:
        api_response = api_instance.update_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_target**
> UpdateWebTargetOutput update_web_target(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateWebTarget() # UpdateWebTarget | 

    try:
        api_response = api_instance.update_web_target(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_web_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWebTarget**](UpdateWebTarget.md)|  | 

### Return type

[**UpdateWebTargetOutput**](UpdateWebTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateWebTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_target_details**
> UpdateTargetOutput update_web_target_details(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UpdateWebTargetDetails() # UpdateWebTargetDetails | 

    try:
        api_response = api_instance.update_web_target_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->update_web_target_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWebTargetDetails**](UpdateWebTargetDetails.md)|  | 

### Return type

[**UpdateTargetOutput**](UpdateTargetOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTargetResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_rsa**
> object upload_rsa(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UploadRSA() # UploadRSA | 

    try:
        api_response = api_instance.upload_rsa(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->upload_rsa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadRSA**](UploadRSA.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uploadRSAResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_jwt_with_classic_key**
> VerifyJWTOutput verify_jwt_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.VerifyJWTWithClassicKey() # VerifyJWTWithClassicKey | 

    try:
        api_response = api_instance.verify_jwt_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->verify_jwt_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyJWTWithClassicKey**](VerifyJWTWithClassicKey.md)|  | 

### Return type

[**VerifyJWTOutput**](VerifyJWTOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verifyJWTWithClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pkcs1**
> object verify_pkcs1(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.VerifyPKCS1() # VerifyPKCS1 | 

    try:
        api_response = api_instance.verify_pkcs1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->verify_pkcs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyPKCS1**](VerifyPKCS1.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verifyPKCS1Response wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pki_cert_with_classic_key**
> VerifyPKICertOutput verify_pki_cert_with_classic_key(body)



### Example

```python
from __future__ import print_function
import time
import akeyless
from akeyless.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)


# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.VerifyPKICertWithClassicKey() # VerifyPKICertWithClassicKey | 

    try:
        api_response = api_instance.verify_pki_cert_with_classic_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->verify_pki_cert_with_classic_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyPKICertWithClassicKey**](VerifyPKICertWithClassicKey.md)|  | 

### Return type

[**VerifyPKICertOutput**](VerifyPKICertOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verifyPKICertWithClassicKeyResponse wraps response body. |  -  |
**0** | errorResponse wraps any error to return it as a JSON object with one \&quot;error\&quot; field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

