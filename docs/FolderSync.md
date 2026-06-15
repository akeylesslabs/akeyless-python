# FolderSync

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **str** | for personal password manager | [optional] [default to 'regular']
**delete_remote** | **bool** | Delete the secret from the remote target as well | [optional] 
**engine_name** | **str** | Hashi Vault engine name prefix, must end with &#39;/&#39; | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Folder name | 
**namespace** | **str** | Vault namespace, relevant only for Hashicorp Vault Target | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Universal Secret Connector name, If not provided all attached USC&#39;s will be synced | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


