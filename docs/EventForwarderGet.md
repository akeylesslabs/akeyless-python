# EventForwarderGet

eventForwarderGet is a command that get event forwarder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | EventForwarder name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.event_forwarder_get import EventForwarderGet

# TODO update the JSON string below
json = "{}"
# create an instance of EventForwarderGet from a JSON string
event_forwarder_get_instance = EventForwarderGet.from_json(json)
# print the JSON string representation of the object
print(EventForwarderGet.to_json())

# convert the object into a dict
event_forwarder_get_dict = event_forwarder_get_instance.to_dict()
# create an instance of EventForwarderGet from a dict
event_forwarder_get_from_dict = EventForwarderGet.from_dict(event_forwarder_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


