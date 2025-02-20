# SSHCertificateIssueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_domains** | **List[str]** | Relevant for host certificate | [optional] 
**allowed_user_key_lengths** | **Dict[str, int]** |  | [optional] 
**allowed_users** | **List[str]** | Relevant for user certificate | [optional] 
**cert_type** | **int** |  | [optional] 
**critical_options** | **Dict[str, str]** |  | [optional] 
**extensions** | **Dict[str, str]** |  | [optional] 
**externally_provided_user_sub_claim_key** | **str** | ExternallyProvidedUserSubClaimKey is the claim key name where the user name should be taken from | [optional] 
**is_externally_provided_user** | **bool** | IsExternallyProvidedUser is true if allow users should be taken from claims and not from AllowedUsers | [optional] 
**principals** | **List[str]** |  | [optional] 
**static_key_id** | **str** | In case it is empty, the key ID will be combination of user identifiers and a random string | [optional] 

## Example

```python
from akeyless.models.ssh_certificate_issue_details import SSHCertificateIssueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SSHCertificateIssueDetails from a JSON string
ssh_certificate_issue_details_instance = SSHCertificateIssueDetails.from_json(json)
# print the JSON string representation of the object
print(SSHCertificateIssueDetails.to_json())

# convert the object into a dict
ssh_certificate_issue_details_dict = ssh_certificate_issue_details_instance.to_dict()
# create an instance of SSHCertificateIssueDetails from a dict
ssh_certificate_issue_details_from_dict = SSHCertificateIssueDetails.from_dict(ssh_certificate_issue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


