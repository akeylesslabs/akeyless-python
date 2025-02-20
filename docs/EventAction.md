# EventAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The Event Action [approve/deny] | 
**event_id** | **int** | The Event ID | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.event_action import EventAction

# TODO update the JSON string below
json = "{}"
# create an instance of EventAction from a JSON string
event_action_instance = EventAction.from_json(json)
# print the JSON string representation of the object
print(EventAction.to_json())

# convert the object into a dict
event_action_dict = event_action_instance.to_dict()
# create an instance of EventAction from a dict
event_action_from_dict = EventAction.from_dict(event_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


