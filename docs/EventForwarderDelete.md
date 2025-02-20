# EventForwarderDelete

eventForwarderDelete is a command that delete event forwarder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | EventForwarder name | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.event_forwarder_delete import EventForwarderDelete

# TODO update the JSON string below
json = "{}"
# create an instance of EventForwarderDelete from a JSON string
event_forwarder_delete_instance = EventForwarderDelete.from_json(json)
# print the JSON string representation of the object
print(EventForwarderDelete.to_json())

# convert the object into a dict
event_forwarder_delete_dict = event_forwarder_delete_instance.to_dict()
# create an instance of EventForwarderDelete from a dict
event_forwarder_delete_from_dict = EventForwarderDelete.from_dict(event_forwarder_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


