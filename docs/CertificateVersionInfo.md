# CertificateVersionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_after** | **datetime** |  | [optional] 
**not_before** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from akeyless.models.certificate_version_info import CertificateVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateVersionInfo from a JSON string
certificate_version_info_instance = CertificateVersionInfo.from_json(json)
# print the JSON string representation of the object
print(CertificateVersionInfo.to_json())

# convert the object into a dict
certificate_version_info_dict = certificate_version_info_instance.to_dict()
# create an instance of CertificateVersionInfo from a dict
certificate_version_info_from_dict = CertificateVersionInfo.from_dict(certificate_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


