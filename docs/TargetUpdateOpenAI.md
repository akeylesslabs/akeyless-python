# TargetUpdateOpenAI

targetUpdateOpenAI is a command that updates an existing openai target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key for OpenAI | [optional] 
**api_key_id** | **str** | API key ID | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_comment']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**keep_prev_version** | **str** | Whether to keep previous version [true/false]. If not set, use default according to account settings | [optional] 
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**model** | **str** | Default model to use with OpenAI | [optional] 
**name** | **str** | Target name | 
**new_comment** | **str** | Deprecated - use description | [optional] [default to 'default_comment']
**new_name** | **str** | New target name | [optional] 
**openai_url** | **str** | Base URL of the OpenAI API | [optional] [default to 'https://api.openai.com/v1']
**organization_id** | **str** | Organization ID | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


