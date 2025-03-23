# PKICertificateIssueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_enabled** | **bool** |  | [optional] 
**allow_any_name** | **bool** |  | [optional] 
**allow_copy_ext_from_csr** | **bool** |  | [optional] 
**allow_subdomains** | **bool** |  | [optional] 
**allowed_domains_list** | **List[str]** |  | [optional] 
**allowed_extra_extensions** | **Dict[str, List[str]]** |  | [optional] 
**allowed_ip_sans** | **List[str]** |  | [optional] 
**allowed_uri_sans** | **List[str]** |  | [optional] 
**auto_renew_certificate** | **bool** |  | [optional] 
**basic_constraints_valid_for_non_ca** | **bool** |  | [optional] 
**certificate_authority_mode** | **str** |  | [optional] 
**client_flag** | **bool** |  | [optional] 
**code_signing_flag** | **bool** |  | [optional] 
**country** | **List[str]** |  | [optional] 
**create_private_crl** | **bool** |  | [optional] 
**create_public_crl** | **bool** |  | [optional] 
**destination_path** | **str** | DestinationPath is the destination to save generated certificates | [optional] 
**enforce_hostnames** | **bool** |  | [optional] 
**expiration_events** | [**List[CertificateExpirationEvent]**](CertificateExpirationEvent.md) | ExpirationNotification holds a list of expiration notices that should be sent in case a certificate is about to expire, this value is being propagated to the Certificate resources that are created | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**gw_cluster_url** | **str** | GWClusterURL is required when CAMode is \&quot;public\&quot; and it defines the cluster URL the PKI should be issued from. The GW cluster must have permissions to read associated target&#39;s details | [optional] 
**is_ca** | **bool** |  | [optional] 
**key_bits** | **int** |  | [optional] 
**key_type** | **str** |  | [optional] 
**key_usage_list** | **List[str]** |  | [optional] 
**locality** | **List[str]** |  | [optional] 
**max_path_len** | **int** |  | [optional] 
**non_critical_key_usage** | **bool** |  | [optional] 
**not_before_duration** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**organization_list** | **List[str]** |  | [optional] 
**organization_unit_list** | **List[str]** |  | [optional] 
**pki_issuer_type** | **str** |  | [optional] 
**postal_code** | **List[str]** |  | [optional] 
**protect_generated_certificates** | **bool** | ProtectGeneratedCertificates dictates whether the created certificates should be protected from deletion | [optional] 
**province** | **List[str]** |  | [optional] 
**renew_before_expiration_in_days** | **int** |  | [optional] 
**require_cn** | **bool** |  | [optional] 
**server_flag** | **bool** |  | [optional] 
**street_address** | **List[str]** |  | [optional] 

## Example

```python
from akeyless.models.pki_certificate_issue_details import PKICertificateIssueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PKICertificateIssueDetails from a JSON string
pki_certificate_issue_details_instance = PKICertificateIssueDetails.from_json(json)
# print the JSON string representation of the object
print(PKICertificateIssueDetails.to_json())

# convert the object into a dict
pki_certificate_issue_details_dict = pki_certificate_issue_details_instance.to_dict()
# create an instance of PKICertificateIssueDetails from a dict
pki_certificate_issue_details_from_dict = PKICertificateIssueDetails.from_dict(pki_certificate_issue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


