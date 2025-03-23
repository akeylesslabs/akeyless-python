# WindowsTargetDetails

WindowsTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.windows_target_details import WindowsTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WindowsTargetDetails from a JSON string
windows_target_details_instance = WindowsTargetDetails.from_json(json)
# print the JSON string representation of the object
print(WindowsTargetDetails.to_json())

# convert the object into a dict
windows_target_details_dict = windows_target_details_instance.to_dict()
# create an instance of WindowsTargetDetails from a dict
windows_target_details_from_dict = WindowsTargetDetails.from_dict(windows_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


