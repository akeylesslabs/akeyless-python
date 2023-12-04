# CreateKey

createKey is a command that creates a new key. [Deprecated: Use command create-dfc-key]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, AES128CBC, AES256CBC, RSA1024, RSA2048, RSA3072, RSA4096] | 
**certificate_common_name** | **str** | Common name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_country** | **str** | Country name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_digest_algo** | **str** | Digest algorithm to be used for the certificate key signing. Currently, we support only \&quot;sha256\&quot; so we hide this option for CLI. | [optional] 
**certificate_locality** | **str** | Locality for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_organization** | **str** | Organization name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_province** | **str** | Province name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_ttl** | **int** | TTL in days for the generated certificate. Required only for generate-self-signed-certificate. | [optional] 
**customer_frg_id** | **str** | The customer fragment ID that will be used to create the key (if empty, the key will be created independently of a customer fragment) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**generate_self_signed_certificate** | **bool** | Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided. | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Key name | 
**split_level** | **int** | The number of fragments that the item will be split into (not includes customer fragment) | [optional] [default to 3]
**tag** | **list[str]** | List of the tags attached to this key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


