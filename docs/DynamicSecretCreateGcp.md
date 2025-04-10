# DynamicSecretCreateGcp

dynamicSecretCreateGcp is a command that creates a GCP dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**gcp_cred_type** | **str** |  | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_key_algo** | **str** | Service account key algorithm, e.g. KEY_ALG_RSA_1024 | [optional] 
**gcp_sa_email** | **str** | The email of the fixed service acocunt to generate keys or tokens for. (revelant for service-account-type&#x3D;fixed) | [optional] 
**gcp_token_scopes** | **str** | Access token scopes list, e.g. scope1,scope2 | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**role_binding** | **str** | Role binding definitions in json format | [optional] 
**service_account_type** | **str** | The type of the gcp dynamic secret. Options[fixed, dynamic] | [default to 'fixed']
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


