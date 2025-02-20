# DeleteRoleRuleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**result** | **str** |  | [optional] 

## Example

```python
from akeyless.models.delete_role_rule_output import DeleteRoleRuleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoleRuleOutput from a JSON string
delete_role_rule_output_instance = DeleteRoleRuleOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteRoleRuleOutput.to_json())

# convert the object into a dict
delete_role_rule_output_dict = delete_role_rule_output_instance.to_dict()
# create an instance of DeleteRoleRuleOutput from a dict
delete_role_rule_output_from_dict = DeleteRoleRuleOutput.from_dict(delete_role_rule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


