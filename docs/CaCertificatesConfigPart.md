# CaCertificatesConfigPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_store** | [**List[CertificateStore]**](CertificateStore.md) |  | [optional] 

## Example

```python
from akeyless.models.ca_certificates_config_part import CaCertificatesConfigPart

# TODO update the JSON string below
json = "{}"
# create an instance of CaCertificatesConfigPart from a JSON string
ca_certificates_config_part_instance = CaCertificatesConfigPart.from_json(json)
# print the JSON string representation of the object
print(CaCertificatesConfigPart.to_json())

# convert the object into a dict
ca_certificates_config_part_dict = ca_certificates_config_part_instance.to_dict()
# create an instance of CaCertificatesConfigPart from a dict
ca_certificates_config_part_from_dict = CaCertificatesConfigPart.from_dict(ca_certificates_config_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


