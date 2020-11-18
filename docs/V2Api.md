# akeyless.V2Api

All URIs are relative to *https://api.akeyless.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assoc_role_auth_method**](V2Api.md#assoc_role_auth_method) | **POST** /assoc-role-am | 
[**auth**](V2Api.md#auth) | **POST** /auth | 
[**configure**](V2Api.md#configure) | **POST** /configure | 
[**create_auth_method**](V2Api.md#create_auth_method) | **POST** /create-auth-method | 
[**create_auth_method_awsiam**](V2Api.md#create_auth_method_awsiam) | **POST** /create-auth-method-aws-iam | 
[**create_auth_method_azure_ad**](V2Api.md#create_auth_method_azure_ad) | **POST** /create-auth-method-azure-ad | 
[**create_auth_method_huawei**](V2Api.md#create_auth_method_huawei) | **POST** /create-auth-method-huawei | 
[**create_auth_method_o_auth2**](V2Api.md#create_auth_method_o_auth2) | **POST** /create-auth-method-oauth2 | 
[**create_auth_method_saml**](V2Api.md#create_auth_method_saml) | **POST** /create-auth-method-saml | 
[**create_auth_method_universal_identity**](V2Api.md#create_auth_method_universal_identity) | **POST** /create-auth-method-universal-identity | 
[**create_dynamic_secret**](V2Api.md#create_dynamic_secret) | **POST** /create-dynamic-secret | 
[**create_key**](V2Api.md#create_key) | **POST** /create-key | 
[**create_pki_cert_issuer**](V2Api.md#create_pki_cert_issuer) | **POST** /create-pki-cert-issuer | 
[**create_role**](V2Api.md#create_role) | **POST** /create-role | 
[**create_secret**](V2Api.md#create_secret) | **POST** /create-secret | 
[**create_ssh_cert_issuer**](V2Api.md#create_ssh_cert_issuer) | **POST** /create-ssh-cert-issuer | 
[**decrypt**](V2Api.md#decrypt) | **POST** /decrypt | 
[**decrypt_pkcs1**](V2Api.md#decrypt_pkcs1) | **POST** /decrypt-pkcs1 | 
[**delete_auth_method**](V2Api.md#delete_auth_method) | **POST** /delete-auth-method | 
[**delete_auth_methods**](V2Api.md#delete_auth_methods) | **POST** /delete-auth-methods | 
[**delete_item**](V2Api.md#delete_item) | **POST** /delete-item | 
[**delete_items**](V2Api.md#delete_items) | **POST** /delete-items | 
[**delete_role**](V2Api.md#delete_role) | **POST** /delete-role | 
[**delete_role_association**](V2Api.md#delete_role_association) | **POST** /delete-assoc | 
[**delete_role_rule**](V2Api.md#delete_role_rule) | **POST** /delete-role-rule | 
[**delete_roles**](V2Api.md#delete_roles) | **POST** /delete-roles | 
[**describe_item**](V2Api.md#describe_item) | **POST** /describe-item | 
[**encrypt**](V2Api.md#encrypt) | **POST** /encrypt | 
[**encrypt_pkcs1**](V2Api.md#encrypt_pkcs1) | **POST** /encrypt-pkcs1 | 
[**get_auth_method**](V2Api.md#get_auth_method) | **POST** /get-auth-method | 
[**get_dynamic_secret_value**](V2Api.md#get_dynamic_secret_value) | **POST** /get-dynamic-secret-value | 
[**get_role**](V2Api.md#get_role) | **POST** /get-role | 
[**get_rsa_public**](V2Api.md#get_rsa_public) | **POST** /get-rsa-public | 
[**get_secret_value**](V2Api.md#get_secret_value) | **POST** /get-secret-value | 
[**get_ssh_certificate**](V2Api.md#get_ssh_certificate) | **POST** /get-ssh-certificate | 
[**list_auth_methods**](V2Api.md#list_auth_methods) | **POST** /list-auth-methods | 
[**list_items**](V2Api.md#list_items) | **POST** /list-items | 
[**list_roles**](V2Api.md#list_roles) | **POST** /list-roles | 
[**move_objects**](V2Api.md#move_objects) | **POST** /move-objects | 
[**refresh_key**](V2Api.md#refresh_key) | **POST** /refresh-key | 
[**reverse_rbac**](V2Api.md#reverse_rbac) | **POST** /reverse-rbac | 
[**rollback_secret**](V2Api.md#rollback_secret) | **POST** /rollback-secret | 
[**rotate_key**](V2Api.md#rotate_key) | **POST** /rotate-key | 
[**set_item_state**](V2Api.md#set_item_state) | **POST** /set-item-state | 
[**set_role_rule**](V2Api.md#set_role_rule) | **POST** /set-role-rule | 
[**sign_pkcs1**](V2Api.md#sign_pkcs1) | **POST** /sign-pkcs1 | 
[**static_creds_auth**](V2Api.md#static_creds_auth) | **POST** /static-creds-auth | 
[**uid_create_child_token**](V2Api.md#uid_create_child_token) | **POST** /uid-create-child-token | 
[**uid_generate_token**](V2Api.md#uid_generate_token) | **POST** /uid-generate-token | 
[**uid_list_children**](V2Api.md#uid_list_children) | **POST** /uid-list-children | 
[**uid_revoke_token**](V2Api.md#uid_revoke_token) | **POST** /uid-revoke-token | 
[**uid_rotate_token**](V2Api.md#uid_rotate_token) | **POST** /uid-rotate-token | 
[**update_item**](V2Api.md#update_item) | **POST** /update-item | 
[**update_role**](V2Api.md#update_role) | **POST** /update-role | 
[**update_secret_val**](V2Api.md#update_secret_val) | **POST** /update-secret-val | 
[**upload_rsa**](V2Api.md#upload_rsa) | **POST** /upload-rsa | 
[**verify_pkcs1**](V2Api.md#verify_pkcs1) | **POST** /verify-pkcs1 | 


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
    body = akeyless.RotateKey() # RotateKey | 

    try:
        api_response = api_instance.rotate_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->rotate_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RotateKey**](RotateKey.md)|  | 

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

