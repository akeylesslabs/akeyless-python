# UpdateCertificateValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tag** | **List[str]** | List of the new tags that will be attached to this item | [optional] 
**certificate_data** | **str** | Content of the certificate in a Base64 format. | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**format** | **str** | CertificateFormat of the certificate and private key, possible values: cer,crt,pem,pfx,p12. Required when passing inline certificate content with --certificate-data or --key-data, otherwise format is derived from the file extension. | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key to use to encrypt the certificate&#39;s key (if empty, the account default protectionKey key will be used) | [optional] 
**key_data** | **str** | Content of the certificate&#39;s private key in a Base64 format. | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Certificate name | 
**rm_tag** | **List[str]** | List of the existent tags that will be removed from this item | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_certificate_value import UpdateCertificateValue

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCertificateValue from a JSON string
update_certificate_value_instance = UpdateCertificateValue.from_json(json)
# print the JSON string representation of the object
print(UpdateCertificateValue.to_json())

# convert the object into a dict
update_certificate_value_dict = update_certificate_value_instance.to_dict()
# create an instance of UpdateCertificateValue from a dict
update_certificate_value_from_dict = UpdateCertificateValue.from_dict(update_certificate_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


