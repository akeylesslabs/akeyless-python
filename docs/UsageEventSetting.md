# UsageEventSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**enable_time** | **datetime** |  | [optional] 
**interval_by_days** | **int** |  | [optional] 

## Example

```python
from akeyless.models.usage_event_setting import UsageEventSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UsageEventSetting from a JSON string
usage_event_setting_instance = UsageEventSetting.from_json(json)
# print the JSON string representation of the object
print(UsageEventSetting.to_json())

# convert the object into a dict
usage_event_setting_dict = usage_event_setting_instance.to_dict()
# create an instance of UsageEventSetting from a dict
usage_event_setting_from_dict = UsageEventSetting.from_dict(usage_event_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


