# DynamicSecretUpdateGoogleWorkspace

dynamicSecretUpdateGoogleWorkspace is a command that updates a Google Workspace dynamic secret
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** |  | 
**admin_email** | **str** | Admin user email | 
**delete_protection** | **str** | Protection from accidental deletion of this item [true/false] | [optional] 
**description** | **str** | Description of the object | [optional] 
**gcp_key** | **str** | Base64-encoded service account private key text | [optional] 
**group_email** | **str** | A group email, relevant only for group access-mode | [optional] 
**group_role** | **str** |  | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Dynamic secret name | 
**new_name** | **str** | Dynamic secret new name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**role_name** | **str** | Name of the admin role to assign to the user, relevant only for role access-mode | [optional] 
**role_scope** | **str** |  | [optional] 
**tags** | **list[str]** | Add tags attached to this object | [optional] 
**target_name** | **str** | Name of existing target to use in dynamic secret creation | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL | [optional] [default to '60m']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


