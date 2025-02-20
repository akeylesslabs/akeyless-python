# UpdateTargetDetails

updateTargetDetails is a command that updates an existing target. [Deprecated]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_json** | **bool** | Set output format to JSON | [optional] [default to False]

## Example

```python
from akeyless.models.update_target_details import UpdateTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTargetDetails from a JSON string
update_target_details_instance = UpdateTargetDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateTargetDetails.to_json())

# convert the object into a dict
update_target_details_dict = update_target_details_instance.to_dict()
# create an instance of UpdateTargetDetails from a dict
update_target_details_from_dict = UpdateTargetDetails.from_dict(update_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


