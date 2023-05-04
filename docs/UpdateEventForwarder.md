# UpdateEventForwarder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_name** | **str** | Workstation Admin Name | [optional] 
**description** | **str** | Description of the object | [optional] [default to 'default_comment']
**email_to** | **str** | A comma seperated list of email addresses to send event to (relevant only for \\\&quot;email\\\&quot; Event Forwarder) | [optional] 
**enable** | **str** | Enable/Disable Event Forwarder [true/false] | [optional] [default to 'true']
**event_source_locations** | **list[str]** | Event sources | [optional] 
**event_types** | **list[str]** | Event types | [optional] 
**host** | **str** | Workstation Host | [optional] 
**json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | EventForwarder name | 
**new_comment** | **str** | Deprecated - use description | [optional] [default to 'default_comment']
**new_name** | **str** | New EventForwarder name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

