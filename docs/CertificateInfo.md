# CertificateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ext_key_usage** | **List[int]** |  | [optional] 
**key_usage** | **int** | KeyUsage represents the set of actions that are valid for a given key. It&#39;s a bitmap of the KeyUsage* constants. | [optional] 
**crl_distribution_points** | **List[str]** |  | [optional] 
**dns_names** | **List[str]** |  | [optional] 
**email_addresses** | **List[str]** |  | [optional] 
**extensions** | [**List[Extension]**](Extension.md) |  | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 
**is_ca** | **bool** |  | [optional] 
**issuer** | [**Name**](Name.md) |  | [optional] 
**issuing_certificate_url** | **List[str]** |  | [optional] 
**key_size** | **int** |  | [optional] 
**not_after** | **datetime** |  | [optional] 
**not_before** | **datetime** |  | [optional] 
**ocsp_server** | **List[str]** |  | [optional] 
**public_key_algorithm_name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**sha_1_fingerprint** | **str** |  | [optional] 
**sha_256_fingerprint** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**signature_algorithm_name** | **str** |  | [optional] 
**subject** | [**Name**](Name.md) |  | [optional] 
**subject_public_key** | **str** |  | [optional] 
**uris** | **List[str]** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from akeyless.models.certificate_info import CertificateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateInfo from a JSON string
certificate_info_instance = CertificateInfo.from_json(json)
# print the JSON string representation of the object
print(CertificateInfo.to_json())

# convert the object into a dict
certificate_info_dict = certificate_info_instance.to_dict()
# create an instance of CertificateInfo from a dict
certificate_info_from_dict = CertificateInfo.from_dict(certificate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


