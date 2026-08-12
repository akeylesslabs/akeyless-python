# TargetCreateOpenAI

targetCreateOpenAI is a command that creates a new openai target
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key for OpenAI | [optional] 
**api_key_id** | **str** | API key ID | [optional] 
**codex_oauth_access_token** | **str** | Codex OAuth access token (auth.json tokens.access_token), used when codex-oauth-mode&#x3D;chatgpt_oauth | [optional] 
**codex_oauth_account_id** | **str** | Codex OAuth account id (auth.json tokens.account_id), used when codex-oauth-mode&#x3D;chatgpt_oauth | [optional] 
**codex_oauth_mode** | **str** | Auth mode: empty (default, static api-key) or chatgpt_oauth | [optional] 
**codex_oauth_refresh_token** | **str** | Codex OAuth refresh token (auth.json tokens.refresh_token), used when codex-oauth-mode&#x3D;chatgpt_oauth | [optional] 
**delete_protection** | **str** | Protection from accidental deletion of this object [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used) | [optional] 
**max_versions** | **str** | Set the maximum number of versions, limited by the account settings defaults. | [optional] 
**model** | **str** | Default model to use with OpenAI | [optional] 
**name** | **str** | Target name | 
**openai_url** | **str** | Base URL of the OpenAI API | [optional] [default to 'https://api.openai.com/v1']
**organization_id** | **str** | Organization ID | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


