# TargetCreateGemini

targetCreateGemini is a command that creates a new gemini target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key for Gemini | [optional] 
**description** | **str** | Description of the object | [optional] 
**gemini_url** | **str** | Base URL of the Gemini API | [optional] [default to 'https://generativelanguage.googleapis.com']
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**model** | **str** | Default model to use with Gemini | [optional] 
**name** | **str** | Target name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


