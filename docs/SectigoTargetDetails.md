# SectigoTargetDetails

SectigoTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_profile_id** | **int** |  | [optional] 
**customer_uri** | **str** |  | [optional] 
**external_requester** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from akeyless.models.sectigo_target_details import SectigoTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SectigoTargetDetails from a JSON string
sectigo_target_details_instance = SectigoTargetDetails.from_json(json)
# print the JSON string representation of the object
print(SectigoTargetDetails.to_json())

# convert the object into a dict
sectigo_target_details_dict = sectigo_target_details_instance.to_dict()
# create an instance of SectigoTargetDetails from a dict
sectigo_target_details_from_dict = SectigoTargetDetails.from_dict(sectigo_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


