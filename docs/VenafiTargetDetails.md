# VenafiTargetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venafi_api_key** | **str** |  | [optional] 
**venafi_base_url** | **str** |  | [optional] 
**venafi_tpp_access_token** | **str** |  | [optional] 
**venafi_tpp_client_id** | **str** |  | [optional] 
**venafi_tpp_password** | **str** | Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead | [optional] 
**venafi_tpp_refresh_token** | **str** |  | [optional] 
**venafi_tpp_username** | **str** | Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead | [optional] 
**venafi_use_tpp** | **bool** |  | [optional] 
**venafi_zone** | **str** |  | [optional] 

## Example

```python
from akeyless.models.venafi_target_details import VenafiTargetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VenafiTargetDetails from a JSON string
venafi_target_details_instance = VenafiTargetDetails.from_json(json)
# print the JSON string representation of the object
print(VenafiTargetDetails.to_json())

# convert the object into a dict
venafi_target_details_dict = venafi_target_details_instance.to_dict()
# create an instance of VenafiTargetDetails from a dict
venafi_target_details_from_dict = VenafiTargetDetails.from_dict(venafi_target_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


