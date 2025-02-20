# UpdateEventForwarder

updateEventForwarder is a command that updates an event forwarder [Deprecated - please use event-forwarder-update-* command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** | Workstation Admin Name | [optional] 
**auth_type** | **str** | The authentication type to use when connecting to ServiceNow (user-pass / jwt) | [optional] [default to 'user-pass']
**client_id** | **str** | The client ID to use when connecting to ServiceNow with jwt authentication | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_comment']
**email_to** | **str** | A comma seperated list of email addresses to send event to (relevant only for \&quot;email\&quot; Event Forwarder) | [optional] 
**enable** | **str** | Enable/Disable Event Forwarder [true/false] | [optional] [default to 'true']
**event_source_locations** | **List[str]** | Event sources | [optional] 
**event_types** | **List[str]** | Event types | [optional] 
**host** | **str** | Workstation Host | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | EventForwarder name | 
**new_comment** | **str** | Deprecated - use description | [optional] [default to 'default_comment']
**new_name** | **str** | New EventForwarder name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_email** | **str** | The user email to use when connecting to ServiceNow with jwt authentication | [optional] 

## Example

```python
from akeyless.models.update_event_forwarder import UpdateEventForwarder

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventForwarder from a JSON string
update_event_forwarder_instance = UpdateEventForwarder.from_json(json)
# print the JSON string representation of the object
print(UpdateEventForwarder.to_json())

# convert the object into a dict
update_event_forwarder_dict = update_event_forwarder_instance.to_dict()
# create an instance of UpdateEventForwarder from a dict
update_event_forwarder_from_dict = UpdateEventForwarder.from_dict(update_event_forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


