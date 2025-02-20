# AllowedIpSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_whitelist** | **str** |  | [optional] 
**lock** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.allowed_ip_settings import AllowedIpSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedIpSettings from a JSON string
allowed_ip_settings_instance = AllowedIpSettings.from_json(json)
# print the JSON string representation of the object
print(AllowedIpSettings.to_json())

# convert the object into a dict
allowed_ip_settings_dict = allowed_ip_settings_instance.to_dict()
# create an instance of AllowedIpSettings from a dict
allowed_ip_settings_from_dict = AllowedIpSettings.from_dict(allowed_ip_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


