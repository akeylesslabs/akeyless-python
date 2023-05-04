# GetCertificateValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The parent PKI Certificate Issuer&#39;s name of the certificate, required when used with display-id and token | [optional] 
**certificate_file_output** | **str** | File to write the certificates to. | [optional] 
**display_id** | **str** | Certificate display ID | [optional] 
**issuance_token** | **str** | Token for getting the issued certificate | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Certificate name | [default to 'dummy_certificate_name']
**private_key_file_output** | **str** | File to write the private key to. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Certificate version | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

