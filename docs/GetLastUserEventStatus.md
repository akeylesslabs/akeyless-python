# GetLastUserEventStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | 
**item_name** | **str** | Event item name | 
**item_type** | **str** | Event item type can be either \&quot;target\&quot; or type of item eg \&quot;static_secret\&quot;/\&quot;dynamic_secret\&quot; To get type of some item run &#x60;akeyless describe-item -n {ITEM_NAME} --jq-expression .item_type&#x60; | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**time_back** | **str** | The time back to search the event, for example if the value is \&quot;5m\&quot; we will return the last user event issued in the last 5 minutes. By default, we will search without any time boundary. | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.get_last_user_event_status import GetLastUserEventStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetLastUserEventStatus from a JSON string
get_last_user_event_status_instance = GetLastUserEventStatus.from_json(json)
# print the JSON string representation of the object
print(GetLastUserEventStatus.to_json())

# convert the object into a dict
get_last_user_event_status_dict = get_last_user_event_status_instance.to_dict()
# create an instance of GetLastUserEventStatus from a dict
get_last_user_event_status_from_dict = GetLastUserEventStatus.from_dict(get_last_user_event_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


