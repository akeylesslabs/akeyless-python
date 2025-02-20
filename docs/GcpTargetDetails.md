# GcpTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_service_account_email** | **str** |  | [optional] 
**gcp_service_account_key** | **str** |  | [optional] 
**gcp_service_account_key_base64** | **str** |  | [optional] 
**gcp_service_account_key_id** | **str** |  | [optional] 
**use_gw_cloud_identity** | **bool** |  | [optional] 

## Example

```python
from akeyless.models.gcp_target_details import GcpTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GcpTargetDetails from a JSON string
gcp_target_details_instance = GcpTargetDetails.from_json(json)
# print the JSON string representation of the object
print(GcpTargetDetails.to_json())

# convert the object into a dict
gcp_target_details_dict = gcp_target_details_instance.to_dict()
# create an instance of GcpTargetDetails from a dict
gcp_target_details_from_dict = GcpTargetDetails.from_dict(gcp_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


