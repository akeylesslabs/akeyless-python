# CreateSalesforceTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_data** | **str** | Base64 encoded PEM cert to use when uploading a new key to Salesforce | [optional] 
**ca_cert_name** | **str** | name of the certificate in Salesforce tenant to use when uploading new key | [optional] 
**client_id** | **str** | Client ID of the oauth2 app to use for connecting to Salesforce | 
**client_secret** | **str** | Client secret of the oauth2 app to use for connecting to Salesforce | 
**comment** | **str** | Comment about the target | [optional] 
**email** | **str** | The email of the user attached to the oauth2 app used for connecting to Salesforce | 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Target name | 
**password** | **str** | The password of the user attached to the oauth2 app used for connecting to Salesforce | 
**security_token** | **str** | The security token of the user attached to the oauth2 app used for connecting to Salesforce | 
**tenant_url** | **str** | Url of the Salesforce tenant | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


