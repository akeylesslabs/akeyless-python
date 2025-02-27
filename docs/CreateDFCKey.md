# CreateDFCKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | DFCKey type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, AES128CBC, AES256CBC, RSA1024, RSA2048, RSA3072, RSA4096] | 
**auto_rotate** | **str** | Whether to automatically rotate every rotation_interval days, or disable existing automatic rotation [true/false] | [optional] 
**certificate_common_name** | **str** | Common name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_country** | **str** | Country name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_digest_algo** | **str** | Digest algorithm to be used for the certificate key signing. Currently, we support only \&quot;sha256\&quot; so we hide this option for CLI. | [optional] 
**certificate_format** | **str** |  | [optional] 
**certificate_locality** | **str** | Locality for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_organization** | **str** | Organization name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_province** | **str** | Province name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_ttl** | **int** | TTL in days for the generated certificate. Required only for generate-self-signed-certificate. | [optional] 
**conf_file_data** | **str** | The csr config data in base64 encoding | [optional] 
**customer_frg_id** | **str** | The customer fragment ID that will be used to create the DFC key (if empty, the key will be created independently of a customer fragment) | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**generate_self_signed_certificate** | **bool** | Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided. | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | DFCKey name | 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic rotation (7-365) | [optional] 
**split_level** | **int** | The number of fragments that the item will be split into (not includes customer fragment) | [optional] [default to 3]
**tag** | **List[str]** | List of the tags attached to this DFC key | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_dfc_key import CreateDFCKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDFCKey from a JSON string
create_dfc_key_instance = CreateDFCKey.from_json(json)
# print the JSON string representation of the object
print(CreateDFCKey.to_json())

# convert the object into a dict
create_dfc_key_dict = create_dfc_key_instance.to_dict()
# create an instance of CreateDFCKey from a dict
create_dfc_key_from_dict = CreateDFCKey.from_dict(create_dfc_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


