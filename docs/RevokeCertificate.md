# RevokeCertificate

RevokeCertificate is a command that revokes a certificate and adds it to the crl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | The item id of the certificate to revoke | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate item name to revoke | [optional] 
**serial_number** | **str** | The serial number of the certificate to revoke | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Certificate version to revoke. Required if item-id or name are used. | [optional] 

## Example

```python
from akeyless.models.revoke_certificate import RevokeCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeCertificate from a JSON string
revoke_certificate_instance = RevokeCertificate.from_json(json)
# print the JSON string representation of the object
print(RevokeCertificate.to_json())

# convert the object into a dict
revoke_certificate_dict = revoke_certificate_instance.to_dict()
# create an instance of RevokeCertificate from a dict
revoke_certificate_from_dict = RevokeCertificate.from_dict(revoke_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


