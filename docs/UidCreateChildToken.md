# UidCreateChildToken

uidCreateChildToken is a command that creates a new child token using Akeyless Universal Identity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** | The universal identity auth method name, required only when uid-token is not provided | [optional] 
**child_deny_inheritance** | **bool** | Deny from new child to create their own children | [optional] 
**child_deny_rotate** | **bool** | Deny from new child to rotate | [optional] 
**child_ttl** | **int** | New child token ttl | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**uid_token_id** | **str** | The ID of the uid-token, required only when uid-token is not provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


