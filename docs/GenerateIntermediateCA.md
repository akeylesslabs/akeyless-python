# GenerateIntermediateCA

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**allowed_domains** | **str** | Allowed domains for future leaf issuance, not inherited into the SCEP subordinate CA certificate | [optional] 
**common_name** | **str** | Optional Common Name for the intermediate CA certificate | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**destination_path** | **str** | Destination path for SCEP-issued leaf certificates. Not derived from the CA certificate item path. | [optional] 
**enable_scep** | **bool** | Enable the fixed SCEP Stage 1 profile | [optional] 
**extended_key_usage** | **str** | Extended key usage for future leaf issuance (serverauth / clientauth / codesigning) | [optional] [default to 'serverauth,clientauth']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**max_path_len** | **int** | The maximum path length of the generated intermediate CA certificate | [optional] [default to 0]
**name** | **str** | Base path for derived intermediate CA resources | 
**parent_ca_name** | **str** | Parent PKI certificate issuer name | [optional] 
**scep_password** | **str** | SCEP static challenge password. Request-only; never returned | [optional] 
**split_level** | **int** | The number of fragments that the DFC key will be split into | [optional] [default to 3]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **str** | Maximum TTL for certificates issued by the new intermediate issuer, supported formats are s,m,h,d | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


