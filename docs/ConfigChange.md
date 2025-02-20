# ConfigChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_hash** | [**ConfigHash**](ConfigHash.md) |  | [optional] 
**last_change** | [**LastConfigChange**](LastConfigChange.md) |  | [optional] 
**last_status** | [**LastStatusInfo**](LastStatusInfo.md) |  | [optional] 
**required_activity** | [**RequiredActivity**](RequiredActivity.md) |  | [optional] 
**update_stamp** | **int** |  | [optional] 

## Example

```python
from akeyless.models.config_change import ConfigChange

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigChange from a JSON string
config_change_instance = ConfigChange.from_json(json)
# print the JSON string representation of the object
print(ConfigChange.to_json())

# convert the object into a dict
config_change_dict = config_change_instance.to_dict()
# create an instance of ConfigChange from a dict
config_change_from_dict = ConfigChange.from_dict(config_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


