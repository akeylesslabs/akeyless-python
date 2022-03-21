# GatewayUpdateProducerGcp

gatewayUpdateProducerGcp is a command that updates a GCP producer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_cred_type** | **str** |  | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**gcp_key_algo** | **str** | Service account key algorithm, e.g. KEY_ALG_RSA_1024 | [optional] 
**gcp_sa_email** | **str** | GCP service account email | [optional] 
**gcp_token_scopes** | **str** | Access token scopes list, e.g. scope1,scope2 | [optional] 
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


