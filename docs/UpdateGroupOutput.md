# UpdateGroupOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.update_group_output import UpdateGroupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupOutput from a JSON string
update_group_output_instance = UpdateGroupOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupOutput.to_json())

# convert the object into a dict
update_group_output_dict = update_group_output_instance.to_dict()
# create an instance of UpdateGroupOutput from a dict
update_group_output_from_dict = UpdateGroupOutput.from_dict(update_group_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


