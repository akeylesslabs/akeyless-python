# UpdateSecretVal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**multiline** | **bool** | The provided value is a multiline value (separated by &#39;\\n&#39;) | [optional] 
**name** | **str** | Secret name | 
**new_version** | **bool** | Whether to create a new version of not | [optional] [default to False]
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 
**value** | **str** | The new secret value | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


