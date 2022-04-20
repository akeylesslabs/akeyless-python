# CertAccessRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_common_names** | **list[str]** | A list of names. At least one must exist in the Common Name. Supports globbing. | [optional] 
**bound_dns_sans** | **list[str]** | A list of DNS names. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_email_sans** | **list[str]** | A list of Email Addresses. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_extensions** | **list[str]** | A list of extensions formatted as \&quot;oid:value\&quot;. Expects the extension value to be some type of ASN1 encoded string. All values must match. Supports globbing on \&quot;value\&quot;. | [optional] 
**bound_organizational_units** | **list[str]** | A list of Organizational Units names. At least one must exist in the OU field. | [optional] 
**bound_uri_sans** | **list[str]** | A list of URIs. At least one must exist in the SANs. Supports globbing. | [optional] 
**certificate** | **list[int]** | Base64 encdoed PEM certificate | [optional] 
**revoked_cert_ids** | **list[str]** | A list of revoked cert ids | [optional] 
**unique_identifier** | **str** | A unique identifier to distinguish different users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


