# GetUserEventStatusOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_status** | **str** |  | [optional] 
**event_created_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from akeyless.models.get_user_event_status_output import GetUserEventStatusOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserEventStatusOutput from a JSON string
get_user_event_status_output_instance = GetUserEventStatusOutput.from_json(json)
# print the JSON string representation of the object
print(GetUserEventStatusOutput.to_json())

# convert the object into a dict
get_user_event_status_output_dict = get_user_event_status_output_instance.to_dict()
# create an instance of GetUserEventStatusOutput from a dict
get_user_event_status_output_from_dict = GetUserEventStatusOutput.from_dict(get_user_event_status_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


