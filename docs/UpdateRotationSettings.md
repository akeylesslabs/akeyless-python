# UpdateRotationSettings

updateRotationSettings is a command that updates rotations settings of an existing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_rotate** | **bool** | Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation | 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**name** | **str** | Key name | 
**rotation_event_in** | **List[str]** | How many days before the rotation of the item would you like to be notified | [optional] 
**rotation_interval** | **int** | The number of days to wait between every automatic key rotation (7-365) | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 

## Example

```python
from akeyless.models.update_rotation_settings import UpdateRotationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRotationSettings from a JSON string
update_rotation_settings_instance = UpdateRotationSettings.from_json(json)
# print the JSON string representation of the object
print(UpdateRotationSettings.to_json())

# convert the object into a dict
update_rotation_settings_dict = update_rotation_settings_instance.to_dict()
# create an instance of UpdateRotationSettings from a dict
update_rotation_settings_from_dict = UpdateRotationSettings.from_dict(update_rotation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


