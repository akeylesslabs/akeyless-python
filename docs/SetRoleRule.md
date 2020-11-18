# SetRoleRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **list[str]** | List of the approved/denied capabilities in the path options: [read, create, update, delete, list, deny] | 
**path** | **str** | The path the rule refers to | 
**role_name** | **str** | The role name to be updated | 
**rule_type** | **str** | item-rule, role-rule or auth-method-rule | [optional] [default to 'item-rule']
**token** | **str** | Use a specific profile from your akeyless/profiles/ folder | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


