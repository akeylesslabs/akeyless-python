# PathRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigners** | [**List[RuleAssigner]**](RuleAssigner.md) |  | [optional] 
**capabilities** | **List[str]** | The approved/denied capabilities in the path | [optional] 
**cb** | **int** |  | [optional] 
**is_limit_access** | **bool** | flag that indicate that this rule is allowed to be access RemainingAccess of times. | [optional] 
**number_of_access_used** | **int** |  | [optional] 
**number_of_allowed_access** | **int** |  | [optional] 
**path** | **str** | The path the rule refers to | [optional] 
**start_time** | **int** |  | [optional] 
**ttl** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from akeyless.models.path_rule import PathRule

# TODO update the JSON string below
json = "{}"
# create an instance of PathRule from a JSON string
path_rule_instance = PathRule.from_json(json)
# print the JSON string representation of the object
print(PathRule.to_json())

# convert the object into a dict
path_rule_dict = path_rule_instance.to_dict()
# create an instance of PathRule from a dict
path_rule_from_dict = PathRule.from_dict(path_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


