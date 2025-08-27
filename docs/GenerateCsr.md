# GenerateCsr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**alt_names** | **str** | A comma-separated list of dns alternative names | [optional] 
**certificate_type** | **str** | The certificate type to be included in the CSR certificate (ssl-client/ssl-server/certificate-signing) | [optional] 
**city** | **str** | The city to be included in the CSR certificate | [optional] 
**common_name** | **str** | The common name to be included in the CSR certificate | 
**country** | **str** | The country to be included in the CSR certificate | [optional] 
**critical** | **bool** | Add critical to the key usage extension (will be false if not added) | [optional] 
**dep** | **str** | The department to be included in the CSR certificate | [optional] 
**email_addresses** | **str** | A comma-separated list of email addresses alternative names | [optional] 
**export_private_key** | **bool** | The flag to indicate if the private key should be exported | [optional] [default to False]
**generate_key** | **bool** | Generate a new classic key for the csr | [optional] 
**hash_algorithm** | **str** | Specifies the hash algorithm used for the encryption key&#39;s operations, available options: SHA256, SHA384, SHA512 | [optional] [default to 'SHA256']
**ip_addresses** | **str** | A comma-separated list of ip addresses alternative names | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key_type** | **str** | The type of the key to generate (classic-key/dfc) | [default to 'classic-key']
**name** | **str** | The key name | 
**org** | **str** | The organization to be included in the CSR certificate | [optional] 
**split_level** | **int** | The number of fragments that the item will be split into (not includes customer fragment) | [optional] [default to 3]
**state** | **str** | The state to be included in the CSR certificate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | A comma-separated list of uri alternative names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


