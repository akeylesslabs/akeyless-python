# UpdateClassicKeyCertificate

UpdateClassicKeyCertificate is a command that updates the certificate for a classic key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_file_data** | **str** | PEM Certificate in a Base64 format. Used for updating RSA keys&#39; certificates. | [optional] 
**certificate_format** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | ClassicKey name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_classic_key_certificate import UpdateClassicKeyCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClassicKeyCertificate from a JSON string
update_classic_key_certificate_instance = UpdateClassicKeyCertificate.from_json(json)
# print the JSON string representation of the object
print(UpdateClassicKeyCertificate.to_json())

# convert the object into a dict
update_classic_key_certificate_dict = update_classic_key_certificate_instance.to_dict()
# create an instance of UpdateClassicKeyCertificate from a dict
update_classic_key_certificate_from_dict = UpdateClassicKeyCertificate.from_dict(update_classic_key_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


