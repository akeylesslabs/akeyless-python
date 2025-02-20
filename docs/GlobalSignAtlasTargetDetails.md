# GlobalSignAtlasTargetDetails

GlobalSignAtlasTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_secret** | **str** |  | [optional] 
**mtls_cert** | **str** |  | [optional] 
**mtls_key** | **str** |  | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 

## Example

```python
from akeyless.models.global_sign_atlas_target_details import GlobalSignAtlasTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSignAtlasTargetDetails from a JSON string
global_sign_atlas_target_details_instance = GlobalSignAtlasTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GlobalSignAtlasTargetDetails.to_json())

# convert the object into a dict
global_sign_atlas_target_details_dict = global_sign_atlas_target_details_instance.to_dict()
# create an instance of GlobalSignAtlasTargetDetails from a dict
global_sign_atlas_target_details_from_dict = GlobalSignAtlasTargetDetails.from_dict(global_sign_atlas_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


