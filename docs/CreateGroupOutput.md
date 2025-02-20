# CreateGroupOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_alias** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.create_group_output import CreateGroupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupOutput from a JSON string
create_group_output_instance = CreateGroupOutput.from_json(json)
# print the JSON string representation of the object
print(CreateGroupOutput.to_json())

# convert the object into a dict
create_group_output_dict = create_group_output_instance.to_dict()
# create an instance of CreateGroupOutput from a dict
create_group_output_from_dict = CreateGroupOutput.from_dict(create_group_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


