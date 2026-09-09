# GetCertificateValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_issuer_name** | **str** | The parent PKI Certificate Issuer&#39;s name of the certificate, required when used with display-id and token | [optional] 
**display_id** | **str** | Certificate display ID | [optional] 
**format** | **str** | Format to download the certificate in [pem/pfx/jks], pfx/jks require a password | [optional] [default to 'pem']
**ignore_cache** | **str** | Retrieve the Secret value without checking the Gateway&#39;s cache [true/false]. This flag is only relevant when using the RestAPI | [optional] [default to 'false']
**include_private_key** | **bool** | If set, includes the private key in the pfx/jks file, only relevant when format is pfx or jks | [optional] 
**issuance_token** | **str** | Token for getting the issued certificate | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**leaf_only** | **bool** | If set, downloads only the leaf certificate instead of the full chain, only available for certificates issued with split certificate chain enabled | [optional] 
**name** | **str** | Certificate name | [optional] 
**password** | **str** | Password to protect the pfx/jks file, required when format is pfx or jks | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**version** | **int** | Certificate version | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


