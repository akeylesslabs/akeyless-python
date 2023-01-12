# UpdateCertificateValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_data** | **str** | Content of the certificate PEM in a Base64 format. | [optional] 
**expiration_event_in** | **list[str]** | How many days before the expiration of the certificate would you like to be notified. | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**key** | **str** | The name of a key to use to encrypt the certificate&#39;s key (if empty, the account default protectionKey key will be used) | [optional] 
**key_data** | **str** | Content of the certificate&#39;s private key PEM in a Base64 format. | [optional] 
**name** | **str** | Certificate name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


