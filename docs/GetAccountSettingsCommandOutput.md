# GetAccountSettingsCommandOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**address** | [**CustomerFullAddress**](CustomerFullAddress.md) |  | [optional] 
**company_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**general_settings** | [**AccountGeneralSettings**](AccountGeneralSettings.md) |  | [optional] 
**object_version_settings** | [**AccountObjectVersionSettingsOutput**](AccountObjectVersionSettingsOutput.md) |  | [optional] 
**phone** | **str** |  | [optional] 
**secret_management** | [**SmInfo**](SmInfo.md) |  | [optional] 
**secure_remote_access** | [**SraInfo**](SraInfo.md) |  | [optional] 
**system_access_creds_settings** | [**SystemAccessCredsSettings**](SystemAccessCredsSettings.md) |  | [optional] 

## Example

```python
from akeyless.models.get_account_settings_command_output import GetAccountSettingsCommandOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountSettingsCommandOutput from a JSON string
get_account_settings_command_output_instance = GetAccountSettingsCommandOutput.from_json(json)
# print the JSON string representation of the object
print(GetAccountSettingsCommandOutput.to_json())

# convert the object into a dict
get_account_settings_command_output_dict = get_account_settings_command_output_instance.to_dict()
# create an instance of GetAccountSettingsCommandOutput from a dict
get_account_settings_command_output_from_dict = GetAccountSettingsCommandOutput.from_dict(get_account_settings_command_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


