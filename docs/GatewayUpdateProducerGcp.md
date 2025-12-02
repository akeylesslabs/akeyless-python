# GatewayUpdateProducerGcp

gatewayUpdateProducerGcp is a command that updates a GCP producer [Deprecated: Use dynamic-secret-update-gcp command]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** |  | [optional] 
**custom_username_template** | **str** | Customize how temporary usernames are generated using go template | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**fixed_user_claim_keyname** | **str** | For externally provided users, denotes the key-name of IdP claim to extract the username from (Relevant only when --access-type&#x3D;external) | [optional] [default to 'ext_email']
**gcp_cred_type** | **str** |  | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_key_algo** | **str** | Service account key algorithm, e.g. KEY_ALG_RSA_1024 (Relevant only when --access-type&#x3D;sa and --gcp-cred-type&#x3D;key) | [optional] 
**gcp_project_id** | **str** | GCP Project ID override for dynamic secret operations | [optional] 
**gcp_sa_email** | **str** | The email of the fixed service account to generate keys or tokens for (Relevant only when --access-type&#x3D;sa and --service-account-type&#x3D;fixed) | [optional] 
**gcp_token_scopes** | **str** | Access token scopes list, e.g. scope1,scope2 (Relevant only when --access-type&#x3D;sa; required when --gcp-cred-type&#x3D;token) | [optional] 
**item_custom_fields** | **dict(str, str)** | Additional custom fields to associate with the item | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**role_binding** | **str** | Role binding definitions in JSON format (Relevant only when --access-type&#x3D;sa and --service-account-type&#x3D;dynamic) | [optional] 
**role_names** | **str** | Comma-separated list of GCP roles to assign to the user (Relevant only when --access-type&#x3D;external) | [optional] 
**secure_access_delay** | **int** | The delay duration, in seconds, to wait after generating just-in-time credentials. Accepted range: 0-120 seconds | [optional] 
**secure_access_enable** | **str** | Enable/Disable secure remote access [true/false] | [optional] 
**secure_access_url** | **str** | Destination URL to inject secrets | [optional] 
**secure_access_web_browsing** | **bool** | Secure browser via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**secure_access_web_proxy** | **bool** | Web-Proxy via Akeyless&#39;s Secure Remote Access (SRA) | [optional] [default to False]
**service_account_type** | **str** | The type of the GCP service account. Options [fixed, dynamic] (Relevant only when --access-type&#x3D;sa) | [optional] [default to 'fixed']
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


