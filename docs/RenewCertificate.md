# RenewCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | [optional] 
**generate_key** | **bool** | Generate a new key as part of the certificate renewal | [optional] 
**item_id** | **int** | Certificate item id | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.renew_certificate import RenewCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of RenewCertificate from a JSON string
renew_certificate_instance = RenewCertificate.from_json(json)
# print the JSON string representation of the object
print(RenewCertificate.to_json())

# convert the object into a dict
renew_certificate_dict = renew_certificate_instance.to_dict()
# create an instance of RenewCertificate from a dict
renew_certificate_from_dict = RenewCertificate.from_dict(renew_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


