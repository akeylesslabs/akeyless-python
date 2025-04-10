# CertificateInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ext_key_usage** | **list[int]** |  | [optional] 
**key_usage** | **int** | KeyUsage represents the set of actions that are valid for a given key. It&#39;s a bitmap of the KeyUsage* constants. | [optional] 
**crl_distribution_points** | **list[str]** |  | [optional] 
**dns_names** | **list[str]** |  | [optional] 
**email_addresses** | **list[str]** |  | [optional] 
**extensions** | [**list[Extension]**](Extension.md) |  | [optional] 
**ip_addresses** | **list[str]** |  | [optional] 
**is_ca** | **bool** |  | [optional] 
**issuer** | [**Name**](Name.md) |  | [optional] 
**issuing_certificate_url** | **list[str]** |  | [optional] 
**key_size** | **int** |  | [optional] 
**not_after** | **datetime** |  | [optional] 
**not_before** | **datetime** |  | [optional] 
**ocsp_server** | **list[str]** |  | [optional] 
**public_key_algorithm_name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**sha_1_fingerprint** | **str** |  | [optional] 
**sha_256_fingerprint** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**signature_algorithm_name** | **str** |  | [optional] 
**subject** | [**Name**](Name.md) |  | [optional] 
**subject_public_key** | **str** |  | [optional] 
**uris** | **list[str]** |  | [optional] 
**version** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


