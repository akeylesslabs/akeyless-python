# KmipRenewClientCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.kmip_renew_client_certificate import KmipRenewClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of KmipRenewClientCertificate from a JSON string
kmip_renew_client_certificate_instance = KmipRenewClientCertificate.from_json(json)
# print the JSON string representation of the object
print(KmipRenewClientCertificate.to_json())

# convert the object into a dict
kmip_renew_client_certificate_dict = kmip_renew_client_certificate_instance.to_dict()
# create an instance of KmipRenewClientCertificate from a dict
kmip_renew_client_certificate_from_dict = KmipRenewClientCertificate.from_dict(kmip_renew_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


