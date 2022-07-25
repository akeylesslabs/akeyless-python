# UpdateSecretVal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] 
**keep_prev_version** | **str** |  | [optional] 
**key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**multiline** | **bool** | The provided value is a multiline value (separated by &#39;\\n&#39;) | [optional] 
**name** | **str** | Secret name | 
**new_version** | **bool** | Deprecated | [optional] 
**password_manager_custom_field** | **dict(str, str)** | For Password Management use, additional fields | [optional] 
**password_manager_inject_url** | **str** | For Password Management use, reflect the website context | [optional] 
**password_manager_password** | **str** | For Password Management use, additional fields | [optional] 
**password_manager_username** | **str** | For Password Management use | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**value** | **str** | The new secret value | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


