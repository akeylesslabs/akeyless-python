# GetEventForwarder

getEventForwarder is a command that creates a new event forwarder [Deprecated - please use event-forwarder-get command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | EventForwarder name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_event_forwarder import GetEventForwarder

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventForwarder from a JSON string
get_event_forwarder_instance = GetEventForwarder.from_json(json)
# print the JSON string representation of the object
print(GetEventForwarder.to_json())

# convert the object into a dict
get_event_forwarder_dict = get_event_forwarder_instance.to_dict()
# create an instance of GetEventForwarder from a dict
get_event_forwarder_from_dict = GetEventForwarder.from_dict(get_event_forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


