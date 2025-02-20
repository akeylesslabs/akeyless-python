# EventForwarderCreateUpdateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_forwarder_id** | **int** |  | [optional] 
**event_forwarder_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.event_forwarder_create_update_output import EventForwarderCreateUpdateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EventForwarderCreateUpdateOutput from a JSON string
event_forwarder_create_update_output_instance = EventForwarderCreateUpdateOutput.from_json(json)
# print the JSON string representation of the object
print(EventForwarderCreateUpdateOutput.to_json())

# convert the object into a dict
event_forwarder_create_update_output_dict = event_forwarder_create_update_output_instance.to_dict()
# create an instance of EventForwarderCreateUpdateOutput from a dict
event_forwarder_create_update_output_from_dict = EventForwarderCreateUpdateOutput.from_dict(event_forwarder_create_update_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


