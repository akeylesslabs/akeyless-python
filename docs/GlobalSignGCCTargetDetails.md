# GlobalSignGCCTargetDetails

GlobalSignGCCTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** | Contact Info - GlobalSign requires this to be sent with every certificate creation request | [optional] 
**last_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.global_sign_gcc_target_details import GlobalSignGCCTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSignGCCTargetDetails from a JSON string
global_sign_gcc_target_details_instance = GlobalSignGCCTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GlobalSignGCCTargetDetails.to_json())

# convert the object into a dict
global_sign_gcc_target_details_dict = global_sign_gcc_target_details_instance.to_dict()
# create an instance of GlobalSignGCCTargetDetails from a dict
global_sign_gcc_target_details_from_dict = GlobalSignGCCTargetDetails.from_dict(global_sign_gcc_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


