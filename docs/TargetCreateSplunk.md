# TargetCreateSplunk

targetCreateSplunk is a command that creates a new splunk target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | Splunk token audience (required when using token authentication for rotation) | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**name** | **str** | Target name | 
**password** | **str** | Splunk Password (used when authenticating with username/password) | [optional] 
**token** | **str** | Splunk Token (used when authenticating with token) | [optional] 
**token_owner** | **str** | Splunk Token Owner (required when using token authentication for rotation) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**url** | **str** | Splunk server URL | 
**use_tls** | **bool** | Use TLS certificate verification when connecting to the Splunk management API | [optional] [default to True]
**username** | **str** | Splunk Username (used when authenticating with username/password) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


