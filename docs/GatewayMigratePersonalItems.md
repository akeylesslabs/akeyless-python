# GatewayMigratePersonalItems

gatewayMigratePersonalItems is a command that migrate personal items from external vault
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_1password_email** | **str** | 1Password user email to connect to the API | [optional] 
**_1password_password** | **str** | 1Password user password to connect to the API | [optional] 
**_1password_secret_key** | **str** | 1Password user secret key to connect to the API | [optional] 
**_1password_url** | **str** | 1Password api container url | [optional] 
**_1password_vaults** | **list[str]** | 1Password list of vault to get the items from | [optional] 
**json** | **bool** | Set output format to JSON | [optional] 
**protection_key** | **str** | The name of a key that used to encrypt the secret value | [optional] 
**target_location** | **str** | Target location in your Akeyless personal folder for migrated secrets | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**type** | **str** | Migration type for now only 1password. | [optional] [default to '1password']
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


