# AllowedAccessUpdateArgs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | Access ID The access id to be attached to this allowed access. Auth method with this access id should already exist. | 
**description** | **str** | Allowed access description | [optional] 
**name** | **str** | Allowed access name | 
**new_name** | **str** | New allowed access name | [optional] 
**permissions** | **str** | Permissions  Comma-seperated list of permissions for this allowed access. Available permissions: [defaults,targets,classic_keys,automatic_migration,ldap_auth,dynamic_secret,k8s_auth,log_forwarding,zero_knowledge_encryption,rotated_secret,caching,event_forwarding,admin,kmip,general] | [optional] 
**sub_claims** | **dict(str, str)** | Sub claims key/val of sub claims, e.g group&#x3D;admins,developers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


