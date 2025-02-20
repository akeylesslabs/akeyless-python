# Update


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_repository** | **str** | Alternative CLI repository url. e.g. https://artifacts.site2.akeyless.io | [optional] 
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]
**show_changelog** | **bool** | Show the changelog between the current version and the latest one and exit (update will not be performed) | [optional] 
**version** | **str** | The CLI version | [optional] [default to 'latest']

## Example

```python
from akeyless.models.update import Update

# TODO update the JSON string below
json = "{}"
# create an instance of Update from a JSON string
update_instance = Update.from_json(json)
# print the JSON string representation of the object
print(Update.to_json())

# convert the object into a dict
update_dict = update_instance.to_dict()
# create an instance of Update from a dict
update_from_dict = Update.from_dict(update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


