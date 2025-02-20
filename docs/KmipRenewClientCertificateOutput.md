# KmipRenewClientCertificateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from akeyless.models.kmip_renew_client_certificate_output import KmipRenewClientCertificateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of KmipRenewClientCertificateOutput from a JSON string
kmip_renew_client_certificate_output_instance = KmipRenewClientCertificateOutput.from_json(json)
# print the JSON string representation of the object
print(KmipRenewClientCertificateOutput.to_json())

# convert the object into a dict
kmip_renew_client_certificate_output_dict = kmip_renew_client_certificate_output_instance.to_dict()
# create an instance of KmipRenewClientCertificateOutput from a dict
kmip_renew_client_certificate_output_from_dict = KmipRenewClientCertificateOutput.from_dict(kmip_renew_client_certificate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


