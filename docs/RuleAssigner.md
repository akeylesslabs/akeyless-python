# RuleAssigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 

## Example

```python
from akeyless.models.rule_assigner import RuleAssigner

# TODO update the JSON string below
json = "{}"
# create an instance of RuleAssigner from a JSON string
rule_assigner_instance = RuleAssigner.from_json(json)
# print the JSON string representation of the object
print(RuleAssigner.to_json())

# convert the object into a dict
rule_assigner_dict = rule_assigner_instance.to_dict()
# create an instance of RuleAssigner from a dict
rule_assigner_from_dict = RuleAssigner.from_dict(rule_assigner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


