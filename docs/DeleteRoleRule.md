# DeleteRoleRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**path** | **str** | The path the rule refers to | 
**role_name** | **str** | The role name to be updated | 
**rule_type** | **str** | item-rule, role-rule, auth-method-rule, search-rule, reports-rule, gw-reports-rule or sra-reports-rule | [optional] [default to 'item-rule']
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.delete_role_rule import DeleteRoleRule

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoleRule from a JSON string
delete_role_rule_instance = DeleteRoleRule.from_json(json)
# print the JSON string representation of the object
print(DeleteRoleRule.to_json())

# convert the object into a dict
delete_role_rule_dict = delete_role_rule_instance.to_dict()
# create an instance of DeleteRoleRule from a dict
delete_role_rule_from_dict = DeleteRoleRule.from_dict(delete_role_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


