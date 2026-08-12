# RotatedSecretSync

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_remote** | **bool** | Delete the secret from remote secret manager (for association create/update) | [optional] 
**environments** | **str** | GitHub environments to sync to. Relevant only for GitHub targets. Syncs to all environments defined on the selected USC by default, or to one or more specific repositories associated with that USC item when specified (e.g. --environments repo1/env1,repo2/env2). | [optional] 
**filter_secret_value** | **str** | JQ expression to filter or transform the secret value | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Rotated secret name | 
**namespace** | **str** | Vault namespace, releavnt only for Hashicorp Vault Target | [optional] 
**remote_secret_name** | **str** | Remote Secret Name that will be synced on the remote endpoint | [optional] 
**repositories** | **str** | GitHub repositories to sync to. Relevant only for GitHub targets. Syncs to all repositories defined on the selected USC by default, or to one or more specific repositories associated with that USC item when specified (e.g. --repositories repo1,repo2). | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**usc_name** | **str** | Universal Secret Connector name, If not provided all attached USC&#39;s will be synced | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


