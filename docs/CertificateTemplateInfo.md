# CertificateTemplateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**csr_cnf_base_64** | **str** |  | [optional] 
**digest_algo** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**self_signed_enabled** | **bool** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from akeyless.models.certificate_template_info import CertificateTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateTemplateInfo from a JSON string
certificate_template_info_instance = CertificateTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(CertificateTemplateInfo.to_json())

# convert the object into a dict
certificate_template_info_dict = certificate_template_info_instance.to_dict()
# create an instance of CertificateTemplateInfo from a dict
certificate_template_info_from_dict = CertificateTemplateInfo.from_dict(certificate_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


