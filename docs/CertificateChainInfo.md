# CertificateChainInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew_certificate** | **bool** |  | [optional] 
**certificate_chain** | [**list[CertificateInfo]**](CertificateInfo.md) |  | [optional] 
**certificate_format** | **str** |  | [optional] 
**certificate_has_private_key** | **bool** |  | [optional] 
**certificate_issuer_gw_cluster_id** | **int** |  | [optional] 
**certificate_issuer_gw_cluster_url** | **str** |  | [optional] 
**certificate_issuer_item_id** | **int** |  | [optional] 
**certificate_issuer_name** | **str** |  | [optional] 
**certificate_pem** | **str** |  | [optional] 
**certificate_status** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**csr_pem** | **str** | CSRPEM contains the PEM-encoded CSR for pending certificates (HTTP-01 challenge) | [optional] 
**error_message** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**expiration_events** | [**list[CertificateExpirationEvent]**](CertificateExpirationEvent.md) |  | [optional] 
**external_ca_id** | [**NullString**](NullString.md) |  | [optional] 
**issuance_status** | **str** |  | [optional] 
**leaf_certificate_pem** | **str** | LeafCertificatePem contains only the leaf certificate, derived from CertificatePem. Populated only when the certificate was issued with SplitCertificateChain enabled. | [optional] 
**not_before** | **datetime** |  | [optional] 
**renew_before_expiration_in_days** | **int** |  | [optional] 
**split_certificate_chain** | **bool** | SplitCertificateChain reflects whether this certificate was issued while its PKI Cert Issuer had split-certificate-chain enabled. When true, LeafCertificatePem is populated in addition to CertificatePem (which always holds the full chain). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


