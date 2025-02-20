# CreateUserEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** | List of the required capabilities options: [read, update, delete,sra_transparently_connect]. Relevant only for request-access event types | [optional] 
**comment** | **str** | Deprecated - use description | [optional] 
**description** | **str** | Description of the object | [optional] 
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | 
**item_name** | **str** | EventItemName Event item name | 
**item_type** | **str** | EventItemType Event item type | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**request_access_ttl** | **int** | For how long to grant the requested access, in minutes | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.create_user_event import CreateUserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserEvent from a JSON string
create_user_event_instance = CreateUserEvent.from_json(json)
# print the JSON string representation of the object
print(CreateUserEvent.to_json())

# convert the object into a dict
create_user_event_dict = create_user_event_instance.to_dict()
# create an instance of CreateUserEvent from a dict
create_user_event_from_dict = CreateUserEvent.from_dict(create_user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


