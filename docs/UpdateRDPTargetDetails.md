# UpdateRDPTargetDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** |  | [optional] 
**admin_pwd** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**host_port** | **str** |  | [optional] 
**name** | **str** | Target name | 
**new_version** | **bool** | Whether to create a new version of not | [optional] [default to False]
**password** | **str** | Required only when the authentication process requires a username and password | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**username** | **str** | Required only when the authentication process requires a username and password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


