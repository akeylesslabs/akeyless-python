# GodaddyTargetDetails

GodaddyTargetDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imap_fqdn** | **str** |  | [optional] 
**imap_password** | **str** |  | [optional] 
**imap_port** | **str** |  | [optional] 
**imap_user** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**validation_email** | **str** |  | [optional] 

## Example

```python
from akeyless.models.godaddy_target_details import GodaddyTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GodaddyTargetDetails from a JSON string
godaddy_target_details_instance = GodaddyTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GodaddyTargetDetails.to_json())

# convert the object into a dict
godaddy_target_details_dict = godaddy_target_details_instance.to_dict()
# create an instance of GodaddyTargetDetails from a dict
godaddy_target_details_from_dict = GodaddyTargetDetails.from_dict(godaddy_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


