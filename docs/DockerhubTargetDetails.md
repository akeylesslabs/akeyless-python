# DockerhubTargetDetails

DockerhubTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from akeyless.models.dockerhub_target_details import DockerhubTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DockerhubTargetDetails from a JSON string
dockerhub_target_details_instance = DockerhubTargetDetails.from_json(json)
# print the JSON string representation of the object
print(DockerhubTargetDetails.to_json())

# convert the object into a dict
dockerhub_target_details_dict = dockerhub_target_details_instance.to_dict()
# create an instance of DockerhubTargetDetails from a dict
dockerhub_target_details_from_dict = DockerhubTargetDetails.from_dict(dockerhub_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


