# UpdateDBTargetDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_type** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**mongo_db_name** | **str** |  | [optional] 
**mongo_uri** | **str** |  | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Deprecated | [optional] 
**port** | **str** |  | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**pwd** | **str** |  | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


