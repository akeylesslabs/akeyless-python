# CreateKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_id** | **str** |  | [optional] 
**fragment_results** | **List[int]** |  | [optional] 
**item_id** | **int** |  | [optional] 

## Example

```python
from akeyless.models.create_key_output import CreateKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyOutput from a JSON string
create_key_output_instance = CreateKeyOutput.from_json(json)
# print the JSON string representation of the object
print(CreateKeyOutput.to_json())

# convert the object into a dict
create_key_output_dict = create_key_output_instance.to_dict()
# create an instance of CreateKeyOutput from a dict
create_key_output_from_dict = CreateKeyOutput.from_dict(create_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


