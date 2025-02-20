# ListTargetsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**targets** | [**List[Target]**](Target.md) |  | [optional] 

## Example

```python
from akeyless.models.list_targets_output import ListTargetsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListTargetsOutput from a JSON string
list_targets_output_instance = ListTargetsOutput.from_json(json)
# print the JSON string representation of the object
print(ListTargetsOutput.to_json())

# convert the object into a dict
list_targets_output_dict = list_targets_output_instance.to_dict()
# create an instance of ListTargetsOutput from a dict
list_targets_output_from_dict = ListTargetsOutput.from_dict(list_targets_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


