# GetSSHCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The name of the SSH certificate issuer | 
**cert_username** | **str** | The username to sign in the SSH certificate | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**public_key_data** | **str** | SSH public key file contents. If this option is used, the certificate will be printed to stdout | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


