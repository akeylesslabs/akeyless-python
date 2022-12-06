# SetRoleRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **list[str]** | List of the approved/denied capabilities in the path options: [read, create, update, delete, list, deny] | 
**json** | **bool** | Set output format to JSON | [optional] 
**path** | **str** | The path the rule refers to | 
**role_name** | **str** | The role name to be updated | 
**rule_type** | **str** | item-rule, target-rule, role-rule, auth-method-rule, search-rule, reports-rule, gw-reports-rule or sra-reports-rule | [optional] [default to 'item-rule']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | RoleRule ttl | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


