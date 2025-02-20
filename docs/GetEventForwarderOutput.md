# GetEventForwarderOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_forwarder** | [**NotiForwarder**](NotiForwarder.md) |  | [optional] 

## Example

```python
from akeyless.models.get_event_forwarder_output import GetEventForwarderOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventForwarderOutput from a JSON string
get_event_forwarder_output_instance = GetEventForwarderOutput.from_json(json)
# print the JSON string representation of the object
print(GetEventForwarderOutput.to_json())

# convert the object into a dict
get_event_forwarder_output_dict = get_event_forwarder_output_instance.to_dict()
# create an instance of GetEventForwarderOutput from a dict
get_event_forwarder_output_from_dict = GetEventForwarderOutput.from_dict(get_event_forwarder_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


