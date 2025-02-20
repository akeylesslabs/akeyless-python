# SystemAccessCredsSettings

SystemAccessCredsSettings describes system access credential settings for account by minutes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt_ttl_default** | **int** |  | [optional] 
**jwt_ttl_maximum** | **int** |  | [optional] 
**jwt_ttl_minimum** | **int** |  | [optional] 

## Example

```python
from akeyless.models.system_access_creds_settings import SystemAccessCredsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAccessCredsSettings from a JSON string
system_access_creds_settings_instance = SystemAccessCredsSettings.from_json(json)
# print the JSON string representation of the object
print(SystemAccessCredsSettings.to_json())

# convert the object into a dict
system_access_creds_settings_dict = system_access_creds_settings_instance.to_dict()
# create an instance of SystemAccessCredsSettings from a dict
system_access_creds_settings_from_dict = SystemAccessCredsSettings.from_dict(system_access_creds_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


