# GetKubeExecCreds

getKubeExecCreds is a command that gets credentials for authentication with Kubernetes cluster based on a PKI cert issuer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | **str** | The Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 
**cert_issuer_name** | **str** | The name of the PKI certificate issuer | 
**common_name** | **str** | The common name to be included in the PKI certificate | [optional] 
**key_data_base64** | **str** | PKI key file contents. If this option is used, the certificate will be printed to stdout | [optional] 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uri_sans** | **str** | The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list) | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


