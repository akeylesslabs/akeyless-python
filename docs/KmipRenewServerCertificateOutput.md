# KmipRenewServerCertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_renew_server_certificate_output import KmipRenewServerCertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipRenewServerCertificateOutput from a JSON string
kmip_renew_server_certificate_output_instance = KmipRenewServerCertificateOutput.from_json(json)
# print the JSON string representation of the object
print(KmipRenewServerCertificateOutput.to_json())

# convert the object into a dict
kmip_renew_server_certificate_output_dict = kmip_renew_server_certificate_output_instance.to_dict()
# create an instance of KmipRenewServerCertificateOutput from a dict
kmip_renew_server_certificate_output_from_dict = KmipRenewServerCertificateOutput.from_dict(kmip_renew_server_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


