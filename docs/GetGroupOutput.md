# GetGroupOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**granted_roles** | [**list[GrantedRole]**](GrantedRole.md) | GrantedRoles are the roles a member of this group gets at login, through the group&#39;s akeyless_groups claim. Read-only, and filled only for the SCIM bearer that owns the group: a group name on its own says nothing about the access it carries, which is what a reviewer certifying the entitlement has to judge. | [optional] 
**granted_roles_known** | **bool** | GrantedRolesKnown is set when GrantedRoles was computed, so an empty list means \&quot;grants no role\&quot; rather than \&quot;not computed\&quot; (another caller, or an older UAM). | [optional] 
**group_alias** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**is_subclaims_with_operator** | **bool** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**scim_external_id** | **str** |  | [optional] 
**scim_managed** | **bool** |  | [optional] 
**scim_provisioned_access_id** | **str** |  | [optional] 
**user_assignments** | [**list[AccessPermissionAssignment]**](AccessPermissionAssignment.md) |  | [optional] 
**version** | **str** | Version identifies the member assignments this group was read with. Pass it back as UpdateGroupInput.ExpectedVersion to make the update conditional. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


