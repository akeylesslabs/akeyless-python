# UpdateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelog** | **str** |  | [optional] 
**latest** | **str** |  | [optional] 
**updated** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.update_output import UpdateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOutput from a JSON string
update_output_instance = UpdateOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateOutput.to_json())

# convert the object into a dict
update_output_dict = update_output_instance.to_dict()
# create an instance of UpdateOutput from a dict
update_output_from_dict = UpdateOutput.from_dict(update_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


