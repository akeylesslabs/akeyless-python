# CreateEventForwarder

createEventForwarder is a command that creates a new event forwarder [Deprecated - please use event-forwarder-create-* command]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** | Workstation Admin Name | [optional] 
**admin_pwd** | **str** | Workstation Admin password | [optional] 
**app_private_key_base64** | **str** | The RSA Private Key PEM formatted in base64 to use when connecting to ServiceNow with jwt authentication | [optional] 
**auth_type** | **str** | The authentication type to use when connecting to ServiceNow (user-pass / jwt) | [optional] [default to 'user-pass']
**client_id** | **str** | The client ID to use when connecting to ServiceNow with jwt authentication | [optional] 
**client_secret** | **str** | The client secret to use when connecting to ServiceNow with jwt authentication | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**email_to** | **str** | A comma seperated list of email addresses to send event to (relevant only for \&quot;email\&quot; Event Forwarder) | [optional] 
**event_source_locations** | **List[str]** | Event sources | 
**event_source_type** | **str** | Event Source type [item, target, auth_method, gateway] | [optional] [default to 'item']
**event_types** | **List[str]** | List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated] | [optional] 
**every** | **str** | Rate of periodic runner repetition in hours | [optional] 
**forwarder_type** | **str** |  | 
**host** | **str** | Workstation Host | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**key** | **str** | The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used) | [optional] 
**name** | **str** | EventForwarder name | 
**runner_type** | **str** |  | 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_email** | **str** | The user email to use when connecting to ServiceNow with jwt authentication | [optional] 

## Example

```python
from akeyless.models.create_event_forwarder import CreateEventForwarder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventForwarder from a JSON string
create_event_forwarder_instance = CreateEventForwarder.from_json(json)
# print the JSON string representation of the object
print(CreateEventForwarder.to_json())

# convert the object into a dict
create_event_forwarder_dict = create_event_forwarder_instance.to_dict()
# create an instance of CreateEventForwarder from a dict
create_event_forwarder_from_dict = CreateEventForwarder.from_dict(create_event_forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


