# SetRoleRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **List[str]** | List of the approved/denied capabilities in the path options: [read, create, update, delete, list, deny] | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | The path the rule refers to | 
**role_name** | **str** | The role name to be updated | 
**rule_type** | **str** | item-rule, target-rule, role-rule, auth-method-rule, search-rule, reports-rule, gw-reports-rule or sra-reports-rule, sra-rule | [optional] [default to 'item-rule']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**ttl** | **int** | RoleRule ttl | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.set_role_rule import SetRoleRule

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoleRule from a JSON string
set_role_rule_instance = SetRoleRule.from_json(json)
# print the JSON string representation of the object
print(SetRoleRule.to_json())

# convert the object into a dict
set_role_rule_dict = set_role_rule_instance.to_dict()
# create an instance of SetRoleRule from a dict
set_role_rule_from_dict = SetRoleRule.from_dict(set_role_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


