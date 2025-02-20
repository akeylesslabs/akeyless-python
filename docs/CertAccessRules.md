# CertAccessRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_cors** | **List[str]** | a list of allowed cors domains if used for browser authentication | [optional] 
**bound_common_names** | **List[str]** | A list of names. At least one must exist in the Common Name. Supports globbing. | [optional] 
**bound_dns_sans** | **List[str]** | A list of DNS names. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_email_sans** | **List[str]** | A list of Email Addresses. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_extensions** | **List[str]** | A list of extensions formatted as \&quot;oid:value\&quot;. Expects the extension value to be some type of ASN1 encoded string. All values must match. Supports globbing on \&quot;value\&quot;. | [optional] 
**bound_organizational_units** | **List[str]** | A list of Organizational Units names. At least one must exist in the OU field. | [optional] 
**bound_uri_sans** | **List[str]** | A list of URIs. At least one must exist in the SANs. Supports globbing. | [optional] 
**certificate** | **str** | Base64 encdoed PEM certificate | [optional] 
**revoked_cert_ids** | **List[str]** | A list of revoked cert ids | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

## Example

```python
from akeyless.models.cert_access_rules import CertAccessRules

# TODO update the JSON string below
json = "{}"
# create an instance of CertAccessRules from a JSON string
cert_access_rules_instance = CertAccessRules.from_json(json)
# print the JSON string representation of the object
print(CertAccessRules.to_json())

# convert the object into a dict
cert_access_rules_dict = cert_access_rules_instance.to_dict()
# create an instance of CertAccessRules from a dict
cert_access_rules_from_dict = CertAccessRules.from_dict(cert_access_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


