# GenerateCsr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**alt_names** | **str** | The DNS Alternative Names to be included in the CSR certificate (in a comma-separated list) | [optional] 
**certificate_type** | **str** | The certificateType to be included in the CSR certificate (ssl-client/ssl-server/certificate-signing) | [optional] 
**city** | **str** | The city to be included in the CSR certificate | [optional] 
**common_name** | **str** | The commonName to be included in the CSR certificate | 
**country** | **str** | The country to be included in the CSR certificate | [optional] 
**critical** | **bool** | Add critical to the key usage extension (will be false if not added) | [optional] 
**dep** | **str** | The department to be included in the CSR certificate | [optional] 
**description** | **str** | Description of the object | [optional] 
**email_addresses** | **str** | The email addresses Alternative Names to be included in the CSR certificate (in a comma-separated list) | [optional] 
**generate_key** | **bool** | Generate a new csr key | [optional] 
**ip_addresses** | **str** | The ip addresses Alternative Names to be included in the CSR certificate (in a comma-separated list) | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**metadata** | **str** | Deprecated - use description | [optional] 
**name** | **str** | Key name in akeyless | 
**org** | **str** | The organization to be included in the CSR certificate | [optional] 
**state** | **str** | The state to be included in the CSR certificate | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | The URI Subject Alternative Names to be included in the CSR certificate (in a comma-separated list) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


