# ImportPasswords

importPasswords is a command that import passwords
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'personal']
**format** | **str** | Password format type [LastPass/Chrome/Firefox/1password/keeper/bitwarden/dashlane] | [optional] [default to 'LastPass']
**import_path** | **str** | File path | 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**protection_key** | **str** | The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used) | [optional] 
**target_folder** | **str** | Target folder for imported passwords | [optional] [default to '/']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**update_mode** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


