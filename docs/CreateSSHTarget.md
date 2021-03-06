# CreateSSHTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment about the target | [optional] 
**host** | **str** |  | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | Target name | 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**port** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**private_key_password** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 
**ssh_username** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


