# PKICertificateIssueDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_any_name** | **bool** |  | [optional] 
**allow_copy_ext_from_csr** | **bool** |  | [optional] 
**allow_subdomains** | **bool** |  | [optional] 
**allowed_domains_list** | **list[str]** |  | [optional] 
**allowed_extra_extensions** | **dict(str, list[str])** |  | [optional] 
**allowed_uri_sans** | **list[str]** |  | [optional] 
**basic_constraints_valid_for_non_ca** | **bool** |  | [optional] 
**certificate_authority_mode** | **str** |  | [optional] 
**client_flag** | **bool** |  | [optional] 
**code_signing_flag** | **bool** |  | [optional] 
**country** | **list[str]** |  | [optional] 
**create_private_crl** | **bool** |  | [optional] 
**create_public_crl** | **bool** |  | [optional] 
**destination_path** | **str** | DestinationPath is the destination to save generated certificates | [optional] 
**enforce_hostnames** | **bool** |  | [optional] 
**expiration_events** | [**list[CertificateExpirationEvent]**](CertificateExpirationEvent.md) | ExpirationNotification holds a list of expiration notices that should be sent in case a certificate is about to expire, this value is being propagated to the Certificate resources that are created | [optional] 
**gw_cluster_id** | **int** |  | [optional] 
**gw_cluster_url** | **str** | GWClusterURL is required when CAMode is \&quot;public\&quot; and it defines the cluster URL the PKI should be issued from. The GW cluster must have permissions to read associated target&#39;s details | [optional] 
**is_ca** | **bool** |  | [optional] 
**key_bits** | **int** |  | [optional] 
**key_type** | **str** |  | [optional] 
**key_usage_list** | **list[str]** |  | [optional] 
**locality** | **list[str]** |  | [optional] 
**not_before_duration** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**organization_list** | **list[str]** |  | [optional] 
**organization_unit_list** | **list[str]** |  | [optional] 
**postal_code** | **list[str]** |  | [optional] 
**protect_generated_certificates** | **bool** | ProtectGeneratedCertificates dictates whether the created certificates should be protected from deletion | [optional] 
**province** | **list[str]** |  | [optional] 
**require_cn** | **bool** |  | [optional] 
**server_flag** | **bool** |  | [optional] 
**street_address** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


