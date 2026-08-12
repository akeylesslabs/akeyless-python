# RotatedSecretDeleteSync

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_from_usc** | **bool** | Delete the secret from the remote target USC as well | [optional] [default to False]
**environments** | **str** | GitHub environments to sync to. Relevant only for GitHub targets. Syncs to all environments defined on the selected USC by default, or to one or more specific repositories associated with that USC item when specified (e.g. --environments repo1/env1,repo2/env2). | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**remote_secret_name** | **str** | Remote Secret Name to disambiguate when multiple syncs exist under the same USC | [optional] 
**repositories** | **str** | GitHub repositories to delete from. Defaults to all repositories available on the selected USC. GitHub repositories to sync to. Relevant only for GitHub targets. Syncs to all repositories defined on the selected USC by default, or to one or more specific repositories associated with that USC item when specified (e.g. --repositories repo1,repo2). | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Universal Secret Connector name | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


