# CertificateIssueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_type** | **str** |  | [optional] 
**max_ttl** | **int** |  | [optional] 
**pki_cert_issuer_details** | [**PKICertificateIssueDetails**](PKICertificateIssueDetails.md) |  | [optional] 
**ssh_cert_issuer_details** | [**SSHCertificateIssueDetails**](SSHCertificateIssueDetails.md) |  | [optional] 

## Example

```python
from akeyless.models.certificate_issue_info import CertificateIssueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateIssueInfo from a JSON string
certificate_issue_info_instance = CertificateIssueInfo.from_json(json)
# print the JSON string representation of the object
print(CertificateIssueInfo.to_json())

# convert the object into a dict
certificate_issue_info_dict = certificate_issue_info_instance.to_dict()
# create an instance of CertificateIssueInfo from a dict
certificate_issue_info_from_dict = CertificateIssueInfo.from_dict(certificate_issue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


