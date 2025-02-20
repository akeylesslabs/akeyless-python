# CreateCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_data** | **str** | Content of the certificate in a Base64 format. | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**expiration_event_in** | **List[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**format** | **str** | CertificateFormat of the certificate and private key, possible values: cer,crt,pem,pfx,p12. Required when passing inline certificate content with --certificate-data or --key-data, otherwise format is derived from the file extension. | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key to use to encrypt the certificate&#39;s key (if empty, the account default protectionKey key will be used) | [optional] 
**key_data** | **str** | Content of the certificate&#39;s private key in a Base64 format. | [optional] 
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Certificate name | 
**tags** | **List[str]** | Add tags attached to this object | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_certificate import CreateCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCertificate from a JSON string
create_certificate_instance = CreateCertificate.from_json(json)
# print the JSON string representation of the object
print(CreateCertificate.to_json())

# convert the object into a dict
create_certificate_dict = create_certificate_instance.to_dict()
# create an instance of CreateCertificate from a dict
create_certificate_from_dict = CreateCertificate.from_dict(create_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


