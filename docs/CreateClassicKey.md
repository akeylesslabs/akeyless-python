# CreateClassicKey

CreateClassicKey is a command that creates classic key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Classic Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048, RSA3072, RSA4096, EC256, EC384, GPG] | 
**auto_rotate** | **str** | Whether to automatically rotate every rotation_interval days, or disable existing automatic rotation [true/false] | [optional] 
**cert_file_data** | **str** | Certificate in a PEM format. | [optional] 
**certificate_common_name** | **str** | Common name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_country** | **str** | Country name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_digest_algo** | **str** | Digest algorithm to be used for the certificate key signing. Currently, we support only \&quot;sha256\&quot; so we hide this option for CLI. | [optional] 
**certificate_format** | **str** |  | [optional] 
**certificate_locality** | **str** | Locality for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_organization** | **str** | Organization name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_province** | **str** | Province name for the generated certificate. Relevant only for generate-self-signed-certificate. | [optional] 
**certificate_ttl** | **int** | TTL in days for the generated certificate. Required only for generate-self-signed-certificate. | [optional] 
**conf_file_data** | **str** | The csr config data in base64 encoding | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**generate_self_signed_certificate** | **bool** | Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided. | [optional] 
**gpg_alg** | **str** | gpg alg: Relevant only if GPG key type selected; options: [RSA1024, RSA2048, RSA3072, RSA4096, Ed25519] | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_data** | **str** | Base64-encoded classic key value | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | ClassicKey name | 
**protection_key_name** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_interval** | **str** | The number of days to wait between every automatic rotation (1-365) | [optional] 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_classic_key import CreateClassicKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClassicKey from a JSON string
create_classic_key_instance = CreateClassicKey.from_json(json)
# print the JSON string representation of the object
print(CreateClassicKey.to_json())

# convert the object into a dict
create_classic_key_dict = create_classic_key_instance.to_dict()
# create an instance of CreateClassicKey from a dict
create_classic_key_from_dict = CreateClassicKey.from_dict(create_classic_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


