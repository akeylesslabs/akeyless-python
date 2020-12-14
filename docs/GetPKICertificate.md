# GetPKICertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | **str** | The Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | 
**common_name** | **str** | The common name to be included in the PKI certificate | [optional] 
**key_file_path** | **str** | The client public or private key file path (in case of a private key, it will be use to extract the public key) | 
**outfile** | **str** | Output file path with the certificate. If not provided, the file with the certificate will be created in the same location of the provided public key with the -cert extension | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


