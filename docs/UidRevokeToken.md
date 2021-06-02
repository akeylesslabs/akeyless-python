# UidRevokeToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** | The universal identity auth method name | [optional] 
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**revoke_token** | **str** | the universal identity token/token-id to revoke | 
**revoke_type** | **str** | revokeSelf/revokeAll (delete only this token/this token and his children) | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


