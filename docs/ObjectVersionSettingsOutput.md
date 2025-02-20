# ObjectVersionSettingsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** | VersionSettingsObjectType defines object types for account version settings | [optional] 
**max_versions** | **str** |  | [optional] 

## Example

```python
from akeyless.models.object_version_settings_output import ObjectVersionSettingsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectVersionSettingsOutput from a JSON string
object_version_settings_output_instance = ObjectVersionSettingsOutput.from_json(json)
# print the JSON string representation of the object
print(ObjectVersionSettingsOutput.to_json())

# convert the object into a dict
object_version_settings_output_dict = object_version_settings_output_instance.to_dict()
# create an instance of ObjectVersionSettingsOutput from a dict
object_version_settings_output_from_dict = ObjectVersionSettingsOutput.from_dict(object_version_settings_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


