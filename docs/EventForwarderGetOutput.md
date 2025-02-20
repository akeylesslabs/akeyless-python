# EventForwarderGetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_forwarder** | [**NotiForwarder**](NotiForwarder.md) |  | [optional] 

## Example

```python
from akeyless.models.event_forwarder_get_output import EventForwarderGetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EventForwarderGetOutput from a JSON string
event_forwarder_get_output_instance = EventForwarderGetOutput.from_json(json)
# print the JSON string representation of the object
print(EventForwarderGetOutput.to_json())

# convert the object into a dict
event_forwarder_get_output_dict = event_forwarder_get_output_instance.to_dict()
# create an instance of EventForwarderGetOutput from a dict
event_forwarder_get_output_from_dict = EventForwarderGetOutput.from_dict(event_forwarder_get_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


